---
title: "Deterministic Payouts Explained"
---

# Deterministic Payouts Explained

One of Skepsis's most powerful features: **you know exactly what you'll win before you bet.**

---

## The Problem with Traditional Betting

### Parimutuel Systems (Horse Racing, etc.)

In traditional parimutuel betting:

```
You bet $100 on Horse A at "5x odds"
1,000 other people also bet on Horse A
Final odds: 2.5x (your payout got cut in half!)
```

**Why?** Because payouts are calculated *after* all bets are placed. More bets on your selection = smaller share of the pool.

### Traditional Prediction Markets

Even some prediction markets have this issue:

```
You buy "Yes" at $0.60 (implied 60% probability)
Market moves to $0.80
If you win, you still get $1.00 per share
But if you try to sell early, dynamics get complicated
```

---

## How Skepsis Works: Deterministic Payouts

When you place a bet on Skepsis, your payout is **locked in immediately**.

```
You bet $100 on range $96K-$97K
Quote shows: 3.2x odds, $320 payout

→ If the outcome lands in $96K-$97K, you receive exactly $320
→ This is guaranteed, no matter what happens next
```

### Why This Matters

| Feature | Parimutuel | Skepsis |
|---------|------------|---------|
| Payout known at bet time | ❌ No | ✅ Yes |
| Payout changes with more bets | ✅ Yes | ❌ No |
| Can calculate exact profit | ❌ No | ✅ Yes |
| Position is transferable | ❌ No | ✅ Yes |

---

## The Math Behind Deterministic Payouts

### Shares = Your Claim

When you bet, you receive **shares** in your selected range.

```
Investment: $100
Price per share: $0.3125
Shares received: 320

Each share = $1 payout if your range wins
Total payout = 320 × $1 = $320
```

### Shares Are Fixed

Once you have 320 shares, you have 320 shares. Period.

- Other people betting doesn't reduce your shares
- Market movements don't reduce your shares
- Time passing doesn't reduce your shares

**Your 320 shares = $320 if you win. Always.**

---

## What Happens to Prices After Your Bet?

When you bet $100 on a range:

### 1. Your Bet Moves Prices
```
Before: $96K-$97K at 25% probability, 4x odds
Your bet: $100
After: $96K-$97K at 28% probability, 3.57x odds
```

### 2. But Your Payout Doesn't Change
```
You locked in: 4x odds, $400 payout
New bettors get: 3.57x odds, $357 payout per $100
Your payout: Still $400 ✅
```

### 3. Future Bets Don't Affect You
```
10 more people bet $1000 each on your range
New odds: 2.5x
Your payout: Still $400 ✅
```

---

## The Trade-Off: Early vs Late Betting

Deterministic payouts create interesting dynamics:

### Early Bettors
- ✅ Get better odds (prices haven't moved yet)
- ❌ Take more risk (less information)
- ✅ Payout is locked regardless of future activity

### Late Bettors
- ❌ Get worse odds (prices already moved)
- ✅ Have more information
- ✅ Still get deterministic payout at their price

**This is fair:** Early bettors are rewarded for taking risk earlier.

---

## Practical Example: BTC Market

### Scenario: $10,000 Liquidity Market

```
Initial state (no bets yet):
$95K-$96K: 20% prob, 5x odds
$96K-$97K: 25% prob, 4x odds  ← Alice bets here
$97K-$98K: 25% prob, 4x odds  ← Bob bets here later
$98K-$99K: 20% prob, 5x odds
$99K-$100K: 10% prob, 10x odds
```

### Alice Bets First
```
Alice: $200 on $96K-$97K
Odds at bet time: 4x
Shares received: 800
Guaranteed payout: $800

After Alice's bet:
$96K-$97K: 32% prob, 3.1x odds
```

### Bob Bets Second
```
Bob: $200 on $97K-$98K
Odds at bet time: 3.8x (slightly worse due to Alice's bet shifting things)
Shares received: 760
Guaranteed payout: $760

After Bob's bet:
$97K-$98K: 30% prob, 3.3x odds
```

### Charlie Bets Last
```
Charlie: $200 on $96K-$97K (same range as Alice!)
Odds at bet time: 2.8x (worse than Alice got)
Shares received: 560
Guaranteed payout: $560
```

### Resolution: BTC = $96,500

```
Winner: $96K-$97K range

Alice: Bet $200, wins $800 (4x) ✅
Bob: Bet $200, wins $0 ❌
Charlie: Bet $200, wins $560 (2.8x) ✅

Alice got better odds because she bet first!
```

---

## Selling Before Resolution

You can sell your shares before the market resolves.

### How Selling Works
```
Your position: 320 shares in $96K-$97K
Current market price: $0.28 per share
If you sell now: 320 × $0.28 = $89.60

You locked in at $0.3125/share, so this is a small loss
But if you think the range won't hit, selling is smart
```

### Why Sell Early?
- Lock in profit if prices moved in your favor
- Cut losses if you changed your mind
- Free up capital for a better opportunity

### Selling Is Also Deterministic
```
Sell quote: 320 shares at $0.28 = $89.60
If you confirm, you receive exactly $89.60
This amount won't change after you confirm
```

---

## Summary: What "Deterministic" Really Means

| Event | Payout Impact |
|-------|---------------|
| Someone else bets on your range | None |
| Someone else bets on other ranges | None |
| Market liquidity changes | None |
| Time passes | None |
| Price feeds update | None |
| You sell early | You get quoted amount |
| Market resolves in your range | You get guaranteed payout |
| Market resolves outside your range | You get $0 |

**Your payout is determined the moment you bet. That's the power of deterministic payouts.**

---

## Why This Matters for Strategy

### 1. No Need to Monitor Post-Bet
Once you bet, you can close the app. Your payout is locked.

### 2. Easy Portfolio Tracking
You know exactly how much you could win across all positions.

### 3. Fair Early Bird Rewards
Getting in early matters—you get better odds for taking risk with less information.

### 4. True Position Ownership
Your shares are yours. They can even be transferred or traded.

---

## Next Steps

<table data-card-size="large" data-view="cards">
<thead><tr><th></th><th></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead>
<tbody>
<tr><td><strong>Market Types</strong></td><td>Different markets, same deterministic payouts</td><td><a href="/for-traders/market-types">market-types.md</a></td></tr>
<tr><td><strong>Strategies</strong></td><td>Use deterministic payouts to your advantage</td><td><a href="/for-traders/strategies">strategies.md</a></td></tr>
</tbody>
</table>
