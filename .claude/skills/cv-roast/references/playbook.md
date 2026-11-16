# CV Review Playbook

The single source of rules for `/cv-roast` (both the roast and the JD match mode). Distilled from a tech recruiter's annotations on engineering CVs and common ATS screening practice.

Each rule says what to check and what to flag. Rules marked **[R]** were raised repeatedly by the recruiter: treat a breach as a must-mention.

---

## A. Top of page 1 (the 7-second skim)

A recruiter looks at name → current title → current company → previous title/company → dates → education, in that order. Fit must be obvious from the top third of page 1.

1. **[R] Contacts at the top.** Name, target title, city + country, phone, email, LinkedIn (and GitHub/portfolio for engineers). Flag:
   - contacts placed at the bottom or in a footer;
   - a missing location, phone or LinkedIn;
   - links that only show a label ("LinkedIn | Website | GitHub") with the URL hidden behind it: a parser and a printed copy both lose them. Print the URL as text (`linkedin.com/in/name`).
1a. **Work rights near the contacts** when the candidate may need a visa for the jobs they target (e.g. their location is in a different country from the role, or they say they are relocating). Plain words: "Full working rights in <country>", "Permanent resident", "Requires visa sponsorship".
2. **Headline/title under the name** matching the target role (e.g. "Senior Backend Engineer"). Flag taglines instead of a title ("Passionate problem-solver with a love of learning").
3. **[R] Summary is mandatory.** 2–3 lines: target title + years + core stack + 1–2 strongest proof points with numbers. Flag:
   - no summary at all;
   - a summary with no concrete tech or results ("7 years of experience across many areas of software development");
   - a generic, long summary that could belong to anyone (buzzwords, adjectives, no numbers). Ask to shorten it and put results in.
4. **[R] Skills section near the top, grouped by category.** E.g. Languages / Frameworks / Data & Messaging / Cloud & DevOps / Frontend. Flag:
   - no skills section;
   - skills at the bottom of the CV;
   - one flat comma list mixing languages, databases and tools;
   - soft or leadership items listed as "skills" ("Leadership", "Communication", "Mentoring"). Leadership is shown in experience bullets with numbers, not claimed in a list.
5. **Junk above the name.** "Updated <date>", "CV", "Resume", page headers: cut them (an ATS reads them first).

## B. Experience: structure

6. **[R] One consistent role header for every role:** Company — Title — Location — Start - End, the same order and date format every time. Flag roles that mix formats or bury the company/title in a sentence.
7. **Company context line:** one short line for employers a foreign recruiter may not know. It should state **scale or domain** ("the country's largest online grocery, 3M customers"), not marketing copy ("We revolutionise the future of commerce…"). Flag a role-level intro sentence that is really a duty ("Was responsible for building the billing service…", "Our client was…"). Turn it into a bullet with a result, or cut it.
8. **[R] 3–4 bullets per role is the target, including the current role** (5 at most for the current role if every bullet is strong). Flag:
   - a role with 5+ bullets, even the most recent one: say "cut to 3–4" and name which bullets to merge. Never call 6 bullets acceptable;
   - bullets that say the same thing → merge them (e.g. separate bullets for "ran hiring loop", "conducted ~40 interviews", "improved incident reviews" → one leadership bullet);
   - a long role with 1–2 thin bullets (reads as low output);
   - a multi-sentence story bullet → cut it to one or two lines: result, measure, how.
9. **[R] Condense or cut old and irrelevant roles.** Roles 10+ years back, short side gigs off the target path (e.g. a 6-month QA stint in a backend CV), early freelance or student projects, unrelated volunteering and hobby clubs. Keep at most a one-line entry when it explains a gap.
10. **Career progression is visible.** Titles should show growth. If the title stayed the same, show scope growth (team size, ownership, promotions). Flag unexplained title regressions.
11. **Overlapping roles** must be labelled (contract, part-time, side project) so the current employer is obvious.

