---
title: "Economics"
description: "Where payouts come from, how the vault earns, and why it stays solvent."
---

## Where payouts come from

When you trade, the LMSR market takes the other side and collects your USDC into the market's pool. The pool is seeded by the vault and held at or above the maximum possible payout at all times, so the market can always pay every winning share. That is the solvency guarantee.

On resolution, the winning bucket is set from the Chainlink feed. Holders of a winning bucket claim a fixed amount per share. Collateral reserved for outcomes that can no longer happen is released as surplus.

## How the vault earns

The vault seeds every market and, on resolution, harvests the surplus and the market's residual capital back for reuse. Across a market, the vault's net is the spread the LMSR captured on trading, plus fees. Because one vault backs every market and recycles on resolution, the same capital earns across many markets instead of locking into one. See [the vault](/for-lps/vault-overview).

## Why it stays solvent

LMSR keeps the pool at or above the maximum possible payout at every point. A market cannot promise more than it can pay. The alpha parameter sets the depth and bounds the worst-case loss on a market to a known fraction of the liquidity committed. [Alpha decay](/how-it-works/alpha-decay) thins the book toward resolution, limiting late-information losses.

## The honest limits

- Liquidity is bootstrapped. Depth is limited on new and thin markets.
- The vault takes real, bounded risk. Fees and spread are the compensation for it.
- Mainnet contracts exist. They are not deployed.
