# Bug & Issue Tracking — Complete Study Notes
Assisted by: Perplexity AI

---

## Table of Contents

1. Introduction
2. What is a Bug?
3. What is an Issue?
4. Bug vs Issue vs Defect vs Error vs Failure
5. Why Bug Tracking is Important
6. Bug Life Cycle
7. Issue Life Cycle
8. Components of a Bug Report
9. Bug Severity
10. Bug Priority
11. Severity vs Priority
12. Types of Bugs
13. Root Cause Analysis
14. Bug Reproduction
15. Bug Triage
16. Issue Management
17. Agile Bug Tracking
18. DevOps & CI/CD Integration
19. Issue Tracking Workflow
20. Labels, Components & Milestones
21. Common Metrics
22. Reporting & Dashboards
23. Popular Bug Tracking Tools
24. GitHub Issue Tracking
25. Jira Issue Tracking
26. Azure DevOps
27. GitLab Issues
28. Bug Tracking Best Practices
29. Common Mistakes
30. Real-world Example
31. Interview Questions
32. Summary

---

## 1. Introduction

Software development is impossible without bugs.

Even companies like Google, Microsoft, Amazon, Netflix, Meta, and Apple ship software that contains bugs. The goal is not **bug-free software**. The goal is to detect bugs quickly, prioritize them correctly, fix them efficiently, and prevent them from happening again.

This is achieved through **Bug Tracking Systems (BTS)** and **Issue Tracking Systems (ITS)**.

---

## 2. What is a Bug?

A **bug** is an unintended problem in software that causes incorrect or unexpected behavior.

### Definition

> A bug is a flaw in software that produces incorrect results or prevents the software from functioning as intended.

### Examples

**Example 1**
- Login button does nothing.
- Expected: user logs in.
- Actual: nothing happens.

**Example 2**
- Shopping cart total should be ₹450 after discount.
- Actual: it shows ₹550.

**Example 3**
- Application crashes after clicking **Save**.

---

## 3. What is an Issue?

An **issue** is any piece of work that needs attention.

An issue may or may not be a bug.

Examples:
- Bug
- Feature request
- Documentation task
- Improvement
- Security vulnerability
- Performance optimization
- Technical debt
- Refactoring

---

## 4. Bug vs Issue vs Defect vs Error vs Failure

| Term | Meaning |
|------|---------|
| Error | Human mistake while coding |
| Defect | Incorrect code introduced |
| Bug | Informal name for a defect |
| Failure | Software behaves incorrectly |
| Issue | Any task requiring action |

### Example flow

Developer writes `if(age > 18)` instead of `if(age >= 18)`.

- Human mistake → **Error**
- Wrong code → **Defect**
- Informal label → **Bug**
- Program rejects 18-year-old users → **Failure**

---

## 5. Why Bug Tracking is Important

Without bug tracking:
- Bugs get forgotten.
- Duplicate work happens.
- Teams become confused.
- Releases become unstable.

With bug tracking:
- Accountability
- Transparency
- Prioritization
- History
- Analytics
- Better collaboration

---

## 6. Bug Life Cycle

```text
New
↓
Assigned
↓
Open
↓
In Progress
↓
Fixed
↓
Testing
↓
Verified
↓
Closed
```

### Alternate states
- Rejected
- Duplicate
- Cannot Reproduce
- Deferred
- Reopened

### State meanings
- **New:** Bug reported.
- **Assigned:** Assigned to a developer.
- **Open:** Developer accepts the bug.
- **In Progress:** Developer starts fixing it.
- **Fixed:** Developer believes the bug is fixed.
- **Testing:** QA verifies the fix.
- **Verified:** QA confirms the fix works.
- **Closed:** Issue is resolved.
- **Reopened:** Bug still exists.
- **Duplicate:** Already reported.
- **Rejected:** Not actually a bug.
- **Deferred:** Will be fixed later.
- **Cannot Reproduce:** QA cannot reproduce the issue.

---

## 7. Issue Life Cycle

Unlike bugs, issues may represent features or other work items.

```text
Backlog
↓
Selected
↓
In Progress
↓
Review
↓
Testing
↓
Done
```

---

## 8. Components of a Bug Report

A professional bug report contains:

### Title
A short summary of the issue.

**Example:** `Login button unresponsive on Chrome`

### Description
Explain the problem clearly and briefly.

### Environment
Example:
- Windows 11
- Chrome 138
- Version 3.2.1
- Production

### Steps to Reproduce
1. Open the login page.
2. Enter credentials.
3. Click **Login**.

### Expected Result
User logs in successfully.

### Actual Result
Nothing happens.

