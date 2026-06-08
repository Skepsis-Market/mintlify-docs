---
title: "Example: BTC hourly close"
description: "Price where BTC closes the hour, not just up or down."
---

BTC is at $61,000. A binary market asks whether BTC is above $61,000 at the top of the hour. You think it closes between $60,800 and $61,200, a tight band around here.

| | Binary | Skepsis |
|---|---|---|
| Question | Above $61,000? | Where does BTC close? |
| Your position | Yes | Range: $60.8k to $61.2k |
| Outcome $61,050 | Wins the same as any "up" | Precise. Your tight band pays |
| Outcome $64,000 | You win | Outside your band. You do not win |

On the binary, a five-cent move over the line pays the same as a $3,000 run. On Skepsis a 1-of-10 band pays about 10x at a uniform prior, because it is harder to hit. Resolution is the Chainlink BTC/USD feed at the top of the hour.
