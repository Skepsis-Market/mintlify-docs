---
title: "The Vault"
---


The Vault is a single pool of USDC that backs every prediction market on Skepsis. Deposit once, LP across all markets, and capital automatically recycles as markets resolve.

---

## Why a Vault Instead of Per-Market LPing

On order-book prediction markets, tail ranges have no liquidity because nobody's willing to make a market there. LMSR doesn't need a counterparty — it prices every outcome algorithmically — but it does need capital behind it. The Vault provides that capital across all ranges and all markets from a single pool, so LPs don't have to pick individual markets or manually redeploy after resolution.

---

## How It Works

### Deposit

Deposit USDC, receive vault shares representing your pro-rata slice of the pool. Your share entitles you to a proportional cut of all fee revenue and market P&L.

### Capital Deployment

The Vault seeds each new market with enough USDC to power its LMSR pricing. No single market gets more than 20% of the Vault. When a market resolves, deployed capital (minus payouts to winners) returns to the pool automatically.

### Revenue

LPs earn from three sources: trading fees (0.3%-1% per trade, split between protocol and Vault), LMSR convexity spread, and residual pool balance after winners are paid. See [Risks & Returns](/for-lps/risks-and-returns) for details.

### Withdrawal

Withdrawals are queue-based (FIFO). Because capital is deployed in active markets, pulling it mid-trade would break solvency guarantees. As markets resolve and capital returns, the queue processes in order.

---

## Risks

Per-market LP loss is bounded at `α * ln(bucketCount)`. For a typical market (alpha = 3,333 USDC, 16 buckets), that's ~$9,240 max. The 20% per-market cap limits concentration risk — even correlated losses across several markets won't drain the Vault.

Withdrawals are not instant. If capital is fully deployed, you wait until markets resolve. During volatile periods this could take days.

---

## Who Should LP?

LPs who want passive, diversified exposure to prediction market fee flow without picking individual markets. You need a time horizon longer than a single market cycle, and you need to be comfortable with bounded but real downside risk. Not suitable if you need instant liquidity.

---

## Quick Start

<Steps>
  <Step title="Connect Wallet">
    Go to [alpha.skepsis.live](https://alpha.skepsis.live) and connect via Privy or your EVM wallet.
  </Step>
  <Step title="Navigate to Vault">
    Find the Vault section in the app.
  </Step>
  <Step title="Deposit USDC">
    Enter the amount you want to deposit. Receive vault shares.
  </Step>
  <Step title="Earn">
    Your capital is now deployed across every market on Skepsis.
  </Step>
</Steps>

<Frame>
  <img src="/images/vault-overview.png" alt="Vault overview showing deposit interface and earnings" />
</Frame>
*The Vault dashboard: deposit, track shares, and monitor earnings*

<Frame>
  <img src="/images/seed-overview.png" alt="Seed overview showing capital deployed across markets" />
</Frame>
*See how your capital is deployed across active markets*

