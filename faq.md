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

**It depends on how you sign in:**

| Sign-in Method | Gas Fees |
|----------------|----------|
| **Privy (email/social)** | Sponsored (we pay for you) |
| **EVM Wallet** | Get free test AVAX from [Avalanche Faucet](https://faucet.avax.network/) |

### Do I need a crypto wallet?

**Not necessarily.** You have two options:

| Option | Best For |
|--------|----------|
| **Sign in with Privy** | New to crypto, instant access, gas sponsored |
| **Connect EVM Wallet** | Crypto natives, full control, need test AVAX for gas |

Both options work identically. Privy creates an embedded wallet linked to your account, no extensions needed.

### When will mainnet launch?

No date announced yet. Join our [Telegram](https://t.me/skepsis_market) or follow [@skepsis_market](https://x.com/skepsis_market) for updates.

---

## Getting Started

### What is Skepsis?

Skepsis is a **continuous outcome prediction market** built on Avalanche. Instead of betting yes/no on binary questions, you bet on **ranges** where you think an outcome will land.

### How is this different from Polymarket?

Polymarket uses binary (yes/no) markets. Skepsis uses continuous markets where you select ranges. This lets you express more nuanced predictions and see full probability distributions.

[Learn more: Skepsis vs Binary Markets →](/comparisons/vs-binary-markets)

### What do I need to get started?

**Just an email account**, or an EVM wallet if you prefer.

On testnet:
- Free test USDC from faucet
- No gas fees (we sponsor them)
- No real money required

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

Your USDC goes into the market's liquidity pool. In return, you receive "shares" representing your position. If the outcome lands in your range, each share is worth \$1. If not, they're worth \$0.

### Can I sell my position before resolution?

Yes! You can sell your shares at any time before the market closes. The amount you receive depends on current market prices.

### What if I forget to claim my winnings?

You have **90 days** after resolution to claim. After that, unclaimed funds go to the protocol treasury.

---

## Odds & Payouts

### How are odds calculated?

Odds are determined by the **LMSR algorithm** based on current betting activity:

- More bets on a range = higher probability, lower odds
- Fewer bets on a range = lower probability, higher odds

[Learn more: LMSR Explained →](/how-it-works/lmsr-for-humans)

### What does "3.5x odds" mean?

If you bet \$100 at 3.5x odds:
- **If you win:** You receive \$350
- **If you lose:** You receive \$0

The multiplier tells you your payout relative to your bet.

### Are payouts guaranteed?

**Yes.** This is called "deterministic payouts." The moment you place your bet, your potential payout is locked in. Future bets by others don't change your payout.

[Learn more: Deterministic Payouts →](/for-traders/deterministic-payouts)

### What if the outcome is exactly on my range boundary?

Boundaries are **lower-inclusive, upper-exclusive**:
- Range: \$96,000 - \$97,000
- \$96,000.00: in range
- \$96,999.99: in range
- \$97,000.00: not in range (belongs to next bucket)

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
- Price markets: Pyth/Chainlink price feeds
- Weather markets: NOAA official data
- Event markets: official announcements

[Learn more: Trust & Resolution →](/how-it-works/trust-and-resolution)

### What if the oracle is wrong?

There's a **24-hour dispute window** after resolution. If you have evidence the outcome was reported incorrectly, you can submit a dispute.

---

## Fees & Costs

### What are the fees?

- **Trading fee:** 0.3%-1% per trade (varies by market risk category)
- **Gas fee:** ~\$0.01 per transaction (paid in AVAX)

### Where do fees go?

Fees are split between:
- Protocol treasury (30%)
- Market creators (30%)
- Liquidity providers (40%)

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

Can't find your answer? Ask in our [Telegram](https://t.me/skepsis_market).

---

## Start Predicting

<Note>
[Launch Skepsis →](https://alpha.skepsis.live/markets)
</Note>

---

<Info>
Claude has been a friendly neighbour who helped us build these docs. For feedback or corrections, reach out on Telegram: [@defigonn](https://t.me/defigonn).
</Info>
