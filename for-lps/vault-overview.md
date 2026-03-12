---
title: "The Vault"
---


Think of the Vault as a shared war chest that funds every prediction market on Skepsis.

---

## The Old Way vs The Vault Way

### Without a Vault (How Most Protocols Work)

Imagine you want to provide liquidity to prediction markets. Here's what it looks like:

```
Market 1 (BTC price): You deposit $5,000
Market 2 (ETH price): You deposit $3,000
Market 3 (Weather):   You deposit $2,000

Your $10,000 is split across 3 markets.
Market 1 resolves → Capital stuck until you manually redeploy.
Market 4 launches → No capital left. You miss it.
```

You're a fund manager with no fund — just a bunch of scattered bets.

### With the Vault

```
You deposit $10,000 into the Vault. Done.

Vault deploys $4,000 → Market 1
Vault deploys $3,000 → Market 2
Vault deploys $3,000 → Market 3

Market 1 resolves → Capital returns to Vault automatically
Vault deploys $4,000 → Market 4 (new!)

Your money never sleeps.
```

**One deposit. Every market. Automatic recycling.**

---

## How It Works

### Deposit

You deposit USDC into the Vault and receive vault shares in return. These shares represent your slice of the entire pool.

```
You deposit: 10,000 USDC
Vault total: 100,000 USDC
Your share: 10%

Every fee earned, every market funded — you get 10%.
```

### Capital Deployment

The Vault pushes capital into active markets as they're created. Each market gets enough USDC to power its LMSR pricing — this is what makes "always-on liquidity" possible for traders.

```
New BTC market created → Vault sends $5,000
New weather market created → Vault sends $2,000

No single market gets more than 20% of the Vault.
(Safety first.)
```

### Revenue

When traders bet, fees are split:

```
Trader pays 0.3% fee on every trade
├── Part goes to the protocol
└── Part flows back to the Vault (your share)
```

When markets resolve, any leftover pool balance (after paying winners) returns to the Vault. If traders collectively overbought losing ranges, the Vault profits. If the winning range was popular, the Vault might take a small hit — but that's bounded by the math.

### Withdrawal

Want your money back? You request a withdrawal and join the queue.

```
You request: Withdraw 5,000 USDC
Queue position: #3

As markets resolve and capital returns,
the queue processes in order (FIFO).

Capital returns → Your withdrawal is filled → USDC in your wallet.
```

Why a queue? Because your capital is deployed in active markets. We can't yank it mid-trade — that would break the solvency guarantees for traders. The queue ensures everyone gets paid fairly.

---

## What Can Go Wrong?

Let's be honest about the risks.

### The Vault Can Lose Money

If many markets resolve with popular winning ranges, the Vault pays out more than it collects. This is the LP risk — it's the price of being the house.

**But it's bounded.** The LMSR math guarantees that the maximum loss per market is capped. No single market can blow up the entire Vault.

```
Per-market max loss: α × ln(bucketCount)

For a typical market with α = 3,333 and 16 buckets:
Max loss ≈ $9,240

On a $100,000 Vault, that's 9.2% — painful but survivable.
```

### Multiple Markets Can Lose Simultaneously

The 20% cap per market limits concentration. Even if 5 markets all go badly, the Vault survives.

### The Queue Means You Wait

Your withdrawal isn't instant. If all capital is deployed, you wait until markets resolve. During volatile periods, this could take days.

---

## Who Should LP?

The Vault is designed for people who:

- Believe prediction markets will see consistent trading volume
- Want passive yield from fees without picking individual markets
- Understand LP risk (you can lose capital, though it's bounded)
- Have a time horizon longer than a single market cycle

It's **not** for people who want instant liquidity or zero-risk yield.

---

## The Numbers That Matter

| Metric | What It Means |
|--------|---------------|
| **Vault NAV** | Total value of all USDC (liquid + deployed) |
| **Your share %** | Your slice of the Vault |
| **Fee APY** | Annualized return from trading fees |
| **Utilization** | % of Vault capital currently in active markets |
| **Queue depth** | How many USDC in withdrawal requests ahead of you |

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
    Your capital is now working across every market on Skepsis.
  </Step>
</Steps>

---

## Next Steps

<table data-card-size="large" data-view="cards">
<thead><tr><th></th><th></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead>
<tbody>
<tr><td><strong>Risks & Returns</strong></td><td>Deep dive into LP economics</td><td><a href="/for-lps/risks-and-returns">Risks & Returns</a></td></tr>
<tr><td><strong>Economics</strong></td><td>Where does the money flow?</td><td><a href="/how-it-works/economics">Economics</a></td></tr>
</tbody>
</table>
