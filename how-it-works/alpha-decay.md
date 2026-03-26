---
title: "Alpha Decay"
---


Spreads start wide and tighten over time, protecting early markets from whale manipulation while converging toward efficient pricing.

---

## How It Works

Alpha (α) is the liquidity parameter that controls price impact per trade. A high α means prices barely move; a low α means each trade has more impact.

With alpha decay, markets start at a high α and linearly decrease it:

```
Day 1:  α = 3,333  (wide spreads, whale-resistant)
Day 3:  α = 2,500  (moderate spreads)
Day 5:  α = 1,667  (tighter)
Day 7:  α = 1,000  (tight spreads, efficient pricing)
```

Early bettors pay wider spreads — effectively a premium for acting on less information. As α decays, prices tighten and the market becomes more responsive to informed trading.

---

## Impact on Traders

At high α, a $500 bet might move the price 0.3%. By the time α has decayed to its floor, that same bet moves the price significantly more. This creates an early-bird premium:

```
Alice bets at α = 3,333: Gets 6x odds on her range
Bob bets same range at α = 1,000: Gets 3.5x odds

Same prediction. Alice got paid more for betting first.
```

If you have an edge, bet early.

---

## Impact on LPs

Alpha decay releases surplus reserves back to the Vault as spreads tighten:

```
Market opens: α = 3,333 → Required reserves: $9,240
Market matures: α = 1,000 → Required reserves: $2,772

Surplus released: $6,468 → Vault harvests, LPs get capital back early
```

The Vault doesn't have to wait for resolution to start recouping capital.

---

## Configuration

Market creators set alpha decay parameters at creation:

- **Initial α** — Starting liquidity depth
- **Final α** — Floor value (spreads never go tighter than this)
- **Decay start** — When decay begins (e.g., 2 hours after open)
- **Duration** — How long until α reaches the floor

```
Example:
Initial α = 3,333
Final α = 1,000 (can't go below 30% of initial)
Start: 1 hour after market opens
Duration: 6 hours

→ Spreads narrow linearly over 6 hours
```
