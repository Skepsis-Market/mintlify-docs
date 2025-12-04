---
title: "Understanding Ranges"
---

# Understanding Ranges

The key to successful Skepsis trading is understanding how range selection affects your odds and risk.

---

## What is a Range?

A range is a span of values where you believe the outcome will land.

**Example:** In a BTC price market with range $90,000 - $110,000:
- You select: **$96,000 - $98,000**
- This means: "I believe BTC will be somewhere between $96K and $98K at resolution"

---

## How Ranges Work

### Buckets

Every market is divided into discrete **buckets** (also called "spreads").

```
Market: BTC Price ($90K - $110K)
Buckets: 200 (each bucket = $100 width)

Bucket 60: $96,000 - $96,100
Bucket 61: $96,100 - $96,200
Bucket 62: $96,200 - $96,300
... and so on
```

When you select a range, you're actually selecting **multiple adjacent buckets**.

### Your Range = Sum of Buckets

```
Your range: $96,000 - $98,000
= Buckets 60, 61, 62, ... 79 (20 buckets)
= Probability of any single bucket hitting
```

---

## Range Width vs Odds Trade-off

This is the most important concept in Skepsis trading.

### The Rule

| Range Width | Win Probability | Odds | Risk Level |
|-------------|-----------------|------|------------|
| Narrow | Low | High | 🔴 High |
| Medium | Medium | Medium | 🟡 Medium |
| Wide | High | Low | 🟢 Low |

### Visual Example

BTC market, current price $97,000:

```
Narrow range ($500):  $96,750 - $97,250
Win prob: ~12%  |  Odds: 8x  |  Risk: 🔴

████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░

Medium range ($2,000): $96,000 - $98,000  
Win prob: ~45%  |  Odds: 2.2x  |  Risk: 🟡

░░░░░░██████████████████░░░░░░░░░░░░░░░░

Wide range ($5,000):   $95,000 - $100,000
Win prob: ~78%  |  Odds: 1.3x  |  Risk: 🟢

░░░░████████████████████████████░░░░░░░░
```

---

## Strategic Range Selection

### Strategy 1: The Sniper 🎯

**Approach:** Very narrow range, high conviction

**When to use:**
- You have strong edge (insider info, expert analysis)
- You can afford to lose
- High confidence in precise outcome

**Example:**
```
BTC at $97,000, big news coming
You know the exact impact: +$500
Range: $97,400 - $97,600 (just $200 wide)
Odds: 15x
Risk: Very high, but you have edge
```

### Strategy 2: The Zone Player 🎲

**Approach:** Medium range, balanced risk/reward

**When to use:**
- General directional view
- Want reasonable odds without extreme risk
- Most common strategy

**Example:**
```
BTC at $97,000, you think it stays stable
Range: $96,500 - $98,000 ($1,500 wide)
Odds: 3x
Risk: Medium, decent probability
```

### Strategy 3: The Safe Player 🛡️

**Approach:** Wide range, high probability

**When to use:**
- Very risk-averse
- Building a bankroll slowly
- Testing the platform

**Example:**
```
BTC at $97,000
Range: $94,000 - $100,000 ($6,000 wide)
Odds: 1.4x
Risk: Low, very likely to win
```

---

## Range Positioning

Where you place your range matters as much as how wide it is.

### Centering on Current Price

```
Current BTC: $97,000

Centered range: $96,000 - $98,000
= Betting on "no big move"

Off-center (bullish): $97,500 - $99,500  
= Betting on "modest up move"

Off-center (bearish): $94,500 - $96,500
= Betting on "modest down move"
```

### Tail Betting

Betting on unlikely but high-payout outcomes:

```
Current BTC: $97,000

Left tail: $90,000 - $93,000
= "Crash bet" → 20x odds, ~5% probability

Right tail: $102,000 - $105,000  
= "Moon bet" → 25x odds, ~4% probability
```

<Info>
**Tail bets** are high-risk, high-reward. They're like buying lottery tickets—fun money only!
</Note>

---

## Multi-Range Strategy (Hedging)

You can place multiple bets on different ranges.

### Example: Barbell Strategy

```
Total budget: $100

Bet 1: $70 on $96,000 - $98,000 (2.5x odds)
Bet 2: $15 on $98,000 - $100,000 (5x odds)
Bet 3: $15 on $94,000 - $96,000 (5x odds)

Outcomes:
- If $96K-$98K hits: Win $175 (net +$75)
- If $98K-$100K hits: Win $75 (net -$25)
- If $94K-$96K hits: Win $75 (net -$25)
- If outside all: Lose $100
```

This creates **asymmetric payoffs** where your most likely outcome pays the most.

---

## Common Mistakes

### ❌ Range Too Narrow

**Problem:** "I'll bet on exactly $97,000 - $97,100"

**Reality:** Unless you have incredible edge, a $100 range is almost never worth it. The odds might be 50x, but the probability is ~2%.

**Fix:** Widen to at least $500-$1,000 for short-term markets.

---

### ❌ Ignoring the Distribution

**Problem:** Selecting a range without looking at current probabilities.

**Reality:** A range with 3% market probability might be there for a reason—or it might be a golden opportunity.

**Fix:** Always check the distribution chart. Ask: "Why is this range priced this way?"

---

### ❌ Chasing High Odds

**Problem:** "25x odds! I'll be rich!"

**Reality:** 25x odds = ~4% probability. You'll likely lose 24 out of 25 times.

**Fix:** Calculate expected value, not just potential payout.

---

### ❌ Over-Hedging

**Problem:** Betting on too many ranges to "cover everything."

**Reality:** Overlapping bets can guarantee losses.

**Fix:** Use hedging strategically, not defensively.

---

## Quick Reference: Range Selection Cheat Sheet

| Your Confidence | Recommended Width | Expected Odds |
|-----------------|-------------------|---------------|
| "I'm certain" | 2-3 buckets | 10-15x |
| "Pretty sure" | 5-10 buckets | 4-8x |
| "I have a view" | 15-25 buckets | 2-4x |
| "Just playing" | 30+ buckets | 1.5-2x |

---

## Next Steps

<table data-card-size="large" data-view="cards">
<thead><tr><th></th><th></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead>
<tbody>
<tr><td><strong>Reading Odds</strong></td><td>How odds are calculated from probabilities</td><td><a href="reading-odds.md">reading-odds.md</a></td></tr>
<tr><td><strong>Strategies</strong></td><td>Advanced betting strategies</td><td><a href="strategies.md">strategies.md</a></td></tr>
</tbody>
</table>
