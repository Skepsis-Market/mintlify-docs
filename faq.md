---
title: "Frequently Asked Questions"
---


Quick answers to common questions about Skepsis.

---

## About Testnet

### Is this real money?

**No.** Skepsis is currently on **Avalanche Fuji Testnet**. All USDC used is test currency with no real value.

### How do I get test USDC?

1. Go to [alpha.skepsis.live](https://alpha.skepsis.live/markets)
2. Sign in with Privy or connect your EVM wallet
3. Click **"Claim USDC"** in the app
4. Receive free test tokens instantly

### Do I need to pay gas fees?

If you sign in with Privy (email/social), gas is sponsored. If you connect an EVM wallet, grab free test AVAX from the [Avalanche Faucet](https://faucet.avax.network/).

### Do I need a crypto wallet?

No. You can sign in with Privy (email/social) and it creates an embedded wallet for you. Or connect your own EVM wallet if you prefer full control.

### When will mainnet launch?

No date announced yet. Join our [Telegram](https://t.me/skepsis_market) or follow [@skepsis_market](https://x.com/skepsis_market) for updates.

---

## Getting Started

### What is Skepsis?

Skepsis is a **continuous outcome prediction market** built on Avalanche. Instead of betting yes/no on binary questions, you bet on **ranges** where you think an outcome will land.

### How is this different from Polymarket?

Polymarket uses binary (yes/no) markets. Skepsis uses continuous markets where you select ranges. This lets you express more nuanced predictions and see full probability distributions.

### What do I need to get started?

An email account or an EVM wallet. On testnet everything is free — test USDC from the faucet, sponsored gas. See the [Quick Start](/overview/quick-start) if you want a walkthrough.

---

## Trading

### How do I place a bet?

1. Choose a market
2. Select your range (where you think the outcome will land)
3. Enter your bet amount
4. Review your quote (see exact payout)
5. Confirm the transaction

### What happens to my money when I bet?

Your USDC goes into the market's liquidity pool. In return, you receive "shares" representing your position. If the outcome lands in your range, each share is worth \$1. If not, they're worth \$0.

### Can I sell my position before resolution?

Yes! You can sell your shares at any time before the market closes. The amount you receive depends on current market prices.

### What if I forget to claim my winnings?

You have **90 days** after resolution to claim. After that, unclaimed funds go to the protocol treasury.

---

## Odds & Payouts

### How are odds calculated?

Odds are set by the [LMSR algorithm](/how-it-works/lmsr-for-humans). More bets on a range push that range's probability up and its odds down. Less-bet ranges stay cheap.

### What does "3.5x odds" mean?

If you bet \$100 at 3.5x odds:
- **If you win:** You receive \$350
- **If you lose:** You receive \$0

The multiplier tells you your payout relative to your bet.

### Are payouts guaranteed?

**Yes.** Your payout is locked the moment you place your bet. Future bets by others don't change it. See [Deterministic Payouts](/for-traders/deterministic-payouts) for the details.

### What if the outcome is exactly on my range boundary?

Ranges are lower-inclusive, upper-exclusive. So for a \$96,000–\$97,000 range, \$96,000.00 pays out but \$97,000.00 belongs to the next bucket.

---

## Markets

### What types of markets are available?

Price markets (BTC, ETH, etc.), date markets (product launches, event dates), and measurement markets (weather, economic indicators). See [Market Types](/for-traders/market-types) for the full breakdown.

### Who creates markets?

Currently, markets are created by the Skepsis team and approved creators. Permissionless market creation is on the roadmap.

### What determines the outcome?

Oracles report the actual outcome — Pyth/Chainlink for price feeds, NOAA for weather, official announcements for events. Details in [Trust & Resolution](/how-it-works/trust-and-resolution).

### What if the oracle is wrong?

There's a **24-hour dispute window** after resolution. If you have evidence the outcome was reported incorrectly, you can submit a dispute.

---

## Fees & Costs

### What are the fees?

0.3%–1% per trade depending on market risk category, plus ~\$0.01 gas (AVAX).

### Where do fees go?

40% to LPs, 30% to market creators, 30% to the protocol treasury.

---

## Technical

### Is Skepsis decentralized?

**Mostly.** The smart contracts are deployed on Avalanche and handle all trading/settlement logic. Market creation and some parameters are currently controlled by the team.

### Is the code open source?

Yes! Our smart contracts are open source and auditable.

### What blockchain is Skepsis on?

Skepsis is built on **Avalanche**, a high-performance blockchain with fast finality, low fees, and full EVM compatibility.

### Do I need to KYC?

No. Skepsis is wallet-based with no identity verification required.

---

## Safety

### Can the market run out of money?

No. The **LMSR algorithm** mathematically guarantees that the pool can always pay all winners. The system remains solvent under all conditions.

### What if Skepsis disappears?

Your funds are in smart contracts on Avalanche, not held by Skepsis. As long as the blockchain exists, your positions exist.

### Are smart contracts audited?

[Coming soon - link to audits]

---

## Problems & Support

### My transaction failed. What happened?

Common causes:
- Insufficient AVAX for gas
- Insufficient USDC for bet
- Market already closed
- Network congestion

Check your wallet and try again. If issues persist, reach out on Telegram.

### I won but can't claim. What do I do?

1. Make sure the market has resolved
2. Check that the outcome was in your range
3. Ensure you have AVAX for gas
4. Try refreshing and reconnecting wallet

If still stuck, contact support on Telegram.

### Where can I get help?

- **Telegram:** [Join our server](https://t.me/skepsis_market)
- **@X:** [@skepsis_market](https://x.com/skepsis_market)
- **Email:** team@skepsis.live

---

## More Questions?

[Telegram](https://t.me/skepsis_market)

---

<Info>
Claude has been a friendly neighbour who helped us build these docs. For feedback or corrections, reach out on Telegram: [@defigonn](https://t.me/defigonn).
</Info>
