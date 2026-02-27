# vibe-coding-w3 — Legacy System Refactoring
## NEOLAF Vibe Coding Bootcamp | Week 3: The Craft

> **Every production system is a legacy system.** The question is not whether you will encounter legacy code — it is whether you have the judgment to improve it without breaking it. This week, you will develop that judgment.

[![NEOLAF](https://img.shields.io/badge/NEOLAF-Vibe%20Coding%20Bootcamp-blue)](https://neolaf.com)
[![Week](https://img.shields.io/badge/Week-3%20of%205-green)](https://github.com/neolaf2/vibe-coding-w3)
[![Security](https://img.shields.io/badge/Security-Intentionally%20Vulnerable-red)](https://github.com/neolaf2/vibe-coding-w3)
[![License](https://img.shields.io/badge/License-MIT-yellow)](LICENSE)

---

## ⚠️ Security Warning

**This repository contains intentionally vulnerable code for educational purposes.**

Do NOT deploy this application to a public server without completing the security refactoring in Week 3. The vulnerabilities are intentional and serve as the learning material for Day 2.

---

## What You Will Do

You will **analyze, refactor, and document a legacy Python web application** — directing AI agents to find vulnerabilities, fix them, design skills, integrate APIs, and generate comprehensive tests and documentation.

**The challenge:** The application works. But it has security vulnerabilities, performance issues, architectural anti-patterns, and zero tests. Your job is to make it production-ready without breaking it.

---

## Week 3 Daily Modules

| Day | Title | Concept | Artifact |
|-----|-------|---------|----------|
| Day 1 | System Analysis | Semantic debugging, architecture reading | System analysis report + vulnerability inventory |
| Day 2 | Security Refactoring | OWASP Top 10, authorization governance | Security-fixed codebase + OWASP checklist |
| Day 3 | Skill Design | Skills as first-class units, skill graphs | Three installed skills + composition diagram |
| Day 4 | API Integration | MCP protocol, multi-step API workflows | Integration layer + three API connections |
| Day 5 | Testing and Documentation | Tests as intent documentation | Test suite >80% coverage + full documentation |

---

## The Legacy Application

The `app/` directory contains a Flask web application with the following intentional issues:

### Known Issues (Your Learning Material)

**Security Vulnerabilities (OWASP Top 10):**
- SQL injection in the search endpoint
- Hardcoded credentials in configuration
- Missing CSRF protection on forms
- Insecure direct object references
- No rate limiting on authentication endpoints

**Performance Issues:**
- N+1 query pattern in the posts listing
- Missing database indexes
- Synchronous operations that should be async
- No caching layer

**Architectural Anti-Patterns:**
- Business logic mixed with presentation layer
- No separation of concerns
- Global state management
- Missing error handling

**Technical Debt:**
- Zero test coverage
- No documentation
- Inconsistent naming conventions
- Dead code throughout

---

## Getting Started

### Step 1: Fork and Set Up

```
Direct your AI agent:
"I've forked vibe-coding-w3 from https://github.com/neolaf2/vibe-coding-w3
Please help me:
1. Clone the repository
2. Set up a Python virtual environment
3. Install the dependencies from requirements.txt
4. Run the application locally
5. Explain what the application does"
```

### Step 2: System Analysis (Day 1)

```
Direct your AI agent:
"Please analyze this Flask application for:
1. Security vulnerabilities (check against OWASP Top 10)
2. Performance bottlenecks
3. Architectural anti-patterns
4. Technical debt

For each issue found, provide:
- Severity rating (Critical/High/Medium/Low)
- Description of the vulnerability or issue
- Recommended fix
- Estimated effort to fix

Format the output as a structured report."
```

---

## Repository Structure

```
vibe-coding-w3/
├── README.md
├── app/
│   ├── app.py                   # Main Flask application (intentionally flawed)
│   ├── models.py                # Database models
│   ├── routes/                  # Route handlers
│   ├── templates/               # HTML templates
│   └── static/                  # Static assets
├── requirements.txt             # Python dependencies
├── tests/                       # Test directory (empty — you fill it)
├── docs/
│   ├── analysis/                # System analysis reports
│   ├── aar/                     # After-Action Reviews
│   └── architecture/            # Architecture diagrams
├── skills/                      # Custom skills you design (Day 3)
└── .github/
    ├── workflows/
    │   └── ci.yml
    └── PULL_REQUEST_TEMPLATE.md
```

---

## AI Tools for This Week

| Tool | Purpose |
|------|---------|
| **Cursor IDE** | Primary development environment |
| **Snyk** | Security vulnerability scanning |
| **Sourcegraph Cody** | Codebase understanding |
| **OWASP ZAP** | Web application security testing |
| **pytest** | Test generation and execution |

---

## External Courseware

1. [OWASP: Top 10 Web Application Security Risks](https://owasp.org/Top10/) — 2 hours
2. [Snyk: Introduction to Application Security](https://learn.snyk.io/) — 1 hour
3. [Cloudflare Agents SDK: Skills Documentation](https://developers.cloudflare.com/agents/) — 1 hour
4. [MCP Protocol: Introduction](https://modelcontextprotocol.io/introduction) — 30 minutes
5. [Google: Software Engineering at Google — Testing](https://abseil.io/resources/swe-book/html/ch11.html) — 1 hour

---

## Evaluation

Your Week 3 submission must include:

- [ ] System analysis report with severity ratings
- [ ] All critical and high vulnerabilities fixed
- [ ] OWASP compliance checklist completed
- [ ] Three skills designed and installed
- [ ] Integration layer connecting three APIs
- [ ] Test suite with >80% coverage
- [ ] Architecture documentation with diagrams
- [ ] All work committed with conventional messages

**Bonus:** Submit a PR to `neolaf2/vibe-coding-w3` with an improvement to the legacy application.

---

*Built with NEOLAF Vibe Coding Bootcamp | [neolaf.com](https://neolaf.com)*
