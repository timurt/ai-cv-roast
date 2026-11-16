#!/usr/bin/env python3
"""ATS parsing check for a CV.

Usage: python3 -I ats_check.py <cv.pdf|cv.docx|cv.txt>

Prints the text an ATS would see, then a list of parsing problems:
lost fi/fl/ff ligatures, garbled characters, en/em-dash date ranges,
bare years, missing contacts, two-column interleaving and junk symbols.
Needs `pdftotext` (poppler) for PDFs; uses macOS `textutil` for DOCX.
"""
import datetime
import os
import re
import subprocess
import sys

DICT_PATHS = ["/usr/share/dict/words", "/usr/dict/words"]
LIGS = ["ffi", "ffl", "fi", "fl", "ff"]
MONTH = r"(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Sept|Oct|Nov|Dec)[a-z]*\.?"


def run(cmd):
    try:
        return subprocess.run(cmd, capture_output=True, text=True, check=True).stdout
    except (OSError, subprocess.CalledProcessError) as e:
        sys.exit(f"Could not run {cmd[0]}: {e}")


def extract(path):
    ext = os.path.splitext(path)[1].lower()
    if ext == ".pdf":
        return run(["pdftotext", "-layout", "-enc", "UTF-8", path, "-"]), run(
            ["pdftotext", "-enc", "UTF-8", path, "-"]
        )
    if ext in (".docx", ".doc", ".rtf"):
        t = run(["textutil", "-convert", "txt", "-stdout", path])
        return t, t
    with open(path, encoding="utf-8", errors="replace") as f:
        t = f.read()
    return t, t


def load_words():
    for p in DICT_PATHS:
        if os.path.exists(p):
            with open(p, encoding="utf-8", errors="ignore") as f:
                return {w.strip().lower() for w in f if w.strip()}
    return set()


# Common tech-CV words that may be missing from the system dictionary.
EXTRA_WORDS = {"configs", "diffs", "flakiness", "flaky", "workflow", "workflows", "offline",
               "efficient", "efficiently", "efficiency", "profiling", "profile", "financial",
               "fixed", "first", "field", "files", "find", "fine", "fit", "flag", "flags",
               "traffic", "staff", "office", "official", "offer", "offers", "offering",
               "certified", "identified", "simplified", "verified", "modified", "notifications",
               "configured", "configuration", "flutter", "fluent", "fluency", "flow", "flows",
               "flask", "fintech", "affect", "affecting", "differ", "different", "difference",
               "effort", "efforts"}
SUFFIXES = ("", "s", "es", "ed", "ing", "er", "ers", "ly", "ation", "ations")


def is_word(w, words):
    w = w.lower()
    for suf in SUFFIXES:
        if suf and not w.endswith(suf):
            continue
        stem = w[: len(w) - len(suf)] if suf else w
        if len(stem) >= 2 and (stem in words or stem + "e" in words):
            return True
    return False


def ligature_losses(text, words):
    """Find words that only make sense with a dropped fi/fl/ff glyph.

    Heuristic: may still miss rare words, so callers should report the count as "at least N".
    """
    words = words | EXTRA_WORDS
    if not words:
        return []
    hits = {}
    tails = set()
    # case 1: glyph dropped inside a word, leaving a space: "e cient", "di s", "pro le", "cPro le"
    for m in re.finditer(r"(?=\b([A-Za-z]{1,14}) ([a-z]{1,14})\b)", text):
        a, b = m.group(1), m.group(2)
        if is_word(a, words) and is_word(b, words) and len(a) > 3 and len(b) > 3:
            continue
        # allow a camel-case prefix like "cPro" -> try the capitalised tail too
        heads = [a] + [a[i:] for i in range(1, len(a)) if a[i].isupper()]
        for head in heads:
            done = False
            for lig in LIGS:
                cand = head + lig + b
                if len(cand) >= 4 and is_word(cand, words):
                    hits[f"{a} {b}"] = a[: len(a) - len(head)] + cand
                    tails.add(b)
                    done = True
                    break
            if done:
                break
    # case 2: glyph dropped at the start of a word: "nancial", "rst", "xed", "nd", "scalizer"
    for m in re.finditer(r"(?<![A-Za-z\-])([a-z]{2,16})\b", text):
        w = m.group(1)
        if w in tails or is_word(w, words) or text[m.end():m.end() + 1] == "/" or text[max(0, m.start() - 1):m.start()] == "/":
            continue
        for lig in LIGS:
            cand = lig + w
            if (len(cand) >= 5 or cand in EXTRA_WORDS) and is_word(cand, words):
                hits[w] = cand
                break
    return sorted(hits.items())


MONTHS = {m: i + 1 for i, m in enumerate(
    ["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"])}


