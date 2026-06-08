---
title: "Skepsis vs binary markets"
description: "How Skepsis differs from yes/no prediction markets like Polymarket."
---

Binary markets price whether an event happens. Skepsis prices how much, on a continuous range. Different question, different payoff.

| | Binary market | Skepsis |
|---|---|---|
| Question | Will X happen (yes/no) | Where does the number land (range) |
| Payoff | Fixed, on direction | Scales with precision: N / k at uniform prior |
| A near miss | Wins the same as a blowout | Pays only for the band that hits |
| Range exposure | Stack many binaries; liquidity fragments | One curve, shared liquidity |
| One-of-N choice | N separate yes/no books | One market, N options, shared depth |
| Hedging fit | Basis risk vs real exposure | Hedge the band the exposure lives in |
| Resolution | Varies, some discretionary | Chainlink numerical feed, time-gated |
| Listing | Often permissionless | Curated |

## When binary is the right tool

If your view really is binary, will this happen or not, a binary market fits. Skepsis is for outcomes that are numbers, where direction is not the whole story and magnitude is the point.