### Additional Details
- Screenshots
- Logs
- Stack trace
- Crash dump
- Network logs
- HAR file

---

## 9. Bug Severity

Severity indicates the **impact** of the bug.

### Severity levels
- **Critical:** System unusable. Example: database corruption.
- **High:** Major functionality broken. Example: cannot log in.
- **Medium:** Feature partially broken. Example: search gives incorrect results.
- **Low:** Minor inconvenience. Example: typo.
- **Cosmetic:** UI issue. Example: wrong color.

---

## 10. Bug Priority

Priority determines the **fix order**.

### Priority levels
- **P0:** Immediate
- **P1:** High
- **P2:** Medium
- **P3:** Low

Priority is usually based on business need, user impact, deadlines, or visibility.

---

## 11. Severity vs Priority

| Aspect | Severity | Priority |
|--------|----------|----------|
| Meaning | Technical impact | Business urgency |
| Decided by | QA | Product owner / team |

### Example
A typo on the homepage may have **low severity** but **high priority** because the homepage is seen by many users.

---

## 12. Types of Bugs

- **Functional:** Feature does not work.
- **UI Bug:** Layout or styling broken.
- **Performance Bug:** Slow loading or response.
- **Security Bug:** SQL injection, XSS, CSRF, auth bypass.
- **Compatibility Bug:** Works in Chrome but fails in Firefox.
- **Regression Bug:** Previously working feature breaks.
- **Logic Bug:** Incorrect algorithm or condition.
- **Crash Bug:** App terminates unexpectedly.
- **Data Bug:** Wrong calculations or stored values.
- **Memory Leak:** RAM usage keeps increasing.
- **Concurrency Bug:** Race condition or deadlock.
- **Configuration Bug:** Wrong environment variables or settings.

---

## 13. Root Cause Analysis

Instead of only fixing the bug, teams should find **why** it happened.

### Common RCA methods
- **Five Whys:** Ask “Why?” repeatedly until the root cause is found.
- **Fishbone Diagram:** Group causes by people, process, tools, environment, and code.
- **Pareto Analysis:** Often, a small number of modules cause most bugs.

---

## 14. Bug Reproduction

Developers need to reproduce bugs before fixing them.

### Good reproduction steps are:
- Clear
- Numbered
- Repeatable

### Example
1. Log in.
2. Open profile page.
3. Upload PNG.
4. Click Save.

Result: Crash occurs.

---

## 15. Bug Triage

Bug triage is the process of deciding:
- Is it real?
- How severe is it?
- Who should fix it?
- Which release should include it?

### Participants
- QA
- Product Owner
- Developers
- Scrum Master

---

## 16. Issue Management

Issue tracking usually includes:
- Creating issues
- Assigning owners
- Adding labels
- Commenting
- Attaching files
- Setting deadlines
- Updating status
- Closing issues

---

## 17. Agile Bug Tracking

In Agile teams, bugs can be:
- Fixed immediately
- Added to the backlog
- Scheduled for the next sprint

### Typical flow
```text
Product Backlog
↓
Sprint Backlog
↓
Development
↓
Testing
↓
Done
```

---

## 18. DevOps & CI/CD Integration

Modern issue trackers often connect with:
- Git
- CI/CD
- Testing
- Deployment
- Monitoring

### Example workflow
```text
Git Commit
↓
Pull Request
↓
GitHub Actions
↓
Tests
↓
Deployment
↓
Issue Automatically Closed
```

---

## 19. Issue Tracking Workflow

```text
Issue Created
↓
Assigned
↓
Development
↓
Code Review
↓
Merged
↓
Testing
↓
Deployment
↓
Closed
```

---

## 20. Labels, Components & Milestones

### Labels
Examples:
- bug
- documentation
- backend
- frontend
- good first issue
- security
- enhancement
- urgent

### Components
Examples:
- Authentication
- Database
- API
- UI
- Payment

### Milestones
Examples:
- Version 1.0
- Sprint 8
- Release Candidate
- Hotfix

---

## 21. Common Metrics

### Important metrics
- **Open Bugs:** Current unresolved bugs.
- **Closed Bugs:** Resolved bugs.
- **Bug Density:** Bugs per 1000 lines of code.
- **MTTR:** Mean Time to Resolve.
- **Defect Leakage:** Bugs missed in testing and found in production.
- **Reopened Bugs:** Bugs that return after being marked fixed.
- **Bug Arrival Rate:** New bugs reported daily.
- **Resolution Rate:** Bugs fixed daily.

---

## 22. Reporting & Dashboards

