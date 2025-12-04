---
title: "Skepsis vs Polymarket"
---

# Skepsis vs Polymarket

How Skepsis compares to the leading prediction market platform.

---

## Quick Comparison

| Feature | Polymarket | Skepsis |
|---------|------------|---------|
| **Market type** | Binary (Yes/No) | Continuous (Ranges) |
| **Question format** | "Will X happen?" | "Where will X be?" |
| **Blockchain** | Polygon | Sui |
| **Payout timing** | At resolution | Deterministic at bet time |
| **Liquidity model** | Order book + AMM | Pure LMSR |
| **Information density** | Single probability | Full distribution |

---

## Market Type: The Core Difference

### Polymarket: Binary

Every market is a yes/no question:

```
"Will Bitcoin hit $100K by January 1?"
├── Yes: 47%
└── No: 53%

One data point. Cross threshold or don't.
```

### Skepsis: Continuous

Markets show full distributions:

```
"Where will Bitcoin be on January 1?"
├── $80K-$90K:   5%
├── $90K-$95K:   12%
├── $95K-$100K:  25%
├── $100K-$105K: 30%  ← Most likely
├── $105K-$110K: 18%
└── $110K+:      10%

Full probability landscape visible.
```

---

## The "Almost Right" Problem

### On Polymarket

```
You bet YES on "BTC > $100K by Jan 1"
BTC on Jan 1: $99,500

Result: You LOSE
Reality: You were basically right about the price
```

### On Skepsis

```
You bet on "$95K - $105K" range
BTC on Jan 1: $99,500

Result: You WIN ✅
Reality: Your prediction was accurate
```

**Skepsis rewards accuracy. Polymarket rewards threshold crossing.**

---

## Information Value

### What Polymarket Tells You

```
"BTC > $100K?" = 47% Yes

You know: ~47% chance of crossing $100K
You don't know:
- Will it be $100,001 or $200,000?
- How confident is the market?
- What about $95K? $90K?
```

### What Skepsis Tells You

```
Full distribution visible:
- Expected value: ~$101,500
- Mode (most likely): $100K-$105K
- 90% confidence interval: $88K-$115K
- Tail risk: 5% chance of <$85K
- Uncertainty: Distribution is fairly wide
```

**One Skepsis market = infinite binary questions answered**

---

## Expressing Complex Views

### On Polymarket

To express "BTC will be between $95K-$105K":

```
Step 1: Find "BTC > $95K?" market → Buy Yes
Step 2: Find "BTC > $105K?" market → Buy No
Step 3: Hope both markets exist and have liquidity
Step 4: Manage two positions
Step 5: Pay fees twice
```

### On Skepsis

```
Step 1: Select $95K-$105K range
Step 2: Place bet
Done.
```

**Same view. One transaction. One fee. One position.**

---

## Liquidity Model

### Polymarket: Hybrid (Order Book + AMM)

```
Pros:
+ Tight spreads on popular markets
+ Professional market makers participate

Cons:
- Orders can go unfilled
- Spread varies by market
- Less liquid markets have wide spreads
```

### Skepsis: Pure LMSR

```
Pros:
+ Always liquid (any size, any time)
+ Mathematically guaranteed solvency
+ Consistent pricing model

Cons:
- Spreads depend on alpha parameter
- Less efficient for very large trades
```

---

## Payout Timing

### Polymarket

```
You buy Yes at $0.47
Market moves, Yes now at $0.52
If you sell: Get $0.52 (profit!)
If you hold to resolution: Get $1 (if Yes) or $0 (if No)
```

Payouts depend on market price at action time.

### Skepsis

```
You buy 100 shares at $0.32/share
Market moves, price now $0.40/share
Your payout if you win: Still $100 (locked in!)
```

**Deterministic payouts = no surprises**

---

## Blockchain & UX

### Polymarket (Polygon)

```
Gas fees: Very low (~$0.01)
Transaction speed: ~2 seconds
Wallet: MetaMask, etc.
Currency: USDC on Polygon
```

### Skepsis (Sui)

```
Gas fees: Very low (~$0.001)
Transaction speed: <1 second
Wallet: Sui Wallet, Suiet
Currency: USDC on Sui
```

Both are fast and cheap. Sui has slight edge on speed.

---

## Use Case Comparison

### When to Use Polymarket

✅ Binary events (elections, yes/no questions)
✅ High-liquidity popular markets
✅ You want to trade positions before resolution
✅ Professional market making

### When to Use Skepsis

✅ Numerical predictions (prices, dates, measurements)
✅ You want to express ranges, not thresholds
✅ You want deterministic payouts
✅ You value full distribution information

---

## Real Example: Bitcoin Prediction

### The Question

"What will BTC price be on December 31, 2025?"

### On Polymarket (Multiple Markets Needed)

```
Market 1: "BTC > $80K?" → 89% Yes
Market 2: "BTC > $100K?" → 52% Yes
Market 3: "BTC > $120K?" → 28% Yes
Market 4: "BTC > $150K?" → 12% Yes

To understand the distribution:
- Manually calculate ranges from thresholds
- Hope all threshold markets exist
- Deal with different liquidities per market
```

### On Skepsis (One Market)

```
"Where will BTC be Dec 31, 2025?"

$60K-$80K:   8%
$80K-$100K:  35%
$100K-$120K: 30%
$120K-$150K: 18%
$150K+:      9%

Full distribution. One glance. One market.
```

---

## Can You Use Both?

Absolutely! They serve different needs:

| Your Need | Use |
|-----------|-----|
| "Will [candidate] win?" | Polymarket |
| "What will [price] be?" | Skepsis |
| "Will [event] happen?" | Polymarket |
| "When will [event] happen?" | Skepsis |
| "Will [metric] exceed [threshold]?" | Polymarket |
| "What will [metric] be?" | Skepsis |

---

## The Bottom Line

**Polymarket** is great for binary yes/no predictions with high liquidity.

**Skepsis** is better when:
- You want to predict WHERE, not just IF
- You want to see full probability distributions
- You want deterministic payouts
- You want to express nuanced, range-based views

---

## Try Skepsis

Experience the difference between binary and continuous markets.

<Note>
**Make a continuous prediction:** [Launch Skepsis →](https://beta.skepsis.live)
</Note>
