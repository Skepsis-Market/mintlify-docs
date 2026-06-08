---
title: "Risks and returns"
description: "What liquidity providers earn, and the bounded risk they take."
---

## What you earn

The vault earns the spread the LMSR captures on trading, plus fees, across every market it backs. One deposit, exposure across all markets, capital recycled on resolution. See [the vault](/for-lps/vault-overview).

## The risk

The vault is the counterparty to traders. On resolution it pays winning shares from the over-collateralized pool. If informed trading moves a market against the book, the vault can take a loss on that market. This is the risk you are paid for.

## What bounds it

- Solvency: LMSR keeps the pool at or above the maximum payout at all times.
- Bounded loss: the alpha parameter caps the worst-case loss on a market to a known fraction of the liquidity committed.
- Sniper defense: [alpha decay](/how-it-works/alpha-decay) thins the book toward resolution, limiting late-information losses.

## Honest limits

Liquidity is bootstrapped; depth is thin on new markets. The risk is real and bounded, not zero. Mainnet contracts exist; they are not deployed.
