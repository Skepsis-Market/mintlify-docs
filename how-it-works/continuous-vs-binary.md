---
title: "Continuous vs Binary Markets"
---


A deep dive into why predicting distributions beats predicting yes/no.

---

## The Fundamental Difference

### Binary Markets
> "Will Bitcoin be above $100,000 on December 31?"
>
> **Options:** Yes or No
> **Payout:** Yes = $1, No = $1

### Continuous Markets (Skepsis)
> "What will Bitcoin's price be on December 31?"
>
> **Options:** Any range within the market bounds
> **Payout:** $1 per share if outcome lands in your range

---

## Visual Comparison

### Binary: One Data Point

```
Question: "BTC > $100K by Dec 31?"

Yes: 45% ████████████████████░░░░░░░░░░░░░░░░░░░░
No:  55% ████████████████████████████░░░░░░░░░░░░

Information: "Market thinks ~45% chance of crossing $100K"
Unknown: Will it be $100,001 or $500,000? Both are "Yes"
```

### Continuous: Full Distribution

```
Question: "Where will BTC be on Dec 31?"

$80K-$85K:   3%  ██
$85K-$90K:   8%  ████
$90K-$95K:   15% ████████
$95K-$100K:  22% ████████████
$100K-$105K: 25% ██████████████  ← Mode (most likely)
$105K-$110K: 15% ████████
$110K-$120K: 9%  █████
$120K+:      3%  ██

Information: Full probability landscape
- Expected value visible
- Uncertainty visible
- Tail risks visible
```

---

## Information Density

### What Binary Markets Tell You

A single binary market at 45% "Yes" tells you:
- There's a 45% chance of crossing the threshold
- That's it

### What Continuous Markets Tell You

A continuous distribution tells you:
- **Expected value:** Where the market thinks it'll land
- **Confidence:** Is the distribution narrow (confident) or wide (uncertain)?
- **Skew:** Is the market more bullish or bearish?
- **Tail risk:** What's the chance of extreme outcomes?
- **Mode vs Mean:** Most likely outcome vs average expected outcome

---

## Edge Cases: Where Binary Fails

### The "Almost Right" Problem

**Binary market:** "Will BTC hit $100K?"

| Scenario | BTC Price | Bet | Result |
|----------|-----------|-----|--------|
| A | $99,999 | Yes | ❌ LOSE |
| B | $100,001 | Yes | ✅ WIN |

You were right about BTC being "around $100K" in both cases. Binary punishes you in Scenario A.

**Continuous market:** "Where will BTC be?"

| Scenario | BTC Price | Range Bet | Result |
|----------|-----------|-----------|--------|
| A | $99,999 | $98K-$102K | ✅ WIN |
| B | $100,001 | $98K-$102K | ✅ WIN |

Your actual belief (around $100K) is captured and rewarded.

---

### The "Precision Penalty" Problem

**Binary framing forces false precision:**

```
"Will GPT-5 launch before June 1, 2025?"

You think: "Probably April-August 2025"
Binary forces: Pick June 1 as the cutoff

If GPT-5 launches June 15:
- You were basically right (summer 2025)
- Binary says: WRONG
```

**Continuous market:**

```
"When will GPT-5 launch?"

Your bet: April-August 2025 range
GPT-5 launches June 15
Result: ✅ WIN (exactly as you predicted)
```

---

### The "Missing Nuance" Problem

**Binary:** "Will it rain tomorrow?"

- Doesn't capture: How much rain?
- Drizzle and monsoon both = "Yes"
- No way to express "probably light rain"

**Continuous:** "How much rainfall tomorrow?"

- 0.0-0.1 inches: 30%
- 0.1-0.5 inches: 45% ← You bet here
- 0.5-1.0 inches: 20%
- 1.0+ inches: 5%

Your prediction matches your actual belief.

---

## Capital Efficiency

### Binary: Multiple Markets Needed

To express "BTC will be between $95K-$105K," you need:

```
Market 1: "BTC > $95K?" → Buy Yes
Market 2: "BTC > $105K?" → Buy No

Two transactions
Two sets of fees
Two positions to track
Capital spread across markets
```

### Continuous: One Market

```
Range: $95K-$105K
One transaction
One fee
One position
Capital concentrated
```

**Result:** Same belief, half the friction.

---

## Price Discovery

### Binary Markets: Threshold Games

In binary markets, traders fight over the threshold:

```
"BTC > $100K?"
Currently: 48% Yes

Trader A thinks BTC will be $102K → Buys Yes
Trader B thinks BTC will be $98K → Buys No
Trader C thinks BTC will be $150K → Buys Yes (same as A!)

The market can't distinguish A and C's very different views.
```

### Continuous Markets: Full Spectrum

```
"Where will BTC be?"

Trader A (thinks $102K) → Bets $100K-$105K
Trader B (thinks $98K) → Bets $95K-$100K  
Trader C (thinks $150K) → Bets $140K-$160K

Each view has its own odds
Market shows full range of beliefs
Much richer information
```

---

## When Binary Markets Work

Binary isn't always wrong. They work well when:

### 1. The Question is Naturally Binary
- "Will [candidate] win the election?" (1st or not 1st)
- "Will [company] go bankrupt?" (exists or doesn't)
- "Will [law] pass?" (passes or doesn't)

### 2. Threshold is Meaningful
- "Will inflation be above 3%?" (policy threshold)
- "Will [movie] make $100M opening?" (industry benchmark)

### 3. Extremes Don't Matter
- "Will [team] make playoffs?" (whether they dominate or barely qualify doesn't change the outcome)

---

## When Continuous Markets Excel

### 1. Magnitude Matters
- Price predictions (How high? How low?)
- Measurements (How much? How many?)
- Timing (When exactly?)

### 2. Uncertainty is Important
- Is the market confident or uncertain?
- What are the tail risks?
- What's the range of likely outcomes?

### 3. Nuance Adds Value
- Weather (temperatures, rainfall amounts)
- Economic indicators (inflation rate, unemployment)
- Performance metrics (revenue, users, etc.)

---

## The Hybrid Future

At Skepsis, we believe continuous markets can handle most prediction needs. But we're also exploring:

### Derived Binary Markets
From a continuous market, you can derive any binary question:

```
Continuous: "Where will BTC be Dec 31?"

Derived binaries (from same underlying):
- "BTC > $100K?" → Sum of probability above $100K
- "BTC > $90K?" → Sum of probability above $90K
- "BTC between $95K-$105K?" → Sum of that range
```

**One continuous market = infinite binary markets**

---

## Summary

| Aspect | Binary | Continuous |
|--------|--------|------------|
| Information | Single probability | Full distribution |
| Expressiveness | Threshold only | Any range |
| Edge cases | Punishes "almost right" | Rewards accuracy |
| Capital efficiency | Multiple markets | One market |
| Price discovery | Limited | Rich |
| Nuance | None | Preserved |
| Best for | Naturally binary events | Numerical outcomes |

---

## Try the Difference

Experience continuous markets yourself:

<Note>
**Make a continuous prediction:** [Launch Skepsis →](https://beta.skepsis.live/markets)
</Note>

---

## Next Steps

<table data-card-size="large" data-view="cards">
<thead><tr><th></th><th></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead>
<tbody>
<tr><td><strong>Economics</strong></td><td>How the money flows in continuous markets</td><td><a href="/how-it-works/economics">Economics</a></td></tr>
<tr><td><strong>vs Polymarket</strong></td><td>Direct comparison with the leading binary platform</td><td><a href="/comparisons/vs-polymarket">vs Polymarket</a></td></tr>
</tbody>
</table>
