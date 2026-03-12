---
title: "Understanding Ranges"
---


The key to successful Skepsis trading is understanding how range selection affects your odds and risk.

---

## What is a Range?

A range is a span of values where you believe the outcome will land.

**Example:** In a BTC price market with range \$90,000 - \$110,000:
- You select: **\$96,000 - \$98,000**
- This means: "I believe BTC will be somewhere between \$96K and \$98K at resolution"

---

## How Ranges Work

<Frame>
  <img src="/images/range-selection.gif" alt="Selecting a range on the Skepsis interface" />
</Frame>

<Accordion title="Deep Dive: How Ranges are Calculated (Buckets)">
  Every market is divided into discrete **buckets** (also called "spreads").

  **Example:**
  - Market: BTC Price (\$90K - \$110K)
  - Buckets: 200 (each bucket = \$100 width)

  When you select a range like **\$96,000 - \$98,000**, you are actually buying a bundle of **20 adjacent buckets** (Buckets 60 through 79). Your probability of winning is the sum of the probabilities of all these individual buckets.
</Accordion>

---

## Range Width vs Odds Trade-off

This is the most important concept in Skepsis trading: **Width = Probability**.

| Range Type | Width | Win Probability | Odds | Risk |
|------------|-------|-----------------|------|------|
| **Narrow** | \$500 | ~12% (Low) | **8.0x** | 🔴 High |
| **Medium** | \$2,000 | ~45% (Medium) | **2.2x** | 🟡 Medium |
| **Wide** | \$5,000 | ~78% (High) | **1.3x** | 🟢 Low |

<Tip>
**The Golden Rule:** Narrower ranges pay more because they are harder to hit. Wider ranges pay less because they are "safer".
</Tip>

---

## Strategic Range Selection

<CardGroup cols={3}>
  <Card title="The Sniper 🎯" icon="crosshairs">
    **Approach:** Very narrow range, high conviction.
    
    **Best for:** Expert analysis, insider edge.
    
    **Risk:** 🔴 High
    **Reward:** 🚀 Very High (10x+)
  </Card>
  <Card title="The Zone Player 🎲" icon="dice">
    **Approach:** Medium range, balanced view.
    
    **Best for:** General directional bets.
    
    **Risk:** 🟡 Medium
    **Reward:** ⚖️ Balanced (3-5x)
  </Card>
  <Card title="The Safe Player 🛡️" icon="shield">
    **Approach:** Wide range, high probability.
    
    **Best for:** Bankroll building, hedging.
    
    **Risk:** 🟢 Low
    **Reward:** 🐢 Steady (1.2-2x)
  </Card>
</CardGroup>

### Strategy Examples

<Tabs>
  <Tab title="Sniper Example">
    **Scenario:** BTC at \$97,000, big news expected.
    
    - **Range:** \$97,400 - \$97,600 (Width: \$200)
    - **Odds:** 15x
    - **Outcome:** If BTC hits \$97,500, you turn \$100 into \$1,500.
  </Tab>
  <Tab title="Zone Example">
    **Scenario:** BTC at \$97,000, expect stability.
    
    - **Range:** \$96,500 - \$98,000 (Width: \$1,500)
    - **Odds:** 3x
    - **Outcome:** If BTC stays flat, you turn \$100 into \$300.
  </Tab>
  <Tab title="Safe Example">
    **Scenario:** BTC at \$97,000, just want a win.
    
    - **Range:** \$94,000 - \$100,000 (Width: \$6,000)
    - **Odds:** 1.4x
    - **Outcome:** Unless BTC crashes/moons, you turn \$100 into \$140.
  </Tab>
</Tabs>

---

## Range Positioning

Where you place your range matters as much as how wide it is.

### Centering vs. Directional

Assuming Current BTC Price: **\$97,000**

- **Centered Range (\$96k - \$98k):** Betting on "no big move". You win if the price stays stable.
- **Bullish Range (\$97.5k - \$99.5k):** Betting on a "modest up move". You need the price to rise slightly.
- **Bearish Range (\$94.5k - \$96.5k):** Betting on a "modest down move". You need the price to fall slightly.

### Tail Betting

"Tail bets" are wagers on unlikely, extreme outcomes.

- **Left Tail (\$90k - \$93k):** The "Crash Bet". Pays huge (20x+) if the market collapses.
- **Right Tail (\$102k - \$105k):** The "Moon Bet". Pays huge (25x+) if the market rallies hard.

<Info>
**Tail bets** are high-risk, high-reward. They're like buying lottery tickets—fun money only!
</Info>

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

**Problem:** "I'll bet on exactly \$97,000 - \$97,100"

**Reality:** Unless you have incredible edge, a \$100 range is almost never worth it. The odds might be 50x, but the probability is ~2%.

**Fix:** Widen to at least \$500-\$1,000 for short-term markets.

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
<tr><td><strong>Reading Odds</strong></td><td>How odds are calculated from probabilities</td><td><a href="/for-traders/reading-odds">Reading Odds</a></td></tr>
<tr><td><strong>Strategies</strong></td><td>Advanced betting strategies</td><td><a href="/for-traders/strategies">Strategies</a></td></tr>
</tbody>
</table>
