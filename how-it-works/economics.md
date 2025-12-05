---
title: "Economics"
---


Where does the money come from? Where does it go? How does Skepsis stay solvent?

---

## The Simple Version

```
Money In: Traders pay for shares
Money Out: Winners get paid

The Protocol: Manages the flow, takes a small fee
```

That's it. No complex token economics. No ponzinomics. Just predictions and payouts.

---

## The Money Flow

### Step 1: Market Creation

A market creator deposits **initial liquidity**:

```
Creator deposits: \$10,000 USDC
This becomes: The prize pool
```

This liquidity enables trading from day one.

### Step 2: Trading

Traders buy shares in ranges they believe will win:

```
Alice buys: \$100 on range \$96K-\$97K (gets 400 shares)
Bob buys: \$200 on range \$97K-\$98K (gets 500 shares)  
Charlie buys: \$150 on range \$95K-\$96K (gets 800 shares)

Pool grows: \$10,000 + \$100 + \$200 + \$150 = \$10,450
```

### Step 3: Resolution

The outcome is revealed, winners claim:

```
Result: BTC = \$97,200 (Bob's range wins!)

Bob's 500 shares × \$1 = \$500 payout
Alice: \$0 (wrong range)
Charlie: \$0 (wrong range)

Bob's profit: \$500 - \$200 = \$300 ✅
```

### Step 4: Remaining Balance

After all claims:

```
Pool started: \$10,450
Bob claimed: \$500
Pool remaining: \$9,950

This stays in the system for:
- LP withdrawal
- Protocol fees
- Next market seeding
```

---

## Where Winners' Money Comes From

### Source 1: Losing Bets

The primary source. When you lose, your bet goes to:
1. Pay winners
2. Protocol fees
3. LP returns

```
Losers paid: \$250 (Alice + Charlie)
Winner received: \$500 (Bob)
Gap of \$250 from: Initial liquidity
```

### Source 2: Initial Liquidity

When losers don't cover winners, the initial liquidity bridges the gap.

```
Initial LP: \$10,000
Total bets: \$450 (Alice \$100, Bob \$200, Charlie \$150)
Pool: \$10,450

If winners claim \$500:
Losers contribute: \$250
LP contributes: \$250
Winner receives: \$500
```

### Source 3: LMSR Pricing Premium

The LMSR algorithm builds in a small edge for the market maker:

```
Sum of all range probabilities = 100%
Sum of implied prices = slightly > \$1 (spread)

This spread = market maker's edge = system stays solvent
```

---

## The Solvency Guarantee

**Critical question:** Can the market always pay winners?

**Answer:** Yes, by mathematical design.

### How LMSR Guarantees Solvency

```
Max possible payout = Total shares × \$1/share
Pool balance = Initial liquidity + All bets - Payouts

LMSR ensures: Pool balance ≥ Max possible payout (always)
```

### The Alpha Parameter

The **alpha (α)** in LMSR is calibrated to ensure:

```
Max LP loss = 50% of initial liquidity

If creator deposits \$10,000:
Worst case for LP: Lose \$5,000
Best case for LP: Profit from fees and losers
```

This is a known, bounded risk.

### Extreme Scenarios

**What if everyone bets on the winning range?**

```
All traders bet on Range C
Range C probability → very high
Range C odds → very low (close to 1x)

Result: Everyone wins... but wins very little
Pool still covers all payouts
```

The system self-balances.

---

## Fee Structure

### Trading Fees

A small fee on each transaction:

```
Fee: 0.3% (30 basis points)

On a \$100 bet:
Fee: \$0.30
Net bet: \$99.70
```

### Where Fees Go

```
Total fees collected
├── Protocol treasury (30%)
├── Market creator (30%)  
└── Liquidity providers (40%)
```

### Why Fees Exist

1. **Protocol sustainability** — Development, infrastructure, audits
2. **Creator incentives** — Reward for creating good markets
3. **LP incentives** — Return for providing liquidity

---

## For Market Creators

### The Investment

```
Create market with \$10,000 liquidity
Risk: Lose up to 50% (\$5,000) in worst case
Return: Share of trading fees + any remaining liquidity
```

### The Return

```
Market generates \$50,000 in trading volume
Fees at 0.3%: \$150
Creator share (30%): \$45

Plus: Return of remaining liquidity at market close
```

### Risk/Reward

| Outcome | Creator Result |
|---------|----------------|
| Low volume, balanced betting | ~\$0 profit, get liquidity back |
| High volume, balanced betting | Fee profit + most liquidity back |
| Low volume, unbalanced betting | Possible small loss |
| High volume, unbalanced betting | Fee profit may offset LP loss |

---

## For Traders

### Your Money Flow

```
You bet \$100:
├── \$99.70 goes to buy shares
└── \$0.30 goes to fees

If you win:
You receive: Shares × \$1/share = deterministic payout

If you lose:
Your \$99.70 pays other winners
```

### Expected Value

```
EV = (Your probability estimate × Payout) - Cost

Positive EV = Good bet
Negative EV = Bad bet

Example:
Market says: 25% (4x odds)
You think: 35%
EV = (0.35 × \$400) - \$100 = +\$40 ✅
```

---

## Economic Incentives Summary

### For Traders
- **Bet early** → Better odds (prices haven't moved)
- **Bet against crowd** → Higher potential returns
- **Be right** → Profit

### For Market Creators
- **Create interesting markets** → More volume → More fees
- **Set appropriate ranges** → Better UX → More bets
- **Bootstrap liquidity** → Attract early traders

### For the Protocol
- **More markets** → More fees
- **Better UX** → More users
- **Solvency** → Trust → Growth

---

## Comparison: Where Money Flows

### Traditional Betting (Casino/Sportsbook)
```
You bet \$100
House edge: 5-10%
House always profits
Zero-sum for bettors
```

### Prediction Markets (Polymarket-style)
```
You bet \$100 against other users
Platform takes ~2% fee
Winners take from losers
Platform always profits
```

### Skepsis
```
You bet \$100 against the market state
LMSR prices your bet fairly
If you have edge, you profit
Platform takes 0.3% fee
LPs take bounded risk for fee share
```

**Key difference:** Skepsis rewards accurate predictions, not just being on the winning side of a 50/50.

---

## FAQ

### "What if no one bets on the winning range?"

The initial liquidity pays winners. This is by design—LPs take this risk in exchange for fees.

### "Can the market run out of money?"

No. LMSR mathematically guarantees solvency. The alpha parameter ensures max payout ≤ pool balance.

### "Why would anyone provide liquidity?"

Expected return = Fees earned - LP losses
With balanced betting and sufficient volume, this is positive.

### "Is this sustainable?"

Yes. The 0.3% fee covers:
- Protocol costs
- Creator rewards  
- LP incentives

No external token subsidies needed.

---

## Next Steps

<table data-card-size="large" data-view="cards">
<thead><tr><th></th><th></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead>
<tbody>
<tr><td><strong>Trust & Resolution</strong></td><td>How outcomes are determined fairly</td><td><a href="/how-it-works/trust-and-resolution">Trust & Resolution</a></td></tr>
<tr><td><strong>LMSR Explained</strong></td><td>The math behind solvency</td><td><a href="/how-it-works/lmsr-for-humans">LMSR Explained</a></td></tr>
</tbody>
</table>