Modern dashboards show:
- Open issues
- Closed issues
- Sprint progress
- Velocity
- Burndown charts
- Bug trends
- Team workload
- Release status

---

## 23. Popular Bug Tracking Tools

| Tool | Best For |
|------|----------|
| Jira | Enterprise Agile teams |
| GitHub Issues | Open source and GitHub projects |
| GitLab Issues | DevOps workflow |
| Azure DevOps | Microsoft ecosystem |
| Redmine | Open source |
| Bugzilla | Large bug databases |
| YouTrack | JetBrains users |
| Linear | Modern startups |
| Trello | Small teams |
| Asana | Project management |

---

## 24. GitHub Issue Tracking

GitHub Issues supports:
- Issues
- Labels
- Milestones
- Projects
- Discussions
- Pull Requests
- Auto closing

### Example
`Fixes #42`

When the pull request is merged, GitHub can automatically close Issue #42.

---

## 25. Jira Issue Tracking

### Common issue types
- Bug
- Story
- Epic
- Task
- Improvement
- Spike

### Typical workflow
```text
To Do
↓
In Progress
↓
Code Review
↓
Testing
↓
Done
```

Jira supports Scrum, Kanban, roadmaps, dashboards, and automation.

---

## 26. Azure DevOps

Azure DevOps supports:
- Boards
- Pipelines
- Repositories
- Test Plans
- Artifacts

It is especially useful in the Microsoft ecosystem.

---

## 27. GitLab Issues

GitLab Issues works well with:
- Git
- Merge Requests
- Pipelines
- Security
- Releases

It is a strong choice for DevOps-focused teams.

---

## 28. Bug Tracking Best Practices

- Write descriptive titles.
- Include screenshots.
- Provide logs.
- Mention environment details.
- Add reproduction steps.
- Assign ownership.
- Use labels.
- Keep status updated.
- Avoid duplicate issues.
- Verify before closing.

---

## 29. Common Mistakes

- Vague descriptions.
- Missing screenshots.
- No reproduction steps.
- Wrong severity.
- Wrong priority.
- Closing without testing.
- Ignoring regression testing.
- No root cause analysis.

---

## 30. Real-world Example

### Bug Report
**Title:** Checkout page crashes after applying coupon

**Severity:** High

**Priority:** P1

**Environment:** Chrome 138, Windows 11, Production

**Steps:**
1. Add item to cart.
2. Apply coupon.
3. Click Checkout.

**Expected:** Payment page opens.

**Actual:** Application crashes.

### Resolution
Developer finds a null pointer exception, adds validation for an empty coupon object, QA verifies the fix, and the bug is closed.

---

## 31. Interview Questions

### Beginner
- What is a bug?
- What is an issue?
- What is the difference between severity and priority?
- What is the bug life cycle?
- What is regression testing?
- What is bug triage?

### Intermediate
- How do you write a good bug report?
- What metrics measure software quality?
- Explain MTTR.
- Explain defect leakage.
- What is root cause analysis?

### Advanced
- How does Jira integrate with CI/CD?
- How do GitHub Actions automatically close issues?
- How do you manage bugs in Agile?
- How do you prioritize production bugs?
- Explain bug tracking in DevOps.

---

## 32. Summary

Bug and issue tracking are essential for building reliable software. A good tracking process improves collaboration, speeds up debugging, and makes project status visible. Teams should learn how to write strong bug reports, assign severity and priority correctly, use tools like Jira, GitHub Issues, Azure DevOps, and GitLab, and apply RCA and workflow integration to prevent repeated problems.

---

## Quick Revision Cheat Sheet

| Concept | Key Point |
|---------|-----------|
| Bug | Software behaves incorrectly |
| Issue | Any work item |
| Severity | Technical impact |
| Priority | Business urgency |
| RCA | Find the underlying cause |
| Bug Triage | Prioritize and assign bugs |
| Regression Bug | Old functionality breaks after changes |
| MTTR | Average bug resolution time |
| Defect Leakage | Bugs reaching production |
| BTS | Bug Tracking System |
| ITS | Issue Tracking System |
| Popular Tools | Jira, GitHub Issues, Azure DevOps, GitLab, Bugzilla, YouTrack, Linear |

---

## Suggested Learning Path

1. Learn software testing fundamentals.
2. Practice writing high-quality bug reports.
3. Use GitHub Issues in a personal project.
4. Learn Jira workflows.
5. Explore GitLab Issues and Azure DevOps Boards.
6. Understand Agile sprint planning and bug triage.
7. Integrate issue tracking with Git and CI/CD.
8. Learn software quality metrics and dashboards.
9. Study RCA techniques.
10. Apply bug tracking in real projects and open source.