## C. Experience: bullet quality (the core of the review)

12. **[R] Every bullet must answer "Result? Technologies?"**: *Accomplished X, measured by Y, by doing Z (with tech T).*
    - A bullet with no result is a duty, not an achievement ("Built authentication service", "Maintained and developed new features").
    - A bullet listing only tools is a stack dump ("Utilized a modern tech stack including MySQL, Redis, and Elasticsearch"; "Built REST API with Flask, SQLAlchemy, Postgres, Celery…").
    - A bullet with a result but no tech misses ATS keywords.
13. **[R] Technologies go inside the bullets,** not in a "Technologies used:" line under the role or in parentheses after the role title ("Senior Engineer | Acme (Python, Redis, AWS)"). This is still acceptable if the bullets also carry tech; flag it as a fix, not a disaster.
14. **[R] Strong bullets: recognise and protect them.** A bullet with a concrete before→after number, scale or money is strong. Mark it ✅ and do NOT tell the user to cut or rewrite it (at most tighten wording). Examples of strong: "throughput 2 → 150 rps by splitting the monolith with RabbitMQ", "dashboard load 12s → 3s", "test coverage 35% → 85%", "+35% weekly active teams in a quarter", "12% conversion lift from A/B tests", "migrated ~3,000 rps / ~200 services with zero downtime", "mentored two interns who were hired as juniors".
15. **[R] Vague quantifiers mean a number is missing.** Flag and ask for the figure: "significantly", "substantially", "drastically", "greatly", "most of", "improved performance", "improving user experience", "a higher number of", "numerous", "various", "multiple", "complex", "robust", "efficient", "high-quality".
16. **[R] Verbs: past-tense action verbs, even for the current role.** Flag:
    - "-ing" openers: Owning, Managing, Setting, Curating, Implementing, Communicating, Working with, Developing;
    - weak openers: "Responsible for", "Worked on/with", "Contributed to", "Participated in", "Helped", "Took initiative", "Utilized", "Leveraged", "Was responsible";
    - "Lead" used as past tense (should be "Led").
    Good openers: Built, Cut, Reduced, Led, Launched, Migrated, Designed, Shipped, Automated, Scaled, Introduced, Replaced.
17. **[R] Leadership claims need detail:** team size, what was led, and the outcome. "Led a team of N engineers…" → what did the team ship, what changed, how did people grow? Mentoring → name the outcome (intern hired as junior, X promoted).
18. **Banned and filler words:** passionate, leverage, results-driven, dynamic, synergy, multifaceted, drive results, hit the ground running, "significant improvement", "various stakeholders", "ensuring operational excellence", "elevate", "spearheaded" (overused), "cutting-edge", "world-class", "Proven track record".
19. **Bullets not all built the same way.** If every bullet is "Implemented X…" or every bullet has the same length and rhythm, it reads as generated. LLM screeners reward polished, readable text, so the human-skim risk and the AI-screen reward pull in opposite directions: aim for polished but specific, never generic (section I).
20. **Interview backtrack test.** Could the candidate explain this line in an interview without saying "well, what I actually meant was…"? Flag overclaims: "Played a key role in the company's success", "Led the platform rewrite" when the role was a member, suspiciously round numbers, "~" on every number. Do not apply this to bullets you marked ✅ strong (rule 14) unless the claim is clearly impossible.
21. **SWE evidence the best CVs show** (ask for it if absent and the role needs it):
    - Testing: framework + what it prevented ("Jest + Cypress, cut release regressions by X").
    - CI/CD: what got faster or safer (deploy time, rollback rate).
    - Data structures and algorithms used and why.
    - Databases and caching: migrations, query wins, scale.
    - Metrics and alarms: what is monitored and what action follows.
    - Cross-functional work: with PM/UX/QA/other teams, and the business outcome.

## D. Education, certifications, extras

