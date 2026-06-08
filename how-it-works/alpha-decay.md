---
title: "Alpha decay"
description: "Liquidity thins toward resolution to defend LPs against late-information snipers."
---

Alpha is the LMSR liquidity parameter. Higher alpha means deeper liquidity and smaller price impact per trade. Skepsis decays alpha over a market's life.

## How it works

Alpha decays linearly from an initial value to a floor over a configured window. The floor is at least ten percent of the initial value, so the market never goes fully illiquid. Decay is applied in epochs and checkpointed on-chain.

```
Start of life:  alpha = high   (deep book, small price impact)
Toward end:     alpha = floor  (shallow book, large price impact)
```

## Why it decays down

Near resolution, information asymmetry is at its worst. A trader with a late read on the outcome can pick off liquidity providers, and a deep book would let them size up. Thinning the book as resolution approaches limits how much a late-information trader can extract. The contract calls this sniper defense.

The cost lands where it belongs. Early, when information is even, the book is deep and trading is cheap. Late, when information is lopsided, the book is shallow and large trades pay for the asymmetry they carry.

## What it means for you

- Trading early is cheaper: deeper book, smaller impact.
- Trading late costs more price impact, by design.
- Liquidity providers hold a bounded, defended position through resolution. See [the vault](/for-lps/vault-overview).
