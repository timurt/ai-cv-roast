# Roast mode

Paths are relative to the skill folder. The router (SKILL.md) has already loaded the references, run the scripts and set the target role.

## Review the CV top to bottom
Go through each playbook section (A → F) against this CV and note every breach, quoting the exact text. Then check yourself before writing:
- [ ] Contacts: position, location, phone, email, LinkedIn as visible text?
- [ ] Is there a headline/title and a summary? Does the summary have tech + numbers?
- [ ] Skills: present, near the top, grouped by category?
- [ ] Role headers: consistent Company — Title — Location — Dates? Months present?
- [ ] Bullet count per role (target 3–4, even for the current role; flag 5+ and 1–2) and older roles to condense or cut.
- [ ] Length: an explicit page target (≈1 page per 10 years, max 2). Layout: if 2+ format breaches, one "rebuild layout" verdict.
- [ ] **Every bullet audited**: result? number? how/tech? verb? Vague quantifiers?
- [ ] Strong bullets identified and protected (never told to cut).
- [ ] Tech placement: inside bullets vs "Technologies used" lines or parentheses after titles.
- [ ] Leadership claims have team size + outcome?
- [ ] Italics, columns, colours, icons, pills, centred blocks, missing bullet markers?
- [ ] Education and certifications: old, irrelevant or yearless items; in-progress degrees labelled.
- [ ] Extras: interests, clubs, language lists, taglines, "Updated" lines.
- [ ] Style (playbook 44–45, from `text_stats.py`): bullets over ~30 words, the same verb opening many bullets, filler words. Route them into the bullet tables, the Summary row of the section check, or Red flags; no new section.
- [ ] **Timeline:** use the script's TIMELINE section as the only source for tenures, overlaps and gaps; never do date arithmetic yourself. Ignore rows that are education or awards. Overlaps between jobs → flag unless labelled; gaps of 6+ months → flag; tenure under 12 months → note. Year-only dates give a range ("1–2 years"); never say "at most" or pick one value. If there is no script output (pasted text), list the dates and don't state durations.
- [ ] File name.
- [ ] Every parsing issue from the script, explained in plain words.
- [ ] **[R] map** (private): go through playbook [R] rules 1, 3, 4, 6, 8, 9, 12, 13, 15, 16, 17, 23, 26, 27, 28, 28a one by one. Mark each as "not breached" or "breached → fix #". Every breached rule needs an item in "Fix these first". If the bullet tables flag 3+ weak verbs, there is a verbs item (or one merged "Sharpen the bullets" item that names verbs, vague words and results).

## Output: exactly this structure
The reader is the candidate, not a recruiter: plain words, short lines, the action first. Use these exact `##` headings in this order. **Budget: 1,300–1,800 words total.** Each problem is written out **once**, in the section it belongs to (routing rules below); every other mention is a short pointer like "(see Acme #3)".

Never show internal labels in the output: no "[R]", rule numbers, "playbook", "§", "TIMELINE section", "script", "JD INTEGRITY". Say "the parser" or "the text an ATS reads" instead of naming scripts.

**Numbers you state about the CV:**
- Tenures, gaps and overlaps come only from the script's TIMELINE.
- Script counts are minimums: write "at least N".
- Any other count must list its items right after it, e.g. "'Led' opens 4 bullets (Acme #1, #4; Globex #4, #5)". If you can't list them, don't state a number; describe the pattern instead ("most bullets").
- The verdict, first impression and section check must not contradict the bullet tables.
- Years of experience are measured to the CV's own date (the "Updated" line or the year in the file name) when there is one, not to today.

### `## Verdict: Strong / Needs work / Weak`
In JD mode this heading becomes `## CV verdict (general): …`. Then three short lines, ≤ 60 words in total:
- **Reviewed as:** <target role> (<why: stated, or latest title>)
- **Biggest problem:** <one line>
- **Highest-value fix:** <one line>

### `## Fix these first`
6–10 numbered items in priority order, biggest shortlist impact first. Usually: missing summary/skills/contacts → layout verdict → bullets with no results → bullet count and old roles → parsing → extras. Each item, ≤ 40 words:
`1. **<What to do, as a command>**: <the problem, quoted or "missing">. <Where and how>. _Why:_ <≤ 12 words>. `<effort>``
Effort is exactly one of `quick edit`, `needs work`, `needs info`.
**Every [R]-rule breach you found must appear here**, on its own or merged into an item (e.g. "Rebuild the layout" covers columns, contact position and italics). Commonly dropped, so check for them: role header format, vague-quantifier bullets, tech placement. Hard limit of 10: merge by theme (e.g. one "Sharpen the bullets" item pointing to the bullet tables). The length target goes inside the layout or structure item, never as an item of its own. Items point to the bullet tables instead of re-quoting long text.