def _ym(tok, ref):
    """Parse a date token to (year, month, year_only). 'present' -> ref."""
    t = tok.strip().lower().rstrip(".")
    if t in ("present", "now", "current", "today"):
        return ref[0], ref[1], False
    m = re.fullmatch(r"([a-z]{3})[a-z]*\.?\s*(\d{4})", t)
    if m and m.group(1) in MONTHS:
        return int(m.group(2)), MONTHS[m.group(1)], False
    m = re.fullmatch(r"(\d{1,2})/(\d{4})", t)
    if m:
        return int(m.group(2)), int(m.group(1)), False
    m = re.fullmatch(r"(\d{4})", t)
    if m:
        return int(m.group(1)), None, True
    return None


def cv_date(raw, path):
    """Best guess of when the CV was written: (year, month, source) or None."""
    upd = re.search(rf"(?:Updated|Last updated)\s+({MONTH})\s+\d{{0,2}}\w*,?\s*(\d{{4}})", raw, re.I)
    if upd and MONTHS.get(upd.group(1)[:3].lower()):
        return int(upd.group(2)), MONTHS[upd.group(1)[:3].lower()], f"'Updated' line ({upd.group(1)} {upd.group(2)})"
    name = os.path.basename(path)
    m = re.search(r"(?<!\d)(0?[1-9]|1[0-2])[:._-](\d{2})(?!\d)", name)  # e.g. "07:24", "07-24"
    if m:
        return 2000 + int(m.group(2)), int(m.group(1)), f"file name '{m.group(0)}'"
    m = re.search(r"(?<!\d)(20\d{2})(?!\d)", name)
    if m:
        return int(m.group(1)), 12, f"file name year {m.group(1)} (month unknown, Dec assumed)"
    if path.lower().endswith(".pdf"):
        try:
            info = subprocess.run(["pdfinfo", path], capture_output=True, text=True).stdout
            d = re.search(r"CreationDate:\s+\w{3}\s+(\w{3})\s+\d+\s+[\d:]+\s+(\d{4})", info)
            if d and MONTHS.get(d.group(1).lower()):
                return int(d.group(2)), MONTHS[d.group(1).lower()], f"PDF creation date ({d.group(1)} {d.group(2)})"
        except OSError:
            pass
    return None


def timeline(raw, path):
    """Extract date ranges with exact durations, overlaps and gaps."""
    today = datetime.date.today()
    found = cv_date(raw, path)
    if found:
        ref = (found[0], found[1])
        ref_note = f"'present' = CV date from {found[2]}"
    else:
        ref = (today.year, today.month)
        ref_note = (f"'present' = today ({today:%b %Y}); CV date unknown, so don't claim recency "
                    "or gaps measured to 'present'")
    tok = rf"(?:{MONTH}\s*\d{{4}}|\d{{1,2}}/\d{{4}}|\d{{4}})"
    pat = rf"({tok})\s*[-–—]+\s*({tok}|present|now|current)"
    rows = []
    for m in re.finditer(pat, raw, re.I):
        a, b = _ym(m.group(1), ref), _ym(m.group(2), ref)
        if not a or not b:
            continue
        line = raw[max(0, raw.rfind("\n", 0, m.start()) + 1): m.start()].strip()
        label = (line[:60] or raw[max(0, m.start() - 60):m.start()].replace("\n", " ").strip()[-60:])
        year_only = a[2] or b[2]
        if year_only:
            lo = (b[0] - a[0] - 1) * 12 + 1 if b[0] > a[0] else 1
            hi = (b[0] - a[0] + 1) * 12 - 1
            dur = f"{max(lo, 1)}-{hi} months (year-only dates)"
            start, end = (a[0], a[1] or 1), (b[0], b[1] or 12)
        else:
            months = (b[0] - a[0]) * 12 + (b[1] - a[1])
            dur = f"{months} months ({months / 12:.1f} yrs)"
            start, end = (a[0], a[1]), (b[0], b[1])
        rows.append((start, end, m.group(0).strip(), dur, label, year_only))
    rows.sort()
    out = [f"(computed by script; {ref_note}; durations = end month - start month)"]
    for s, e, txt, dur, label, _ in rows:
        out.append(f"- {txt}: {dur}   [{label}]")
    for (s1, e1, t1, _, _, y1), (s2, e2, t2, _, _, y2) in zip(rows, rows[1:]):
        if (y1 or y2) and s2[0] >= e1[0]:
            continue  # year-only boundary year shared: not a real overlap
        if s2 < e1:
            out.append(f"- OVERLAP: '{t2}' starts before '{t1}' ends (check it is labelled, or is education)")
        else:
            gap = (s2[0] - e1[0]) * 12 + (s2[1] - e1[1])
            if gap >= 6:
                out.append(f"- GAP of {gap} months between '{t1}' and '{t2}'")
    return out


