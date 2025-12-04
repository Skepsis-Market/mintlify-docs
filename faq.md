---
title: "Frequently Asked Questions"
---

# Frequently Asked Questions

Quick answers to common questions about Skepsis.

---

## Getting Started

### What is Skepsis?

Skepsis is a **continuous outcome prediction market** built on Sui blockchain. Instead of betting yes/no on binary questions, you bet on **ranges** where you think an outcome will land.

### How is this different from Polymarket?

Polymarket uses binary (yes/no) markets. Skepsis uses continuous markets where you select ranges. This lets you express more nuanced predictions and see full probability distributions.

[Learn more: Skepsis vs Polymarket →](/comparisons/vs-polymarket)

### What do I need to get started?

1. A Sui wallet ([Sui Wallet](https://chrome.google.com/webstore/detail/sui-wallet/opcgpfmipidbgpenhmajoajpbobppdil) or [Suiet](https://suiet.app/))
2. Some USDC on Sui network
3. A small amount of SUI for gas fees

[Full guide: Quick Start →](/overview/quick-start)

---

## Trading

### How do I place a bet?

1. Choose a market
2. Select your range (where you think the outcome will land)
3. Enter your bet amount
4. Review your quote (see exact payout)
5. Confirm the transaction

[Detailed guide: How to Place a Bet →](/for-traders/how-to-place-a-bet)

### What happens to my money when I bet?

Your USDC goes into the market's liquidity pool. In return, you receive "shares" representing your position. If the outcome lands in your range, each share is worth $1. If not, they're worth $0.

### Can I sell my position before resolution?

Yes! You can sell your shares at any time before the market closes. The amount you receive depends on current market prices.

### What if I forget to claim my winnings?

You have **90 days** after resolution to claim. After that, unclaimed funds go to the protocol treasury. Set a reminder!

---

## Odds & Payouts

### How are odds calculated?

Odds are determined by the **LMSR algorithm** based on current betting activity:

- More bets on a range → Higher probability → Lower odds
- Fewer bets on a range → Lower probability → Higher odds

[Learn more: LMSR Explained →](/how-it-works/lmsr-for-humans)

### What does "3.5x odds" mean?

If you bet $100 at 3.5x odds:
- **If you win:** You receive $350
- **If you lose:** You receive $0

The multiplier tells you your payout relative to your bet.

### Are payouts guaranteed?

**Yes!** This is called "deterministic payouts." The moment you place your bet, your potential payout is locked in. Future bets by others don't change your payout.

[Learn more: Deterministic Payouts →](/for-traders/deterministic-payouts)

### What if the outcome is exactly on my range boundary?

Boundaries are **lower-inclusive, upper-exclusive**:
- Range: $96,000 - $97,000
- $96,000.00 → ✅ In range
- $96,999.99 → ✅ In range
- $97,000.00 → ❌ Not in range (belongs to next bucket)

---

## Markets

### What types of markets are available?

- **Price markets:** BTC, ETH, and other asset prices
- **Date markets:** Product launches, event dates
- **Measurement markets:** Weather, economic indicators

[Learn more: Market Types →](/for-traders/market-types)

### Who creates markets?

Currently, markets are created by the Skepsis team and approved creators. Permissionless market creation is on the roadmap.

### What determines the outcome?

**Oracles** report the actual outcome:
- Price markets → Pyth/Chainlink price feeds
- Weather markets → NOAA official data
- Event markets → Official announcements

[Learn more: Trust & Resolution →](/how-it-works/trust-and-resolution)

### What if the oracle is wrong?

There's a **24-hour dispute window** after resolution. If you have evidence the outcome was reported incorrectly, you can submit a dispute.

---

## Fees & Costs

### What are the fees?

- **Trading fee:** 0.3% of each bet
- **Gas fee:** ~$0.001 per transaction (paid in SUI)

### Where do fees go?

Fees are split between:
- Protocol treasury (30%)
- Market creators (30%)
- Liquidity providers (40%)

---

## Technical

### Is Skepsis decentralized?

**Mostly.** The smart contracts are deployed on Sui blockchain and handle all trading/settlement logic. Market creation and some parameters are currently controlled by the team.

### Is the code open source?

Yes! Our smart contracts are open source and auditable.

### What blockchain is Skepsis on?

Skepsis is built on **Sui**, a high-performance Layer 1 blockchain with sub-second finality and low fees.

### Do I need to KYC?

No. Skepsis is wallet-based with no identity verification required.

---

## Safety

### Can the market run out of money?

No. The **LMSR algorithm** mathematically guarantees that the pool can always pay all winners. The system is designed to remain solvent under all conditions.

### What if Skepsis disappears?

Your funds are in smart contracts on Sui blockchain, not held by Skepsis company. As long as the blockchain exists, your positions exist.

### Are smart contracts audited?

[Coming soon - link to audits]

---

## Problems & Support

### My transaction failed. What happened?

Common causes:
- Insufficient SUI for gas
- Insufficient USDC for bet
- Market already closed
- Network congestion

Check your wallet and try again. If issues persist, reach out on Discord.

### I won but can't claim. What do I do?

1. Make sure the market has resolved
2. Check that the outcome was in your range
3. Ensure you have SUI for gas
4. Try refreshing and reconnecting wallet

If still stuck, contact support on Discord.

### Where can I get help?

- **Discord:** [Join our server](https://t.me/skepsis_market)
- **Twitter:** [@SkepsisMarket](https://x.com/skepsis_market)
- **Email:** support@skepsis.market

---

## More Questions?

Can't find your answer? Ask in our [Discord](https://t.me/skepsis_market) — the community is helpful!

---

## Start Predicting

<Note>
**Ready to try it?** [Launch Skepsis →](https://beta.skepsis.live)
</Note>
