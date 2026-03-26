---
title: "LMSR Explained (For Humans)"
---


The math behind Skepsis pricing, explained simply.

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
A: $94K-$95K
B: $95K-$96K  
C: $96K-$97K  ← Current price is here
D: $97K-$98K
E: $98K-$99K
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

### After Alice Bets $100 on Range C

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

### After Bob Bets $200 on Range C

```
Range A: 14% (7.1x odds)  ██
Range B: 14% (7.1x odds)  ██
Range C: 44% (2.3x odds)  █████████  ← Alice + Bob
Range D: 14% (7.1x odds)  ██
Range E: 14% (7.1x odds)  ██
```

**What happened:**
- Range C moved even more
- But not twice as much, due to logarithmic diminishing returns
- Other ranges now have better odds for contrarians

---

## Key Properties of LMSR

**Infinite liquidity.** No order book, no counterparties. The cost function always returns a quote, so every trade fills immediately.

**Bounded loss.** The protocol's maximum loss is mathematically bounded — it can't go bankrupt regardless of outcomes.

**Path independence.** Final prices depend only on total shares outstanding, not the order trades came in. Alice then Bob, or Bob then Alice — same result. No timing advantage.

**No manipulation.** A whale buying $10K of shares to push the price up can't profit by selling — the act of selling pushes the price back down. The cost function is symmetric, so pump-and-dump strategies net out to roughly zero (minus fees).

---

## The Alpha Parameter

Alpha (α) controls how sensitive prices are to bets:

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

Here's a simplified look under the hood:

### The Cost Function

```
Cost to buy shares = C(after) - C(before)

Where C(q) = α × ln(Σ e^(qi/α))

Where:
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

Uniswap-style AMMs price token pairs across an unbounded range — they don't care whether prices "add up" to anything. LMSR is purpose-built for predictions: outcome probabilities always sum to 100%, there's no impermanent loss (loss is bounded instead), and the price range is naturally constrained between 0% and 100%.

---

## Why LMSR for Prediction Markets

LMSR exists because prediction markets have a constraint that token markets don't: outcome probabilities must sum to 100%. LMSR enforces this natively. Combined with bounded loss, guaranteed liquidity, and incentive-compatibility (honest predictions are the profit-maximizing strategy), it's the standard choice for on-chain prediction markets.

---

## Further reading

- [Original LMSR paper — Robin Hanson](http://mason.gmu.edu/~rhanson/mktscore.pdf)
- [Gnosis LMSR implementation](https://gnosis.io/)