def main():
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    path = sys.argv[1]
    layout, raw = extract(path)
    words = load_words()
    issues = []

    lig = ligature_losses(raw, words)
    if lig:
        shown = ", ".join(f'"{a}" -> {b}' for a, b in lig[:15])
        issues.append(f"LOST LIGATURES (at least {len(lig)} words): {shown}. These words are unsearchable. "
                      "Re-export the PDF (Word/Google Docs 'Download as PDF' or LaTeX) and re-check.")

    garbled = re.findall(r"\(cid:\d+\)|�", raw)
    if garbled:
        issues.append(f"GARBLED TEXT: {len(garbled)} unreadable glyphs like {garbled[0]}.")

    dash_ranges = re.findall(
        rf"(?:{MONTH}\s*)?\b(?:\d{{1,2}}/)?\d{{4}}\s*[–—]\s*(?:{MONTH}\s*)?(?:\d{{1,2}}/)?(?:\d{{4}}|[Pp]resent|PRESENT|[Nn]ow|[Cc]urrent)",
        raw,
    )
    if dash_ranges:
        issues.append(f"EN/EM-DASH DATE RANGES ({len(dash_ranges)}, first {min(5, len(dash_ranges))} shown): {dash_ranges[:5]}. "
                      "Some parsers don't split on them; use a plain hyphen 'Mar 2021 - Nov 2022'.")

    year_only = [
        m.group(0)
        for m in re.finditer(r"(?<![/\d])\b(?:19|20)\d{2}\s*[-–—]\s*(?:(?:19|20)\d{2}|[Pp]resent|PRESENT)\b", raw)
        if not re.search(rf"{MONTH}\s*$", raw[max(0, m.start() - 12):m.start()])
    ]
    if year_only:
        issues.append(f"YEAR-ONLY RANGES ({len(year_only)}): {year_only[:5]}. Recent roles should show months.")

    formats = set()
    if re.search(rf"\b{MONTH}\s+\d{{4}}", raw):
        formats.add("Mon YYYY")
    if re.search(r"\b\d{1,2}/\d{4}\b", raw):
        formats.add("MM/YYYY")
    if year_only:
        formats.add("YYYY")
    if len(formats) > 1:
        issues.append(f"MIXED DATE FORMATS: {sorted(formats)}. Pick one.")

    email = re.search(r"[\w.+-]+@[\w-]+\.[\w.]+", raw)
    phone = next((m for m in re.finditer(r"\+?\(?\d[\d ()-]{7,}\d", raw)
                  if len(re.sub(r"\D", "", m.group(0))) >= 9
                  and not re.fullmatch(r"(?:19|20)\d{2}\s*-\s*(?:19|20)\d{2}", m.group(0).strip())), None)
    linkedin = re.search(r"linkedin\.com/in/[\w-]+", raw, re.I)
    head = "\n".join(raw.strip().splitlines()[:8])
    if not email:
        issues.append("NO EMAIL in the text layer.")
    elif email.group(0) not in head:
        issues.append("EMAIL NOT AT THE TOP: it appears below the first 8 lines (likely footer/bottom).")
    if not phone:
        issues.append("NO PHONE NUMBER in the text layer.")
    if not linkedin:
        label = re.search(r"\bLinkedIn\b", raw)
        issues.append("LINKEDIN URL NOT VISIBLE" + (" (only the word 'LinkedIn' - the URL is hidden behind a link)." if label else "."))

    # two-column heuristic: many layout lines with a wide gap between two text blocks
    split_lines = [l for l in layout.splitlines() if re.search(r"\S {8,}\S", l.strip()) and len(l.strip()) > 60]
    bullets_right = [l for l in split_lines if re.search(r" {8,}[•●◦\-–]\s", l)]
    if len(bullets_right) >= 3 or len(split_lines) > 25:
        issues.append(f"POSSIBLE MULTI-COLUMN LAYOUT: {len(split_lines)} lines carry two text blocks side by side; "
                      "reading order may interleave.")

    junk = sorted(set(re.findall(r"[∼#-]", raw)))
    if junk:
        issues.append(f"SYMBOLS THAT MAY PARSE AS JUNK: {junk}.")

    if re.search(r"\b(Updated|Last updated)\b.{0,30}\d{4}", head):
        issues.append("'Updated <date>' line at the top: the ATS reads it before your name.")

    name = os.path.basename(path)
    if re.search(r"\(\d\)|^cv\b|copy|final|:\d\d", name, re.I):
        issues.append(f"FILE NAME '{name}' looks unprofessional; use Firstname-Lastname-CV.pdf.")

    print("=== TEXT AS AN ATS SEES IT (layout) ===")
    print(layout)
    print("=== PARSING ISSUES ===")
    print("\n".join(f"- {i}" for i in issues) if issues else "- none found")
    print("=== TIMELINE (all date ranges found, sorted; includes education) ===")
    print("\n".join(timeline(raw, path)))


if __name__ == "__main__":
    main()
