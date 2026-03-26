---
title: "Glossary"
---


Quick reference for terms used on Skepsis.

---

## Core Concepts

### Range
The span of values you're betting on (e.g., "$95,000 - $97,000"). If the outcome lands anywhere in your range, you win.

### Bucket
The smallest unit of a range. Markets are divided into discrete buckets (e.g., each $100 increment). Your selected range is a set of adjacent buckets.

### Probability Distribution
How likely each outcome range is according to current market pricing. Peaks = high probability, valleys = potentially better odds.

### Resolution
When the actual outcome is determined and reported. After resolution, winning positions can claim payouts.

---

## Trading Terms

### Position
Your stake in a market — received when you bet on a range.

### Odds / Multiplier
How much you win relative to your bet. 5x odds means $100 wins $500 if correct.

### Quote
Real-time price calculation showing cost and potential payout for a bet, based on current market state.

### Deterministic Payout
Your payout is fixed at the moment you bet. No post-trade payout changes.

### Shares
Internal units representing position size. Each share pays $1 if your range wins, $0 if it loses.

---

## Market Structure

### Market
A prediction question with a defined outcome range and resolution time.

### Outcome Range
The full span of possible values (e.g., $80,000 - $120,000 for a BTC market).

### Bucket Count
How many segments the outcome range is divided into. More buckets = finer granularity but lower liquidity per bucket.

### Liquidity
Total funds available for trading. Higher liquidity = less price impact.

### Pool Balance
Total USDC held by the market contract, used to pay winners.

---

## Pricing & Economics

### LMSR (Logarithmic Market Scoring Rule)
The pricing algorithm. Guarantees always-available liquidity, prices reflecting beliefs, and bounded protocol risk.

### Alpha (a) / Liquidity Parameter
Controls price sensitivity to trades. Higher alpha = prices move less per trade.

### Spread
Difference between buy and immediate-sell price. The market's embedded fee.

### Slippage
Difference between quoted price and execution price. Minimal on Skepsis due to LMSR's properties.

---

## Resolution Terms

### Oracle
Trusted data source reporting the actual outcome (e.g., Pyth or Chainlink for price feeds).

### Resolution Time
The predetermined moment when the outcome is measured.

### Winning Bucket
The bucket where the actual outcome landed. All positions containing this bucket win.

### Claim
Withdrawing winnings after resolution. Winners receive $1 per share in winning buckets.

---

## Position Management

### Buy
Open or add to a position by paying USDC to receive shares.

### Sell
Close part or all of a position before resolution by returning shares for USDC. Amount received depends on current market prices.

### Total Invested
Sum of USDC across all your bets in a market.

### Potential Payout
Maximum amount you win if your selected ranges contain the outcome.

---

## Technical Terms

### Avalanche
The blockchain Skepsis runs on. Fast finality, low fees, EVM-compatible.

### USDC
Stablecoin used for betting. 1 USDC ~ $1.

### Transaction
An on-chain action (placing a bet, claiming winnings). Requires a small gas fee in AVAX.

### Smart Contract
On-chain code managing markets, positions, and payouts. Skepsis contracts are open-source.

### Vault
ERC-4626 pool where LPs deposit USDC to seed markets. Capital deploys across markets and recycles as they resolve. LPs earn trading fees.

### Alpha Decay
Gradual decrease of the liquidity parameter over a market's lifetime, tightening spreads as the market matures.

### Position NFT
Your bet is an ERC-1155 token — transferable, composable, and self-custodied.

---

## See Also

- [FAQ](/faq)
- [Telegram](https://t.me/skepsis_market)
- [@skepsis_market](https://x.com/skepsis_market)
