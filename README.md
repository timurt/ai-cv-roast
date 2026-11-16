# CV Roast: a CV review skill for Claude Code

A [Claude Code](https://claude.com/claude-code) skill, `/cv-roast`, that reviews engineering CVs the way a tech recruiter and an ATS would.

- **CV only**: a blunt review of the CV on its own. The report opens with a verdict and a prioritised "Fix these first" list, then shows the first impression, a section check, a verdict for every bullet, red flags, ATS parsing problems, and questions that pull out missing numbers.
- **CV + job description**: a verdict for that job at the top (would this CV get shortlisted?), then the same general review as Part 1, then Part 2, fit for this job: deal-breakers, whether recruiter searches find you, a keyword table, an A–D AI match grade, a recruiter read, tailoring fixes and cover-letter points. Part 2 points back to Part 1 instead of repeating it, and the questions are merged into one list.

The same rules apply to every CV, whatever the country: about 1 page per 10 years (max 2), consistent spelling, no photo or personal details, and work rights next to your contacts if you need a visa.

The skill never rewrites your CV or invents facts. It tells you what to change and asks for the numbers it needs.

## Requirements
- Claude Code
- Python 3
- `pdftotext` for PDFs (`brew install poppler` / `apt install poppler-utils`)
- DOCX files are read with macOS `textutil`. On other systems, export to PDF first.

## Install
Clone the repo and run Claude Code inside it. The skill is picked up from `.claude/skills/`.

To use it in any project, copy the skill folder into your user skills directory:
```
cp -r .claude/skills/cv-roast ~/.claude/skills/
```

## Usage
```
/cv-roast ~/Downloads/My-CV.pdf
/cv-roast ~/Downloads/My-CV.pdf target: Senior Backend Engineer
/cv-roast ~/Downloads/My-CV.pdf https://careers.example.com/jobs/123
/cv-roast ~/Downloads/My-CV.pdf   (then paste the job description in the same message)
```

### What to prepare
**Any review**
- The exact PDF/DOCX you send out, not the Word/LaTeX source. The skill checks what an ATS actually reads.
- Optional: target role and level.

**With a job description**
- The **full JD, verbatim**. Prefer the employer's careers-page copy, because aggregators often drop the level and requisition ID.
- Optional but useful: your location and work rights, screening questions from the application form, your LinkedIn text or cover letter, and **extra facts**: true things that aren't on the CV (metrics, tools, scope).

## Layout
```
.claude/skills/cv-roast/
  SKILL.md                  router: picks roast or roast + JD, runs the scripts
  modes/roast.md            roast output format
  modes/jd-match.md         JD match output format (Part 2, JD mode only)
  references/playbook.md    all CV rules
  references/examples.md    calibration examples: strong vs weak lines
  scripts/ats_check.py      shows the text an ATS sees, parsing issues and a timeline
  scripts/text_stats.py     readability, repeated words, filler; with --jd, a lexical CV↔JD fit and a JD integrity check
```

`ats_check.py` also works on its own:
```
python3 -I .claude/skills/cv-roast/scripts/ats_check.py My-CV.pdf
```

## Which model to use for edits
This skill diagnoses; you (or a model) write the final wording. If you use AI to draft or rephrase CV text, the choice of model can matter when the employer screens with an LLM. An audit of 9 LLM screeners scoring 5,500 AI-written application texts (Pagan et al., *AI evaluators favor job applications written by certain AI models, independent of candidate quality*, arXiv 2610.41866, Oct 2026) found:

- **Avoid small local models** (~8B, e.g. Llama-3.1-8B, DeepSeek-R1-8B). Every screener ranked their text lowest (36–42% head-to-head win rate). In the worst pairing, about 2 of every 25 qualified candidates lost their place because of the writing model alone.
- **Use a current frontier hosted model.** The top writers were Gemini 3.5 Flash and GPT-5-mini (56% each) and DeepSeek V3.2 (54%). Claude Haiku 4.5 was the weakest hosted model (47%), and Claude Sonnet 4.6 ranked 7th of 11.
- **Screeners favour their own model's text** (self-preference). Drafting with the same model family as the employer's screener helps, but you rarely know which one they use.
- **Content beats the model.** Once the screener sees the CV, writer effects shrink a lot (the largest preference gap dropped from +0.45 to +0.12 on a 10-point scale). Semantic fit to the JD and specific, true bullets matter more. That is what `/cv-roast` with a JD checks.

Caveats: the study measured AI-written cover letters, not CVs, so applying it to CV text is an inference. The model ranking will shift as models update. Running the skill in Claude Code for the diagnosis is fine; this advice is about which model writes the final wording.

The playbook's section I (LLM screeners) is based on the same paper. `text_stats.py` gives a lexical proxy for CV↔JD fit, not the paper's embedding score.

## Built on real recruiter feedback
`/cv-roast` isn't generic resume advice. It was tuned against real engineering CVs that recruiters annotated line by line, so it flags what a recruiter actually objects to and leaves strong bullets alone. On top of that, its playbook brings together hiring best practices from recruiters at several large international tech companies, so you get the kind of feedback that usually takes a referral and a favour to get.

The source CVs are kept private to protect the people they belong to. The examples in `references/` are illustrative.
