---
title: "How to Place a Bet"
---


A complete guide to making your first prediction on Skepsis.

<Tip>
Currently on testnet. Claim free USDC from the app to try it out — no real money needed.
</Tip>

---

## Overview

Placing a bet on Skepsis involves four simple steps:

1. **Choose a market.** Find a prediction you have an opinion on.
2. **Select your range.** Define where you think the outcome will land.
3. **Review your quote.** See your exact odds and potential payout.
4. **Confirm the bet.** Execute the transaction.

---

## Step 1: Choose a Market

Browse available markets on the [Skepsis app](https://alpha.skepsis.live/markets).

<Frame>
  <img src="/images/browse-markets.png" alt="Active market cards showing question, distribution, and time remaining" />
</Frame>

### What You'll See

Each market card shows:
- **Question:** What's being predicted
- **Current distribution:** Where the crowd thinks the answer is
- **Time remaining:** When the market resolves
- **Liquidity:** How much money is in the market

Markets cover price feeds, weather, events, and more. See [Market Types](/for-traders/market-types) for the full breakdown. Short-duration markets (e.g. 1-hour BTC) are a good place to start.

---

## Step 2: Select Your Range

This is where Skepsis differs from traditional betting. Instead of a simple "Yes/No", you define the exact outcome range you believe in.

### The Range Selector

When you open a market, you'll see a probability chart. Click and drag to select your range:

<Frame>
  <img src="/images/range-selection.gif" alt="Interactive range selection on the probability chart" />
</Frame>

Wider ranges are more likely to win but pay less. Narrow ranges pay more but are harder to hit. For strategy details, see [Understanding Ranges](/for-traders/understanding-ranges).

---

## Step 3: Review Your Quote

Before confirming, you'll see a detailed quote on the right side of the screen.

<Frame>
  <img src="/images/bet-slip.png" alt="Bet slip showing range, amount, probability, and potential payout" />
</Frame>

### Understanding the Quote

| Field | Meaning |
|-------|---------|
| **Min/Max Price** | The specific range you are betting on (e.g., \$93.3K - \$95.1K). |
| **Your Bet** | The amount of USDC you are risking (e.g., 100 USDC). |
| **Win Probability** | The market's current estimated chance of the outcome landing in your range (e.g., 53.67%). |
| **IF YOU WIN** | The total amount you will receive if you are correct (e.g., \$204.75). |
| **Return** | Your multiplier (e.g., 2.0x). This is your payout divided by your bet amount. |

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
- **Actual Cost:** The exact cost to buy the position. This is often slightly less than your input amount (e.g., if you input 100 USDC, the actual cost might be 99.50 USDC). The unused difference never leaves your wallet.
- **Network fee:** ~0.01 AVAX (negligible)

<Note>
**Why is the cost lower?** 
Due to the way our market maker (LMSR) calculates prices, we can't always match your input amount exactly down to the cent. We buy as much as possible up to your limit. **Any unused USDC never leaves your wallet.**
</Note>

### What Happens Next

1. Transaction confirmed on Avalanche
2. Your position is created
3. You can view it in "My Positions"
4. Wait for market resolution

---

## After Placing Your Bet

### Track Your Position

Go to **"Portfolio"** to see all your positions (active, sold, claimable, and lost) along with stats like total PNL, win rate, and realized gains.

<Frame>
  <img src="/images/portfolio.png" alt="Portfolio page showing positions and performance stats" />
</Frame>

### Optional: Sell Early

You can sell your position before resolution:
- Click on your position
- Select **"Sell"**
- Review the quote (based on current market prices)
- Confirm the sale

<Warning>
**Selling early** gives you less than waiting for resolution if you win, but it lets you lock in partial profit or cut losses.
</Warning>

### Claiming Winnings

After resolution:
1. Check if the outcome landed in your range
2. If yes, click **"Claim Winnings"**
3. USDC is transferred to your wallet instantly

---

## Example Walkthrough

### Scenario: BTC 1-Hour Market

**You believe:** Bitcoin will stay between \$96K-\$98K in the next hour.

1. **Open** the BTC 1-hour market
2. **Select** range: \$96,000 - \$98,000
3. **Enter** investment: \$50 USDC
4. **Review** quote:
   - Odds: 2.1x
   - Potential payout: \$105
   - Probability: ~48%
5. **Confirm** bet
6. **Wait** 1 hour
7. **Result:** BTC closes at \$97,200
8. **Claim** your \$105 USDC

---

## Common Questions

**Range boundaries:** Lower bound is inclusive, upper bound is exclusive. If your range is \$96,000-\$97,000, a result of exactly \$97,000 is *not* in range.

**Multiple ranges:** Yes, you can bet on multiple ranges in the same market.

**Lost connection mid-bet:** If you signed the transaction, it will complete on-chain. Check "My Positions" to verify. If you didn't sign, nothing left your wallet.

For more, see the [FAQ](/resources/faq).