### `## First impression (7 seconds)`
≤ 60 words. What a recruiter takes from the top third (name, title, current and previous company, dates, progression) and whether the fit is obvious. Progression comments live here only.

### `## Section check`
| Section | | Note |
|---|---|---|
Rows: Header & contacts, Summary, Skills, Experience structure, Bullet quality, Education & certs, Extras, Format & length, ATS parsing. The middle column is ✅ / ⚠️ / ❌. Note ≤ 12 words.

### `## Bullet by bullet`
First line: `✅ keep · ✏️ sharpen · 🔀 merge · ✂️ cut`
Then, per role, a `###` heading `<Company>: <Title> · <N> bullets → <role verdict>` and one table covering every bullet. The role verdict is one of **keep** / **cut to 3–4 bullets** / **add 1–2 bullets** (long role, thin bullets) / **condense to 1–2 lines** / **cut the role**. Decide it with playbook rule 9 first, then rule 8: a short stint off the target path (e.g. a 6-month DevOps or QA role in a backend CV), an early freelance gig or a role 10+ years back gets **condense** or **cut** even when its bullet count is fine. Never write just "fine".
| # | Bullet | Verdict | What's missing / what to do |
- **Bullet:** quoted, first ~10 words + ….
- **Verdict:** ✅ keep, ✏️ sharpen, 🔀 merge with #n, or ✂️ cut.
- **What's missing / what to do** (≤ 12 words, one fix only): name what is missing from result / number / tech / strong past-tense verb, plus any vague word or weak verb quoted (e.g. `result, number; vague "significantly"`). For a ✅ row write "—" or a tiny tweak ("Lead" → "Led").
A bullet that shows real production **scale or adoption** (users, orders/day, rps, number of teams or engineers using it) but no outcome gets **✅ keep** with "add the outcome (question N)". It is never sharpen or cut, and treat all such bullets in the CV the same way.
This section is the **only** place for bullet-level problems: vague words, weak or "-ing" verbs, missing results, and tweaks to ✅ bullets. After a table, add at most one line on the role itself if needed: which bullets to merge, header format, tech placement, whether to condense or drop the role. Roles older than ~8 years may be covered in one line instead of a table.

### `## Red flags`
≤ 5 bullets. Only CV-wide or cross-role items: timeline issues (overlaps, gaps, short stints), overclaims, CV-wide patterns (e.g. "every bullet opens with 'Implemented'"), inconsistent tech names. Don't re-list vague words or verbs already in the bullet tables, and don't repeat leadership or result gaps already in a verdict. **Nothing from a ✅ bullet appears here, not even a typo** (typos inside a ✅ bullet go in its table row). Group the other typos into one line. Symbols and date formats belong in ATS parsing. If there are none, write "None found."

### `## ATS parsing`
Bullets, each `<problem> → <concrete fix>` (e.g. "Dates use en dashes (`Apr. 2023 – present`) → write `Apr 2023 - Present`"). Every issue the parser found plus anything visible in the layout, in plain words.

### `## Questions for you`
≤ 10, numbered, aimed at the weak bullets with the most impact (use playbook section H). Ask for the fact only; don't restate why it matters. Point to the bullet: "(Acme #2) 'Published an open-source SDK': how many customers integrated it, or how many GitHub stars/downloads?" Merge related ones.

End with one line: "Add every number you confirm to your master CV, and for each job you apply to rerun `/cv-roast <cv> <job link or text>`: AI screeners rank on how closely the CV matches that specific job."

**Before you finish:** estimate the word count. If it's over 1,800, cut in this order: Red flags, the _Why_ parts of the fix items, the per-role notes, then Questions. Never cut bullet-table rows or the verdict. Re-check that every number in the verdict, first impression and section check is copied from your tables or the script. **Dedupe pass:**
- Scan Red flags and First impression. Any point already in the bullet tables or ATS parsing becomes a short pointer, or is removed.
- Delete from Red flags and Fix these first any word quoted from a ✅ row.

If the script's TIMELINE says the CV date is unknown, make no recency or gap claims measured to "present".

## Style rules
- Quote, don't paraphrase. Every criticism points at real text or says "missing".
- Be specific: "Add the result to 'Built Single sign-on service'", not "add more metrics".
- Protect what works. Explicitly call out the strong bullets so the user doesn't cut them.
- Don't suggest adding skills, numbers or titles the CV doesn't support. Ask instead.
- Keep it tight: tables over prose, no intro or outro chatter, no repeated points.
- Weight matters: real shortlist blockers first and in full; nitpicks grouped and short.
- Describe the CV exactly (playbook 39a): only tech, counts and years that appear in the text.
