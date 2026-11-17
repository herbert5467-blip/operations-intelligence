# Operations Intelligence

> Analysis of technical support operations with SQL (BigQuery) and a dashboard.
> **Status:** in progress (week 1 of 6) · **Data:** 100% fictitious

## Problem

A technical support team handles thousands of tickets across equipment lines, categories and priorities. A supervisor needs to answer, every week:

- Which urgent tickets have been open the longest?
- Which equipment lines generate the most warranty tickets?
- How long does it take to close a ticket, by category?
- Are warranty issues factory defects, natural wear or operational errors?

This project answers those questions with SQL and turns them into a dashboard.

## Requirements

| # | Requirement | Status |
| --- | --- | --- |
| R1 | Fictitious dataset with the same structure as a real ticketing system | Done |
| R2 | 10 business questions answered with SQL, one file per question | In progress |
| R3 | Each query documented: question, logic, result, decision it supports | To do |
| R4 | Dashboard with backlog, volume by equipment, time to close and root cause | To do |
| R5 | Data quality checks (empty vs NULL, duplicates, invalid dates) | To do |

## Architecture

```mermaid
flowchart LR
    G[generate_tickets.py] --> C[tickets.csv]
    C --> BQ[(BigQuery sandbox)]
    BQ --> Q[sql/*.sql]
    Q --> D[Dashboard]
```

## Project structure

```
operations-intelligence/
├── data/          dataset generator and data dictionary
├── sql/           one query per business question
├── dashboard/     dashboard link and screenshots
├── docs/          architecture and decisions
└── tests/         data quality checks
```

## How to run

1. `python data/generate_tickets.py` creates `data/tickets.csv` (3,000 fictitious tickets).
2. Upload the CSV to a BigQuery sandbox (free, no credit card) as `<project>.ops.tickets`.
3. Run the queries in `sql/` in order.

## What I learned

_Filled in at the end of each week._

## Author

Herbert Marques · Technical Support Supervisor moving into Process Automation and Data · [LinkedIn](https://www.linkedin.com/in/herbert-m-0abb10112/)
