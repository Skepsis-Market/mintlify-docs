---
title: "Risks & Returns"
---


The honest breakdown of what LPs can expect.

---

## How LPs Make Money

### 1. Trading Fees

Every trade on Skepsis pays a 0.3% fee. A portion of that flows to the Vault.

```
Daily trading volume: $500,000
Fee rate: 0.3%
Daily fees: $1,500
LP share of fees: ~$600

On a $100,000 Vault position, that's 0.6%/day
(Hypothetical — actual volume varies)
```

### 2. Market Maker Spread

LMSR doesn't price at exactly "fair value" — there's a tiny spread built into the math. This spread is what makes the system solvent, and it benefits LPs.

```
Sum of all range probabilities: 100%
Sum of all range prices: slightly > $1

That "slightly more" is your edge as an LP.
```

### 3. Losing Trader Capital

When traders bet wrong, their capital stays in the pool. After winners are paid, the remainder goes back to the Vault.

```
Market pool: $15,000
Winners claim: $8,000
Remaining: $7,000 → Returns to Vault

If the Vault deployed $10,000, it lost $3,000 on this market.
But across many markets, winners and losers balance out.
```

---

## How LPs Lose Money

### The Winning Range Problem

If a very popular range wins, the market owes a lot of USDC. The Vault covers the gap.

```
Everyone bets on $96K-$97K
BTC lands at $96,500
Many winners, many payouts

Pool can't cover it all from trader bets alone
→ Vault-deployed capital covers the rest
→ LP loss on this market
```

### The Bound

Here's the good news: the maximum LP loss per market is mathematically capped.

```
Max LP loss = α × ln(bucketCount)

Typical values:
- α = 3,333 USDC, 16 buckets → Max loss ≈ $9,240
- α = 1,000 USDC, 8 buckets  → Max loss ≈ $2,079

This is known BEFORE the market starts.
```

---

## Alpha Decay: The LP's Friend

Here's where it gets interesting. Markets on Skepsis can use **alpha decay** — the liquidity parameter shrinks over time.

### Why This Helps LPs

```
Market opens: α = 3,333
Required reserves: $9,240

Market matures: α = 1,000
Required reserves: $2,772

Surplus released: $6,468
→ Vault harvests this → LPs get capital back early
```

Early in a market's life, spreads are wide and the LP takes more risk — but earns more from the spread. As the market matures, spreads tighten (better for traders), and the LP's risk decreases. The excess capital gets recycled.

---

## Solvency: Three Layers

### Layer 1: Market Level

Every market enforces the P-Z invariant:

```
poolBalance ≥ maxLiability + 2 × α × ln(N)

Translation: The market always has enough to pay winners.
If a trade would violate this, it reverts. No exceptions.
```

### Layer 2: Vault Level

The Vault keeps a 20% liquid buffer — capital not deployed to any market.

```
Vault total: $100,000
Deployed: $80,000 (across markets)
Liquid buffer: $20,000

This covers:
- Withdrawal queue processing
- Emergency scenarios
- New market seeding
```

### Layer 3: Per-Market Cap

No single market gets more than 20% of the Vault.

```
Vault total: $100,000
Max per market: $20,000

Even if a market goes maximally wrong,
the Vault loses at most ~$9K, not $100K.
```

---

## Expected Returns

Let's be realistic. LP returns depend on:

| Factor | Good for LPs | Bad for LPs |
|--------|-------------|-------------|
| High trading volume | More fees | — |
| Balanced betting | Spread across ranges | — |
| Alpha decay | Surplus harvest | — |
| Many markets | Diversification | — |
| — | — | One-sided betting |
| — | — | Low volume |
| — | — | Many popular ranges winning |

**Bottom line:** LPs are betting that across many markets, trading fees and spread income will outweigh payouts to winners. History of LMSR-based systems suggests this is generally true, but not guaranteed.

---

## Summary

| Aspect | Detail |
|--------|--------|
| **Revenue sources** | Trading fees, spread, losing trader capital |
| **Risk** | Popular winning ranges, bounded per market |
| **Max loss per market** | α × ln(N), known in advance |
| **Withdrawal** | Queue-based, FIFO |
| **Best for** | Patient capital, believers in prediction market volume |

---

## Next Steps

<table data-card-size="large" data-view="cards">
<thead><tr><th></th><th></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead>
<tbody>
<tr><td><strong>The Vault</strong></td><td>How to deposit and get started</td><td><a href="/for-lps/vault-overview">The Vault</a></td></tr>
<tr><td><strong>LMSR Explained</strong></td><td>The math that makes it work</td><td><a href="/how-it-works/lmsr-for-humans">LMSR Explained</a></td></tr>
</tbody>
</table>
