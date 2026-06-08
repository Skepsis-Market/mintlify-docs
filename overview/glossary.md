---
title: "Glossary"
description: "The terms used across Skepsis, defined briefly."
---

**Continuous-outcome market.** A market that prices the range a number lands in, not a yes or no.

**Range, time, options.** The three market shapes. Range: where a number lands. Time: when a level is reached. Options: one of N named outcomes, priced on one shared curve.

**Bucket.** One interval of the outcome range. Markets are split into buckets; you take a position on one or more.

**LMSR.** Logarithmic Market Scoring Rule. The pricing rule that turns shares held in each bucket into a price, on one continuous curve.

**Alpha.** The LMSR liquidity parameter. Higher alpha means deeper liquidity and smaller price impact per trade.

**Alpha decay.** A scheduled reduction of alpha over a market's life, from an initial value to a floor. It thins the book near resolution to defend liquidity providers against late-information snipers.

**Basis risk.** The gap between the outcome you priced and the outcome that paid. Binary markets carry it; Skepsis is built to remove it.

**Uniform prior.** The starting state where every bucket is equally likely. Payoff math is quoted at uniform prior: payoff = N / k for k of N buckets.

**Vault.** A single ERC-4626 contract that seeds every market and recycles capital on resolution.

**Position.** Your holding in a market, issued as an ERC-1155 token.

**Resolution.** Settlement of a market from a Chainlink numerical feed at a set time.

**Curated.** Every market is reviewed and listed by the team. Skepsis is not permissionless.
