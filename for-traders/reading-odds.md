---
title: "Reading Odds & Probabilities"
---


Understanding how Skepsis calculates odds will help you spot value and make better predictions.

---

## The Basics

### Probability → Odds

Skepsis displays both probability and odds for every range:

| Probability | Odds (Multiplier) | What It Means |
|-------------|-------------------|---------------|
| 50% | 2x | Coin flip, double your money |
| 25% | 4x | Underdog, 4x payout |
| 10% | 10x | Long shot, 10x payout |
| 5% | 20x | Very unlikely, 20x payout |

### The Formula

```
Odds = 1 / Probability

Example:
- Range probability: 25%
- Odds = 1 / 0.25 = 4x
- \$100 bet → \$400 payout if correct
```

---

## Reading the Probability Distribution

When you open a market, you see a probability curve that represents the crowd's consensus.

<Frame>
  <img src="/images/range-selection.gif" alt="Probability distribution curve on Skepsis" />
</Frame>

### What the Shape Tells You

| Shape | Meaning | Opportunity |
|-------|---------|-------------|
| **Tall narrow peak** | High confidence in specific range | Low odds in center, good odds on edges |
| **Wide flat** | Uncertainty | Similar odds everywhere |
| **Two peaks** | Market disagrees with itself | Pick a side for better odds |
| **Long tail** | Some believe in extreme outcome | High-risk, high-reward tail bets |

---

## Understanding Your Quote

When you select a range and amount, you get a quote:

<Frame>
  <img src="/images/bet-slip.png" alt="Bet slip showing odds and potential payout" />
</Frame>

### Breaking It Down

#### Return (Odds)
Your multiplier if you win.

```
Return = Total Payout / Your Bet
2.0x = \$200 / \$100
```

#### Win Probability
The market's current estimate of your range winning.

```
Probability = 1 / Return
50% = 1 / 2.0
```

#### If You Win
The total amount you receive (your initial bet + profit).

```
Payout = Bet × Return
\$200 = \$100 × 2.0
```

---

## Finding Value

**Value** exists when you think the true probability is higher than the market's implied probability.

### Example: Spotting Value

```
Market shows: Range \$96K-\$97K at 20% probability (5x odds)

You believe: Based on your analysis, true probability is 30%

Expected Value calculation:
- EV = (Your prob × Payout) - Investment
- EV = (0.30 × \$500) - \$100
- EV = \$150 - \$100 = +\$50

This is a +EV bet! The market is mispricing this range.
```

### When to Bet

| Your Belief vs Market | Action |
|----------------------|--------|
| Your prob > Market prob | ✅ Bet (you have edge) |
| Your prob = Market prob | ⚖️ Neutral (no edge) |
| Your prob < Market prob | ❌ Don't bet (negative edge) |

---

## How Odds Change

Skepsis uses **LMSR (Logarithmic Market Scoring Rule)** which means:

### After Someone Bets on a Range:

1. **That range's probability increases**
2. **That range's odds decrease** (less payout per dollar)
3. **Other ranges' probabilities decrease**
4. **Other ranges' odds increase** (more payout per dollar)

### Example: Price Movement

```
Before Alice's \$500 bet on \$96K-\$97K:
- \$96K-\$97K: 20% prob, 5x odds
- \$97K-\$98K: 25% prob, 4x odds

After Alice's bet:
- $96K-$97K: 28% prob, 3.6x odds  ← Probability up, odds down
- $97K-$98K: 22% prob, 4.5x odds  ← Probability down, odds up
```

### What This Means for You

- **Bet early** if you have a view — you get better odds
- **Bet against the crowd** — unpopular ranges have better odds
- **Watch for overreaction** — big bets can create value elsewhere

---

## Comparing Odds Across Markets

Different markets have different liquidity, which affects spreads.

### High Liquidity Market
```
Range \$96K-\$97K:
- Buy price: \$0.31 per share
- Sell price: \$0.29 per share
- Spread: 6.5%
```

### Low Liquidity Market
```
Range \$96K-\$97K:
- Buy price: \$0.35 per share
- Sell price: \$0.22 per share  
- Spread: 37%
```

<Warning>
**Low liquidity = wider spreads.** You pay more to enter and get less when exiting. Prefer high-liquidity markets when possible.
</Warning>

---

## Odds vs Expected Value

High odds ≠ good bet. What matters is **expected value**.

### The Math

```
Expected Value (EV) = (Probability × Payout) - Cost

Good bet: EV > 0
Bad bet: EV < 0
```

### Comparing Bets

| Bet | Odds | Your Est. Prob | EV per \$100 |
|-----|------|----------------|-------------|
| A | 2x | 60% | +\$20 ✅ |
| B | 10x | 8% | -\$20 ❌ |
| C | 5x | 25% | +\$25 ✅ |
| D | 20x | 5% | \$0 ⚖️ |

**Bet C is best** despite lower odds than B or D because your edge is highest.

---

## Quick Probability-to-Odds Table

| Probability | Odds | \$100 Payout |
|-------------|------|-------------|
| 80% | 1.25x | \$125 |
| 50% | 2x | \$200 |
| 33% | 3x | \$300 |
| 25% | 4x | \$400 |
| 20% | 5x | \$500 |
| 10% | 10x | \$1,000 |
| 5% | 20x | \$2,000 |
| 2% | 50x | \$5,000 |
| 1% | 100x | \$10,000 |

---

## Deterministic Payouts: The Skepsis Advantage

Unlike traditional betting where payouts can change:

### Traditional Betting
```
You bet at 5x odds
More people bet the same
Final payout: 3x (reduced!)
```

### Skepsis
```
You bet at 5x odds
More people bet the same  
Your payout: Still 5x (locked in!)
```

**Your odds are guaranteed the moment you bet.** Future trading doesn't affect your payout.

---

## Next Steps

<table data-card-size="large" data-view="cards">
<thead><tr><th></th><th></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead>
<tbody>
<tr><td><strong>Deterministic Payouts</strong></td><td>Deep dive into payout mechanics</td><td><a href="/for-traders/deterministic-payouts">Deterministic Payouts</a></td></tr>
<tr><td><strong>Strategies</strong></td><td>Put your odds knowledge to work</td><td><a href="/for-traders/strategies">Strategies</a></td></tr>
</tbody>
</table>
