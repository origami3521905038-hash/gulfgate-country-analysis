# GulfGate Country Analysis Skill

[简体中文](README.md) · [English](README.en.md) · [العربية](README.ar.md)

<div align="center">
  <img src="docs/images/hero-analysis.png" alt="GulfGate Country Analysis Skill hero" width="100%">
</div>

> Turn fragmented information about the six GCC markets into a decision brief that a team can discuss, assign, and stop when the evidence does not support further spending.

[![Agent Skill](https://img.shields.io/badge/Agent%20Skill-compatible-1f6f50)](SKILL.md)
[![Markets](https://img.shields.io/badge/GCC%20markets-6-c18b49)](#coverage)
[![Python](https://img.shields.io/badge/Python-3%20standard%20library-3776ab)](#install)
[![Validation](https://img.shields.io/badge/tests-passing-2f7d55)](tests/validate_package.py)

This is not a generic “Middle East market report” prompt. It separates country, jurisdiction, product use, transaction role, evidence status, and execution stage, then answers four management questions:

1. Should we proceed?
2. What should happen first?
3. What must be true before we increase investment?
4. What signal should make us pause, change course, or exit?

## Why it exists

Most international expansion mistakes are not caused by a lack of information. They come from collapsing different evidence layers into one conclusion:

- a large market is treated as accessible revenue;
- a friendly partner is treated as a capable partner;
- a product certificate is treated as project and use-case approval;
- a live website is treated as a currently valid rule;
- two meetings are treated as permission to quote, sign, or hold inventory.

GulfGate forces every recommendation back to evidence, a calculation, or an explicit planning assumption.

## Demo

<div align="center">
  <img src="docs/images/demo-analysis.png" alt="Country analysis demo output" width="100%">
</div>

Example request:

```text
Use $gulfgate-country-analysis.
We are a mid-sized commercial energy-storage company planning to enter the UAE
through a local distributor, with no local entity yet. Initial targets are
industrial parks and commercial buildings. Decide whether to proceed and create
a 90-day validation plan.
```

See the full public-safe example in [examples/analysis-demo.md](examples/analysis-demo.md).

## Three operating modes

| Mode | Use it when | Typical output |
| --- | --- | --- |
| Research | Exploring an opportunity, comparing markets, or planning entry | Market hypothesis, buyer chain, path comparison, validation plan |
| Diagnosis | You already have a proposal and need an evidence audit | Failure points, evidence gaps, repair order, conditions for reconsideration |
| Precheck | Before bidding, signing, incorporating, or committing major resources | Proceed/pause conditions, stage gates, stop conditions |

Complex tasks produce one self-contained Markdown deliverable. Tables, diagrams, and source notes stay inside the same file.

## Install

```bash
git clone https://github.com/origami3521905038-hash/gulfgate-country-analysis.git
mkdir -p ~/.codex/skills
cp -R gulfgate-country-analysis ~/.codex/skills/
```

Copy the complete directory. `references/`, `assets/`, and `scripts/` are required runtime resources.

Run the offline package check:

```bash
cd gulfgate-country-analysis
python tests/validate_package.py
```

## Coverage

- Markets: Saudi Arabia, United Arab Emirates, Qatar, Kuwait, Bahrain, and Oman
- Industry entry points: renewable energy, construction materials and contracting, cross-border e-commerce and consumer electronics, medical devices, and light industrial products
- Business chain: market opportunity, commercial ecosystem, partner diligence, cross-cultural engagement, access and tendering, contracts and collection, delivery and local operations, compliance and crisis management
- Assets: 565 structured records, 1,549 business terms, country and industry knowledge files, and eight method files

## Test evidence

<div align="center">
  <img src="docs/images/test-analysis.png" alt="Country analysis validation results" width="100%">
</div>

The release check validates frontmatter, local links, knowledge paths, JSONL parsing, and the local lookup smoke test. GitHub Actions runs the same check on every push and pull request.

Passing tests prove that the package is readable and operational. They do not prove that every regulatory, tax, or certification conclusion is current.

## Fact boundary

This Skill is a research workflow and historical retrieval aid. It does not replace legal, tax, medical, engineering, or regulator advice. High-impact and time-sensitive facts require live source verification with publication date, scope, and verification date.

The Skill includes no search entitlement, API key, or backend service. When the host cannot access the web, the correct output is an explicit “unverified” status plus a verification plan.

## Companion project

The onboarding and judgment-training Skill lives in a separate repository: [GulfGate Country Training](https://github.com/origami3521905038-hash/gulfgate-country-training).

## Co-creators

This project was jointly created by [@origami3521905038-hash](https://github.com/origami3521905038-hash) and [@18719203981lkr-spec](https://github.com/18719203981lkr-spec).

Contributions are welcome through issues and pull requests. See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

No open-source license is attached yet. Copyright remains with the co-creators. Written permission is required before public reuse, commercial use, or redistribution.

