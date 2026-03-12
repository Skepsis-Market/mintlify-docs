---
title: "Alpha Decay"
---


Why spreads get tighter over time — and why that's good for everyone.

---

## The Problem Alpha Decay Solves

When a market first opens, nobody knows anything. The crowd hasn't spoken yet. If spreads are tight from the start, a single whale can move prices dramatically and snipe cheap shares before anyone else has a chance.

But if spreads stay wide forever, the market never becomes efficient. Traders get bad prices even when the market is mature and well-informed.

**Alpha decay solves both problems at once.**

---

## How It Works

Alpha (α) is the liquidity parameter that controls how much prices move per trade. Think of it as the market's "shock absorber."

```
High α → Prices barely move per trade (wide shock absorber)
Low α  → Prices move a lot per trade (stiff shock absorber)
```

With alpha decay, the market starts with a high α and gradually decreases it:

```
Day 1:  α = 3,333  (wide spreads, whale-resistant)
Day 3:  α = 2,500  (moderate spreads)
Day 5:  α = 1,667  (tighter)
Day 7:  α = 1,000  (tight spreads, efficient pricing)
```

---

## A Day in the Life of a Market

### Morning: The Market Opens

```
BTC 24-hour market opens
α = 3,333 (high)

Alice bets $500 on $96K-$97K
Price moves: barely (0.3%)

This is by design — early info is noisy.
No one should dominate the price with one bet.
```

### Afternoon: The Crowd Arrives

```
α has decayed to 2,000

Same $500 bet now moves price 0.5%
Market is starting to form real opinions
Spreads are tighter — better deals for traders
```

### Evening: Market Matures

```
α = 1,000

The probability distribution is well-formed
Prices are responsive — good info gets rewarded
Spreads are tight — fair pricing for everyone
```

### The Result

Early bettors got paid a premium for betting with less information (wider spreads = better odds for contrarians). Late bettors get efficient prices that reflect the crowd's wisdom. Everyone wins.

---

## Why Traders Should Care

### Early Bird Premium

```
Alice bets at α = 3,333: Gets 6x odds on her range
Bob bets same range at α = 1,000: Gets 3.5x odds

Same prediction. Alice got paid more for betting first.
```

This is intentional. Alpha decay rewards conviction. If you have an edge, bet early.

### Late Game Efficiency

```
By the time α is low, prices are tight.
You see what the crowd actually thinks.
Great for spotting mispriced ranges.
```

---

## Why LPs Should Care

Alpha decay directly benefits LPs through surplus harvesting.

```
Market opens: α = 3,333
Required reserves: $9,240

Market matures: α = 1,000
Required reserves: $2,772

Surplus released: $6,468
→ Vault harvests this → LPs get capital back early
```

The Vault doesn't have to wait for resolution to start recouping capital. As α decays, the excess safety margin is returned.

---

## The Settings

Market creators configure alpha decay at creation:

| Parameter | What It Does |
|-----------|--------------|
| **Initial α** | Starting liquidity depth |
| **Final α** | Floor (spreads never go tighter than this) |
| **Decay start** | When decay begins (e.g., 2 hours after open) |
| **Duration** | How long until α reaches the floor |

```
Example:
Initial α = 3,333
Final α = 1,000 (can't go below 30% of initial)
Start: 1 hour after market opens
Duration: 6 hours

→ Spreads narrow linearly over 6 hours
```

---

## The Bottom Line

Alpha decay is the difference between a dumb market and a smart one. It starts cautious and ends precise — just like a good prediction should.

---

## Next Steps

<table data-card-size="large" data-view="cards">
<thead><tr><th></th><th></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead>
<tbody>
<tr><td><strong>LMSR Explained</strong></td><td>Understand the pricing algorithm</td><td><a href="/how-it-works/lmsr-for-humans">LMSR Explained</a></td></tr>
<tr><td><strong>The Vault</strong></td><td>How LPs benefit from alpha decay</td><td><a href="/for-lps/vault-overview">The Vault</a></td></tr>
</tbody>
</table>
