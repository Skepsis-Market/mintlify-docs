---
title: "Continuous vs Binary Markets"
---


Why predicting distributions beats predicting yes/no.

---

## The Difference

Binary markets ask threshold questions: "Will BTC be above $100K on Dec 31?" You get Yes or No.

Continuous markets ask open questions: "What will BTC's price be on Dec 31?" You bet on a range within the market bounds. $1 per share if the outcome lands in your range.

A binary market at 45% "Yes" tells you one number. A continuous distribution tells you expected value, confidence (narrow vs wide distribution), skew, tail risk, and where the mode differs from the mean.

---

## The Distribution

```
Question: "Where will BTC be on Dec 31?"

$80K-$85K:   3%  ██
$85K-$90K:   8%  ████
$90K-$95K:   15% ████████
$95K-$100K:  22% ████████████
$100K-$105K: 25% ██████████████  ← Mode
$105K-$110K: 15% ████████
$110K-$120K: 9%  █████
$120K+:      3%  ██
```

---

## Where Binary Markets Break Down

### The "Almost Right" Problem

Binary market: "Will BTC hit $100K?" BTC lands at $99,999 — you lose. BTC lands at $100,001 — you win. Your thesis was correct both times.

Continuous market: you bet $98K-$102K. Both outcomes are wins.

### The Precision Penalty

"Will GPT-5 launch before June 1?" You think "probably April-August." Binary forces you to pick a cutoff. GPT-5 launches June 15 — you were right about the timeframe but the binary says you're wrong.

Continuous market: bet the April-August range. June 15 launch = win.

### Missing Nuance

"Will it rain tomorrow?" treats a drizzle and a monsoon identically. A continuous rainfall market lets you express "probably light rain" by betting the 0.1-0.5 inch range.

---

## Capital Efficiency

To express "BTC will be between $95K-$105K" in binary markets, you need two positions across two markets (buy "BTC > $95K" Yes, buy "BTC > $105K" No) — two transactions, two fee payments, two positions to manage.

Continuous market: one range bet, one transaction, one fee.

---

## Price Discovery

Binary markets can't distinguish between a trader who thinks BTC will be $102K and one who thinks $150K — both buy "Yes" on a $100K threshold. Continuous markets separate these views into distinct ranges with distinct odds, producing far richer information.

---

## When Binary Still Works

Binary markets are fine when the question is naturally binary (election wins, company bankruptcy, law passage), when the threshold itself is meaningful (inflation above 3%), or when magnitude doesn't matter (making the playoffs).

---

## Derived Binary Markets

From a single continuous market, you can derive any binary question by summing probabilities above or below a threshold. One continuous market = infinite binary markets.

```
Continuous: "Where will BTC be Dec 31?"

"BTC > $100K?" → Sum of probability above $100K
"BTC > $90K?"  → Sum of probability above $90K
"BTC $95K-$105K?" → Sum of that range
```