22. **Education stays brief for experienced engineers:** degree (official name), institution, location, years. GPA only if strong and early-career. An in-progress degree must say "in progress, expected <Month Year>"; a bare future date (e.g. "June 2025") reads oddly. The summary, the education entry and any availability line must give the same completion date.
23. **[R] Keep certifications recent and relevant.** Drop school olympiads, certs older than ~8 years, and beginner course certificates (Udemy) unless directly relevant. Every certification needs a year. Elite items (top competition results, selective programs) can stay as one line.
24. **Cut or justify extras:** interests, hobby clubs, long language lists with proficiency levels, unbacked lists of domains or clients. Always give both options: cut it, or keep it only if shown through a concrete example (a competitive programming rank, an open-source project link, a number of students taught).
25. **Projects** need a result too (users, stars, outcome), not a one-line description.

## E. Format and length

26. **[R] Simple, consistent formatting.** Black and white, one font, clear section headings, real bullet markers. Flag:
    - **italics** (the recruiter explicitly does not recommend italics; flag italic titles, dates and degree lines);
    - centred section headings and text blocks without bullet markers (hard to scan);
    - colour accents, sidebars, icons, photos, skill bars, rating dots, tag "pills";
    - personal details: photo, date of birth or age, marital status, nationality. Recommend removing them; never recommend adding them.
27. **[R] Single column.** Two-column layouts break ATS reading order and are harder to skim.
28. **[R] Length.** About 1 page per 10 years of experience, max 2 pages. A CV that spills a few lines onto page 2 or ends half-empty should be tightened. **Always state an explicit length target** ("cut to 1 page" / "keep 2 pages, but fill page 2 or cut it"), and put it in the fix list.
28a. **[R] Layout verdict.** If the CV breaks 2+ formatting rules (columns, colour, centred blocks, missing bullet markers, contacts or skills in the wrong place, no structure), give one explicit verdict: "Rebuild the layout: single column, contacts at top, then Summary → Skills → Experience → Education", as one row in the fix list. Don't scatter it across small items.
29. **File name:** `Firstname-Lastname-CV.pdf` or `Firstname-Lastname-Senior-Backend-Engineer.pdf`, not `cv (2) (1).pdf` or `resume_final_v3.pdf`.
30. **Spelling and grammar:** typos, "Postgresql" vs "PostgreSQL" vs "Postgres" inconsistency, wrong capitalisation of tech names (Mysql, Mongo, ElasticSearch, kubernetes). US or UK spelling are both fine; flag only a mix of the two.
31. **Gaps and tenure:** unexplained gaps of 6+ months and several stints under ~1 year should be explained briefly (in the cover letter, or as a one-word label: "contract", "company closed").

## F. ATS parsing checks (run on extracted text)

Always extract text: `pdftotext -layout -enc UTF-8 cv.pdf -` (and without `-layout` for reading order). Then check:

32. **Lost ligatures.** Apple Pages and some fonts drop "fi/fl/ff/ffi": "financial" → "nancial", "first" → "rst", "fixed" → "xed", "efficient" → "e cient", "profile" → "pro le", "diffs" → "di s", "configs" → "con gs". Those words become unsearchable. Fix: re-export the PDF (Print → Save as PDF from Word or Google Docs, or LaTeX) and re-check.
33. **Garbled text:** `(cid:123)`, `�`, broken accented letters.
34. **Reading order:** two columns or sidebars come out interleaved (lines of the left and right column on the same text line).
35. **Dates:** each role and degree needs a start and an end with a plain ASCII hyphen: `Mar 2021 - Nov 2022`. Flag en/em dashes in ranges (`Apr. 2023 – present`, `2020—PRESENT`), bare single years (`2016`), year-only ranges for recent roles (`2020-2022` hides months), and inconsistent formats (`06/2023` vs `Aug. 2018` vs `July.`).
36. **Contacts survive as plain text:** email and phone visible in the text layer and not only in a header/footer or icon.
37. **Symbols:** `∼`, `#`, `◦` and icon glyphs appear as junk characters. Plain `~` or none is safer.
38. **Referees:** "Available on request" unless the ad asks for them.

