---
title: "Reading Odds & Probabilities"
---

Odds and probability are inverses: `Odds = 1 / Probability`. A range at 25% probability pays 4x. A range at 10% pays 10x. The UI shows both for every range.

---

## Reading the Distribution

When you open a market, you see a probability curve — the crowd's consensus.

<Frame>
  <img src="/images/range-selection.gif" alt="Probability distribution curve on Skepsis" />
</Frame>

The shape tells you a lot. A tall narrow peak means high confidence in one area (cheap odds on edges). A flat distribution means uncertainty everywhere. Two peaks mean the market is split — pick a side. A long tail means someone's positioning for an extreme move.

---

## Your Quote

When you select a range and amount, the bet slip shows three numbers:

<Frame>
  <img src="/images/bet-slip.png" alt="Bet slip showing odds and potential payout" />
</Frame>

- **Return (Odds):** Your multiplier if you win. `Payout / Bet`.
- **Win Probability:** The market's implied chance. `1 / Return`.
- **If You Win:** Total payout including your original bet. `Bet * Return`.

---

## Finding Value

**Value** exists when you think the true probability is higher than the market's implied probability.

### Example: Spotting Value

```
Market shows: Range $96K-$97K at 20% probability (5x odds)

You believe: Based on your analysis, true probability is 30%

Expected Value calculation:
- EV = (Your prob × Payout) - Investment
- EV = (0.30 × $500) - $100
- EV = $150 - $100 = +$50

+EV. Take it.
```

If your estimated probability exceeds the market's implied probability, you have edge. If not, pass.

---

## How Odds Change

Skepsis uses **LMSR (Logarithmic Market Scoring Rule)**, which means:

### After Someone Bets on a Range:

1. **That range's probability increases**
2. **That range's odds decrease** (less payout per dollar)
3. **Other ranges' probabilities decrease**
4. **Other ranges' odds increase** (more payout per dollar)

### Example: Price Movement

```
Before Alice's $500 bet on $96K-$97K:
- $96K-$97K: 20% prob, 5x odds
- $97K-$98K: 25% prob, 4x odds

After Alice's bet:
 - $96K-$97K: 28% prob, 3.6x odds  ← Probability up, odds down
 - $97K-$98K: 22% prob, 4.5x odds  ← Probability down, odds up
```

Bet early if you have a view — you get better odds. Large bets on one range create value in adjacent ranges.

---

## Liquidity and Spreads

Different markets have different liquidity depths. In a high-liquidity market, buy/sell spread on a range might be 6-7%. In a thin market, the same range could have a 30%+ spread. You pay more to enter and get less when exiting thin markets.

---

## Expected Value Over Odds

High odds don't make a good bet. Expected value does: `EV = (Your Probability * Payout) - Cost`.

A 5x bet where you estimate 25% probability has EV of +\$25 per \$100. A 10x bet where you estimate 8% has EV of -\$20. Always compare on EV, not multiplier.

## Reference

| Probability | Odds | \$100 Payout |
|-------------|------|-------------|
| 50% | 2x | \$200 |
| 25% | 4x | \$400 |
| 10% | 10x | \$1,000 |
| 5% | 20x | \$2,000 |
| 2% | 50x | \$5,000 |
| 1% | 100x | \$10,000 |

## Deterministic Payouts

Unlike parimutuel systems, your odds are locked at bet time. Future bets on the same range don't dilute your payout. See [Deterministic Payouts](/for-traders/deterministic-payouts) for the full mechanics.
