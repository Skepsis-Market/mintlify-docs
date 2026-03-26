---
title: "Economics"
---


Where the money comes from, where it goes, and how solvency is maintained.

---

## Money Flow

### Market Creation

A shared **Vault** pools LP capital and deploys it across active markets. When markets resolve, capital returns to the Vault for reuse. LPs earn fees across all markets rather than being locked into one.

### Trading

Traders buy shares in ranges they believe will contain the outcome:

```
Alice buys: $100 on range $96K-$97K (gets 400 shares)
Bob buys: $200 on range $97K-$98K (gets 500 shares)
Charlie buys: $150 on range $95K-$96K (gets 800 shares)
```

### Resolution

The outcome is revealed and winners claim. 1 share in the winning bucket = $1 USDC.

```
Result: BTC = $97,200 (Bob's range wins)

Bob's 500 shares × $1 = $500 payout
Bob's profit: $500 - $200 = $300
Alice and Charlie: $0
```

### Remaining Balance

After all claims, the remaining pool balance covers LP withdrawal, protocol fees, and seeds future markets.

---

## Where Winners' Money Comes From

Three sources, in order of priority:

1. **Losing bets** — the primary source. Losers' capital pays winners.
2. **Initial liquidity** — when losers don't fully cover winners, LP capital bridges the gap. This is the bounded risk LPs take in exchange for fees.
3. **LMSR pricing spread** — the sum of implied prices across all ranges slightly exceeds $1, giving the market maker a built-in edge that keeps the system solvent.

---

## Solvency Guarantee

LMSR mathematically guarantees that pool balance >= max possible payout at all times. The alpha parameter bounds worst-case LP loss to 50% of initial liquidity — a known, bounded risk.

When everyone piles into the same range, odds compress toward 1x. Everyone wins, but wins very little. The pool still covers all payouts.

---

## Fee Structure

A fee of 0.3%-1% (varies by market risk category) is taken on each transaction.

```
On a $100 bet at 0.5% fee:
Fee: $0.50
Net bet: $99.50
```

Fee distribution:

```
Total fees collected
├── Protocol treasury (30%)
├── Market creator (30%)
└── Liquidity providers (40%)
```

---

## For Market Creators

Creators deposit initial liquidity and earn a share of trading fees. Risk is bounded: worst case is losing up to 50% of deposited liquidity. With balanced betting and decent volume, fee income plus returned liquidity makes this profitable.

---

## For Traders

```
You bet $100:
├── $99.70 goes to buy shares
└── $0.30 goes to fees

If you win: Shares × $1/share = deterministic payout
If you lose: Your capital pays other winners
```

Expected value: `EV = (Your probability estimate × Payout) - Cost`. If the market prices a range at 25% and you think it's 35%, that's a +EV bet.

---

## FAQ

**What if no one bets on the winning range?**
The initial liquidity pays winners. LPs take this risk in exchange for fees.

**Can the market run out of money?**
No. LMSR mathematically guarantees solvency. Alpha ensures max payout <= pool balance.

**Why would anyone provide liquidity?**
Expected return = fees earned - LP losses. With balanced betting and sufficient volume, this is positive. No external token subsidies needed.
