---
title: "The vault"
description: "One ERC-4626 vault seeds every market and recycles capital on resolution."
---

## One vault, every market

Most prediction markets fragment liquidity. Each market has its own pool, and a new market opens dead until someone seeds it. Skepsis pools all liquidity in a single ERC-4626 vault. The vault seeds every market the moment it is created, so a market is tradable on day one.

When a market resolves, its capital returns to the vault and redeploys to live markets. No pool sits idle. No market launches empty.

<Frame caption="One vault seeds every market and recycles capital on resolution.">
  <img src="/images/vault-recycle.svg" alt="LP deposits into one vault, which funds every market and recycles on resolution" />
</Frame>

## What liquidity providers get

- One deposit, exposure across every market, not one.
- Fees earned across all markets the vault backs.
- Capital that recycles on resolution instead of locking up.

## Bounded risk, guaranteed solvency

LMSR keeps the vault's exposure bounded and known. The pool balance is always at least the maximum possible payout, so every market is solvent on every trade. The alpha parameter sets the depth and bounds the worst-case loss on a market to a known fraction of the liquidity committed. See [risks and returns](/for-lps/risks-and-returns) and [economics](/how-it-works/economics).

[Alpha decay](/how-it-works/alpha-decay) adds a second layer: as a market nears resolution its liquidity thins, defending the vault against traders acting on late information.

<Note>
Liquidity is bootstrapped on testnet. Depth is limited and slippage is real on thin markets. Mainnet contracts exist; they are not deployed.
</Note>