## G. Grounding (applies to every suggestion)

39. Only suggest adding what the CV, LinkedIn or the user's stated facts show. Never invent numbers, skills, titles or scope. If a fix needs a fact, **ask for it** in "Questions for you".
39a. **Describe the CV exactly.** When you mention technologies, counts or years "on the CV", use only strings that appear in the text. No "X-style", "e.g. Kafka", or guesses about tools they "probably" used. Compute years of experience from the earliest to latest professional dates and say how you counted. Count list items (languages, bullets) from the text, not from memory.
40. Diagnose, don't rewrite. You may show a *pattern* ("Reduced <metric> from A to B by <how> using <tech>") but not a finished bullet with invented numbers.
41. Quote the exact CV text whenever you point to a problem.

## H. Brainstorming questions (to extract missing numbers)

Use these to build "Questions for you":
- What changed because of this work: latency, throughput, cost, revenue, conversion, incidents, time saved?
- How many users, requests/sec, records, services, teams or engineers did it touch?
- What was the before → after?
- Which tech did you use for it, specifically?
- Testing: which framework, coverage before → after, what failures did it prevent?
- CI/CD: deploy time or frequency before → after, fewer rollbacks?
- Leadership: team size, who you hired or mentored and what happened to them, what process changed and what it fixed?
- Was this solo or team work, and what part was yours?
- For a long role with 1–2 bullets: what else did that period contain (secondary projects, internal tooling, distinct phases)?

## I. LLM screeners (AI match ranking)

Many ATS now rank candidates with an LLM. An audit of 9 LLM screeners (Pagan et al., arXiv 2610.41866, 2026) found that screeners' CV-only rankings agreed with plain CV↔JD semantic similarity for 86–94% of candidates, that a bare CV with no framing scored low (~4/10 even for strong fits), and that readable, precise, varied, non-gushing text was rewarded. The style findings were measured on cover letters, so treat them as tie-breakers for the CV, not as the main fix.

42. **Semantic mirroring.** The headline, summary and the top 2–3 bullets of recent roles should describe the work in the target JD's own language: its duties and domain, not just its skill nouns. Only rephrase true experience (rules 20, 39); never borrow a duty the candidate didn't do.
43. **The summary is the persuasive frame.** An LLM screener reading a bare list of roles scores it low. The summary (rule 3) is the one place to say "this is a <target title> who did <closest proof>", so it is the main lever for the AI ranking.
44. **Readable but precise.** One idea per bullet, exact technical terms. Flag bullets over ~30 words that chain clauses with commas; split or cut them.
45. **Vocabulary variety and tone.** The same verb or adjective repeated across many bullets lowers variety (see rule 19). Keep the tone confident and composed; gushing words ("passionate", "thrilled") are filler (rule 18).
46. **Writing tool.** If the candidate drafts or rephrases with AI, use a current frontier hosted model, not a small local model (every screener in the same audit ranked small-model text lowest), then edit for rules 19 and 20. Never let the tool invent facts.

## J. Work rights (JD knockouts)

47. **Read work-rights wording exactly.**
    - "Citizen or permanent resident" / "full working rights": a permanent resident passes. "Citizens only": a permanent resident fails.
    - Security clearances (government, defence) usually require citizenship; waivers are rare. Treat a non-citizen as a likely fail.
    - "Visa sponsorship not available" with a candidate who needs sponsorship is a knockout; say so prominently.
    - An ad that says nothing about work rights is not permission: say the user should check the employer's careers or FAQ page.
    - A company-wide "international applicants welcome" doesn't cover a specific program or stream unless that program is listed.
    - Never suggest misrepresenting citizenship, visa status or clearance.
