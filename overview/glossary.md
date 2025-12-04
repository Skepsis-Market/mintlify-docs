---
title: "Glossary"
---


Quick reference for terms you'll encounter on Skepsis.

---

## Core Concepts

### Range
The span of values you're betting on. For example, in a Bitcoin market, your range might be "$95,000 - $97,000". If the final price lands anywhere within your range, you win.

### Bucket / Spread
The smallest unit of a range. Markets are divided into discrete buckets (e.g., each $100 increment for BTC). When you select a range, you're actually selecting multiple adjacent buckets.

### Probability Distribution
A visualization showing how likely each outcome range is according to current market beliefs. Peaks indicate high-probability areas; valleys indicate low-probability areas (and potentially better odds).

### Resolution
The moment when the actual outcome is determined and reported. After resolution, winning positions can claim their payouts.

---

## Trading Terms

### Position
Your stake in a market. When you bet on a range, you receive a position representing your potential claim to winnings.

### Odds / Multiplier
How much you'll win relative to your bet. "5x odds" means a $100 bet wins $500 if correct.

### Quote
The instant price calculation showing what your bet will cost and what you'll win. Quotes are generated in real-time based on current market state.

### Deterministic Payout
Your payout is fixed the moment you bet. Unlike traditional betting where payouts can change, Skepsis guarantees your exact winnings upfront.

### Shares
Internal accounting units representing your position size. Each share is worth exactly $1 if your range wins, $0 if it loses.

---

## Market Structure

### Market
A single prediction question with a defined outcome range and resolution time. Example: "BTC price at 5:00 PM UTC on December 15th"

### Outcome Range
The full span of possible values for a market. For a BTC market, this might be $80,000 - $120,000.

### Bucket Count
How many discrete segments the outcome range is divided into. More buckets = finer granularity but potentially lower liquidity per bucket.

### Liquidity
The total funds available in a market for trading. Higher liquidity = tighter spreads and less price impact.

### Pool Balance
The total USDC held by the market smart contract, used to pay winners.

---

## Pricing & Economics

### LMSR (Logarithmic Market Scoring Rule)
The mathematical algorithm that determines prices. It ensures:
- Always-available liquidity
- Prices that reflect current beliefs
- Bounded risk for the protocol

### Alpha (α) / Liquidity Parameter
A value that controls how sensitive prices are to trades. Higher alpha = prices move less per trade = more stable but lower profit potential for early traders.

### Spread
The difference between what you pay to buy and what you'd receive to sell immediately. Think of it as the market's "fee" embedded in prices.

### Slippage
The difference between the quoted price and the actual execution price. On Skepsis, slippage is minimal due to LMSR's mathematical properties.

---

## Resolution Terms

### Oracle
The trusted data source that reports the actual outcome. For price markets, this might be a price feed like Pyth or Chainlink.

### Resolution Time
The predetermined moment when the outcome is measured and winners are determined.

### Winning Bucket
The bucket (or range) where the actual outcome landed. All positions containing this bucket win.

### Claim
The action of withdrawing your winnings after resolution. Winners receive $1 per share they hold in winning buckets.

---

## Position Management

### Buy
Opening a new position or adding to an existing one by paying USDC to receive shares.

### Sell
Closing part or all of your position before resolution by returning shares for USDC. The amount you receive depends on current market prices.

### Total Invested
The sum of USDC you've put into positions across all your bets in a market.

### Potential Payout
The maximum amount you could win if all your selected ranges contain the winning outcome.

---

## Technical Terms

### Sui
The layer-1 blockchain Skepsis is built on. Known for high speed, low fees, and object-based architecture.

### USDC
The stablecoin used for betting on Skepsis. 1 USDC ≈ $1 USD.

### Transaction
An on-chain action like placing a bet or claiming winnings. Each transaction requires a small gas fee paid in SUI.

### Smart Contract
Self-executing code on the blockchain that manages markets, positions, and payouts. Skepsis contracts are open-source and auditable.

---

## Quick Reference Table

| Term | Simple Definition |
|------|-------------------|
| Range | What you're betting on (e.g., "$95K-$97K") |
| Odds | Your multiplier if you win (e.g., "5x") |
| Position | Your stake / bet |
| Resolution | When the winner is decided |
| Claim | Withdrawing your winnings |
| LMSR | The math that sets prices |
| Bucket | Smallest betting unit |
| Liquidity | Money in the market pool |

---

## Still Confused?

- Check our [FAQ](/faq) for common questions
- Join [Telegram](https://t.me/skepsis_market) to ask the community
- Follow [@skepsis_market](https://x.com/skepsis_market) for updates
