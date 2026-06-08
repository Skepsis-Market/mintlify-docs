---
title: "Trust and resolution"
description: "How markets settle, and why Skepsis is curated."
---

## Resolution

Every market resolves from a named Chainlink feed at a set time. The outcome is numerical and the resolution time is fixed when the market is created, so settlement is mechanical: the feed reports, the contract settles, positions pay out.

No discretionary judging. No dispute desk deciding what happened. The oracle and the clock decide.

## Curated, not permissionless

Not anyone can list a market. Every market on Skepsis is reviewed and listed by the team, against a named feed and a clear resolution rule. Permissionless listing is the largest unbounded-risk surface in this category. Curation removes it, and the customers who hedge real exposure want it as a trust signal.

## What you can verify

- The resolving feed and the resolution time are set on-chain at creation.
- Pricing is LMSR over a bucket tree; the pool is always at least the maximum payout.
- Positions are ERC-1155 tokens; the vault is an ERC-4626 contract on Arbitrum Sepolia.

## Honest limit

Resolution waits on the oracle's time gate. A market settles when its feed reports at the scheduled time, not before.
