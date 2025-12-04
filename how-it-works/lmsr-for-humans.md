---
title: "LMSR Explained (For Humans)"
---


The math behind Skepsis pricing — no PhD required.

---

## What is LMSR?

**LMSR** stands for **Logarithmic Market Scoring Rule**. It's the algorithm that:

1. Sets prices for every range
2. Updates prices when people bet
3. Guarantees there's always liquidity
4. Ensures the market stays solvent

Think of it as the **automated market maker** that runs every Skepsis market.

---

## The Simple Explanation

### The Core Idea

Imagine a market with 5 possible outcome ranges:

```
A: \$94K-\$95K
B: \$95K-\$96K  
C: \$96K-\$97K  ← Current price is here
D: \$97K-\$98K
E: \$98K-\$99K
```

LMSR assigns each range a **probability** based on how many people have bet on it:

```
More bets on C → C's probability goes up
C's probability up → C's odds go down
Other ranges → Their probabilities go down
Other ranges → Their odds go up
```

### Why Logarithmic?

The "logarithmic" part means:

- **Small bets** move prices a little
- **Large bets** move prices more, but with diminishing impact
- **No bet can move prices to 0% or 100%**

This prevents manipulation and keeps the market stable.

---

## A Visual Example

### Starting State

New market, no bets yet. All ranges equally likely:

```
Range A: 20% (5x odds)  ████
Range B: 20% (5x odds)  ████
Range C: 20% (5x odds)  ████
Range D: 20% (5x odds)  ████
Range E: 20% (5x odds)  ████
```

### After Alice Bets \$100 on Range C

```
Range A: 17% (5.9x odds)  ███
Range B: 17% (5.9x odds)  ███
Range C: 32% (3.1x odds)  ██████  ← Alice's bet
Range D: 17% (5.9x odds)  ███
Range E: 17% (5.9x odds)  ███
```

**What happened:**
- Range C probability increased (more demand)
- Range C odds decreased (worse deal now)
- Other ranges' odds improved (less demand)

### After Bob Bets \$200 on Range C

```
Range A: 14% (7.1x odds)  ██
Range B: 14% (7.1x odds)  ██
Range C: 44% (2.3x odds)  █████████  ← Alice + Bob
Range D: 14% (7.1x odds)  ██
Range E: 14% (7.1x odds)  ██
```

**What happened:**
- Range C moved even more
- But not twice as much (logarithmic diminishing returns)
- Other ranges now have great odds for contrarians

---

## Key Properties of LMSR

### 1. Infinite Liquidity

You can **always** place a bet. There's no order book, no waiting for counterparties.

```
Traditional exchange: "No sellers at this price, order not filled"
LMSR: "Here's your quote, always available"
```

### 2. Bounded Loss

The market maker (protocol) has a **known maximum loss**. It can't go bankrupt.

```
Initial liquidity: $10,000
Max possible loss: ~$5,000 (50%)
This is calculated mathematically, guaranteed.
```

### 3. Path Independence

The final market state depends only on **total bets**, not the order they came in.

```
Scenario A: Alice bets $100, then Bob bets $100
Scenario B: Bob bets $100, then Alice bets $100

Final prices: SAME in both scenarios
```

This means no one gets an unfair advantage by timing.

### 4. No Manipulation

You can't "pump and dump" the market:

```
Whale buys $10K to move price up
Whale tries to sell at new price
Selling moves price back down
Whale ends up roughly where they started (minus fees)
```

---

## The Alpha Parameter

You might hear about "alpha" (α) in Skepsis discussions. Here's what it means:

### What Alpha Does

Alpha controls how sensitive prices are to bets:

| Alpha | Effect | Who Benefits |
|-------|--------|--------------|
| **High α** | Prices move slowly | Large traders, stable odds |
| **Low α** | Prices move quickly | Small traders, volatile odds |

### The Skepsis Approach

We use **dynamic alpha** that adjusts based on market liquidity:

```
Formula: α = pool_balance / (2 × ln(n))

Where:
- pool_balance = current liquidity in the market
- n = number of buckets/ranges
- ln = natural logarithm
```

### Why This Matters

- **More liquidity** = higher alpha = more stable prices
- **Less liquidity** = lower alpha = prices move more per bet

This means:
- Popular markets are more stable
- Small markets are more volatile (but potentially more profitable)

---

## How Prices Actually Calculate

Let's peek under the hood (simplified):

### The Cost Function

```
Cost to buy shares = C(after) - C(before)

Where C(q) = α × ln(Σ e^(qi/α))

Don't panic! Let's break it down:
- q = shares in each bucket
- α = liquidity parameter
- The formula sums up exponentials
```

### In Plain English

1. Look at current state of all buckets
2. Calculate a "cost score" (C_before)
3. Add your shares to your bucket
4. Calculate new "cost score" (C_after)
5. You pay the difference

### Why Exponentials?

The exponential function creates:
- Smooth price transitions
- No sudden jumps
- Prices always between $0 and $1 per share
- Natural probability interpretation

---

## LMSR vs Other Systems

### vs Order Books (Traditional Exchanges)

| Feature | Order Book | LMSR |
|---------|------------|------|
| Liquidity | Depends on traders | Always available |
| Spread | Variable | Predictable |
| Fill guarantee | Not guaranteed | Always fills |
| Complexity | Simple concept | Math-heavy |

### vs AMMs (Uniswap-style)

| Feature | Uniswap AMM | LMSR |
|---------|-------------|------|
| Use case | Token swaps | Predictions |
| Price range | 0 to ∞ | 0% to 100% |
| Impermanent loss | Yes | No (bounded loss) |
| Sum to 100%? | No | Yes (probabilities) |

---

## Why LMSR is Perfect for Prediction Markets

1. **Probabilities naturally sum to 100%** — Unlike token prices, predictions must add up
2. **Bounded loss** — Market can always pay winners
3. **Always liquid** — No waiting for counterparties
4. **Incentivizes truth** — Honest predictions are rewarded

---

## The Bottom Line

You don't need to understand the math to use Skepsis. Just know:

- ✅ Prices automatically adjust based on betting activity
- ✅ More popular ranges = lower odds
- ✅ Less popular ranges = higher odds
- ✅ You can always bet (infinite liquidity)
- ✅ Your payout is guaranteed (deterministic)

The LMSR handles all the complexity behind the scenes.

---

## Want to Go Deeper?

For the mathematically curious:

- [Original LMSR Paper by Robin Hanson](http://mason.gmu.edu/~rhanson/mktscore.pdf)
- [Gnosis LMSR Implementation](https://gnosis.io/)
- Our technical docs (coming soon)

---

## Next Steps

<table data-card-size="large" data-view="cards">
<thead><tr><th></th><th></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead>
<tbody>
<tr><td><strong>Continuous vs Binary</strong></td><td>Why distributions beat yes/no</td><td><a href="/how-it-works/continuous-vs-binary">Continuous vs Binary</a></td></tr>
<tr><td><strong>Economics</strong></td><td>Where does the money come from?</td><td><a href="/how-it-works/economics">Economics</a></td></tr>
</tbody>
</table>
