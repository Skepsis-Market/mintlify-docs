---
title: "Understanding Ranges"
---

A range is a span of values where you think the outcome will land. In a BTC price market (\$90K-\$110K), selecting \$96K-\$98K means you're betting BTC settles somewhere in that window at resolution.

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

## Range Width vs Odds

Width = probability. A \$500 range might sit at ~12% probability (8x odds), while a \$5,000 range covers ~78% (1.3x). Narrower pays more because it's harder to hit.

---

## Range Archetypes

**Sniper** (2-3 buckets, 10x+): High conviction, narrow range. You need real edge to justify this.

**Zone** (15-25 buckets, 2-4x): Directional bet with room for error. The workhorse range.

**Wide** (30+ buckets, 1.3-2x): High probability, low payout. Good for hedging or grinding.

---

## Range Positioning

Where you place your range matters as much as width. With BTC at \$97K:

- **Centered (\$96K-\$98K):** Betting on stability.
- **Bullish (\$97.5K-\$99.5K):** Modest up move needed.
- **Bearish (\$94.5K-\$96.5K):** Modest down move needed.

### Tail Bets

Ranges far from current price — \$90K-\$93K or \$102K-\$105K — pay 20x+ but hit rarely. Size accordingly.

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

**Going too narrow:** A \$100-wide range at 50x odds is ~2% probability. Unless you have serious edge, widen to \$500+ for short-term markets.

**Ignoring the distribution:** Check why a range is priced where it is before betting into it. Cheap ranges are usually cheap for a reason.

**Chasing multipliers:** 25x = ~4% win rate. Think in expected value, not potential payout.

**Over-hedging:** Covering too many ranges guarantees net losses. Hedge with purpose, not anxiety.

## Quick Reference

| Confidence | Width | Typical Odds |
|------------|-------|-------------|
| High conviction | 2-3 buckets | 10-15x |
| Directional view | 5-10 buckets | 4-8x |
| Loose thesis | 15-25 buckets | 2-4x |
| Just want action | 30+ buckets | 1.5-2x |
