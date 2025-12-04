---
title: "How to Place a Bet"
---

# How to Place a Bet

A complete guide to making your first prediction on Skepsis.

---

## Overview

Placing a bet on Skepsis involves four simple steps:

1. **Choose a market** — Find a prediction you have an opinion on
2. **Select your range** — Define where you think the outcome will land
3. **Review your quote** — See your exact odds and potential payout
4. **Confirm the bet** — Execute the transaction

Let's walk through each step.

---

## Step 1: Choose a Market

Browse available markets on the [Skepsis app](https://app.skepsis.market).

### What You'll See

Each market card shows:
- **Question:** What's being predicted
- **Current distribution:** Where the crowd thinks the answer is
- **Time remaining:** When the market resolves
- **Liquidity:** How much money is in the market

### Market Types

| Type | Example | Typical Duration |
|------|---------|------------------|
| **Price** | BTC/USD in 1 hour | Minutes to hours |
| **Weather** | Tomorrow's high temp | Hours to days |
| **Events** | Product release date | Days to months |

<Info>
**Start with short-duration markets** — You'll see results faster and learn the mechanics quickly.
</Note>

---

## Step 2: Select Your Range

This is where Skepsis differs from traditional betting.

### The Range Selector

When you open a market, you'll see a probability chart. Click and drag to select your range:

```
Your selected range: $96,000 - $97,500

         ▓▓▓▓▓▓▓▓▓▓▓▓▓
      ▓▓▓░░░░░░░░░░░░░▓▓▓
   ▓▓▓░░░░░░░░░░░░░░░░░░░▓▓▓
▓▓▓░░░░░░░░░░░░░░░░░░░░░░░░░▓▓▓
|----|----|----|----|----|----|
$94K $95K $96K $97K $98K $99K $100K
          └────────┘
          Your range
```

### Range Selection Tips

| Range Width | Odds | Risk Level |
|-------------|------|------------|
| Very narrow ($500) | 10-20x | 🔴 High risk |
| Moderate ($2,000) | 3-5x | 🟡 Medium risk |
| Wide ($5,000) | 1.5-2x | 🟢 Low risk |

**The trade-off:** Wider ranges are more likely to win but pay less. Narrow ranges pay more but are harder to hit.

---

## Step 3: Review Your Quote

Before confirming, you'll see a detailed quote:

```
┌─────────────────────────────────────┐
│  YOUR BET SUMMARY                    │
├─────────────────────────────────────┤
│  Range:        $96,000 - $97,500     │
│  Investment:   $100 USDC             │
│  Your Odds:    3.2x                  │
│                                      │
│  If you WIN:   $320 USDC             │
│  If you LOSE:  $0 (lose your $100)  │
│                                      │
│  Probability:  ~31%                  │
│  Expected Value: +$0.80              │
└─────────────────────────────────────┘
```

### Understanding the Quote

| Field | Meaning |
|-------|---------|
| **Range** | The outcome range you're betting on |
| **Investment** | How much USDC you're risking |
| **Your Odds** | Your multiplier if you win |
| **If you WIN** | Exact payout amount (guaranteed) |
| **If you LOSE** | You lose your investment |
| **Probability** | Market's current estimate of this range hitting |
| **Expected Value** | Probability × Payout - Investment |

<Note>
**Deterministic payouts:** Unlike traditional betting, your payout is locked in at bet time. It won't change regardless of future bets.
</Note>

---

## Step 4: Confirm the Bet

1. Click **"Place Bet"**
2. Your wallet will prompt you to sign the transaction
3. Review the transaction details
4. Click **"Approve"** in your wallet

### Transaction Details

You'll pay:
- **Bet amount:** Your USDC investment
- **Gas fee:** ~0.001 SUI (negligible)

### What Happens Next

1. ✅ Transaction confirmed on Sui blockchain
2. ✅ Your position is created
3. ✅ You can view it in "My Positions"
4. ⏳ Wait for market resolution

---

## After Placing Your Bet

### Track Your Position

Go to **"My Positions"** to see:
- All your active bets
- Current probability of each range
- Potential payouts
- Time until resolution

### Optional: Sell Early

You can sell your position before resolution:
- Click on your position
- Select **"Sell"**
- Review the quote (based on current market prices)
- Confirm the sale

<Warning>
**Selling early** gives you less than waiting for resolution if you win, but it lets you lock in partial profit or cut losses.
</Note>

### Claiming Winnings

After resolution:
1. Check if the outcome landed in your range
2. If yes, click **"Claim Winnings"**
3. USDC is transferred to your wallet instantly

---

## Example Walkthrough

### Scenario: BTC 1-Hour Market

**You believe:** Bitcoin will stay between $96K-$98K in the next hour.

1. **Open** the BTC 1-hour market
2. **Select** range: $96,000 - $98,000
3. **Enter** investment: $50 USDC
4. **Review** quote:
   - Odds: 2.1x
   - Potential payout: $105
   - Probability: ~48%
5. **Confirm** bet
6. **Wait** 1 hour
7. **Result:** BTC closes at $97,200
8. **Claim** your $105 USDC! 🎉

---

## Common Questions

### What if the outcome is exactly on my range boundary?

The lower bound is inclusive, upper bound is exclusive. So range $96,000-$97,000:
- $96,000.00 → ✅ In range
- $96,999.99 → ✅ In range
- $97,000.00 → ❌ Not in range

### Can I bet on multiple ranges?

Yes! You can place multiple bets on different ranges in the same market. This is a common hedging strategy.

### What happens if I lose connection during the bet?

If the transaction was signed, it will complete. Check "My Positions" to verify. If it wasn't signed, no USDC left your wallet.

---

## Next Steps

<table data-card-size="large" data-view="cards">
<thead><tr><th></th><th></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead>
<tbody>
<tr><td><strong>Understanding Ranges</strong></td><td>Deep dive into range selection strategy</td><td><a href="understanding-ranges.md">understanding-ranges.md</a></td></tr>
<tr><td><strong>Reading Odds</strong></td><td>How odds are calculated and what they mean</td><td><a href="reading-odds.md">reading-odds.md</a></td></tr>
</tbody>
</table>
