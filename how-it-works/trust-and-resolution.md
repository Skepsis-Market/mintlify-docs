---
title: "Trust & Resolution"
---


How outcomes are determined and winners get paid.

---

## Resolution Process

1. **Trading closes** at the bidding deadline. No more bets after this point.
2. **Oracle reports** the outcome after resolution time is crossed.
3. **Winning bucket identified** — the bucket containing the reported value wins. All shares in that bucket redeem for $1 each; all others are worth $0.
4. **Winners claim** — call `claim` to receive USDC. Claims never expire.

```
Market: "BTC price at 5:00 PM UTC"
Bidding deadline: 5:00 PM UTC
Oracle reports: BTC = $97,245.67
Winning range: $97,200 - $97,300 (bucket #47)

Your 500 shares in that bucket → $500 USDC
```

---

## Oracle Sources

**Price markets (BTC, ETH, etc.):** Pyth Network as primary, Chainlink as backup, aggregated via median to prevent single-oracle manipulation.

**Weather markets:** NOAA official data, cross-checked against multiple weather services.

**Date/event markets:** Official announcements with pre-defined resolution rules, verified against multiple reputable sources.

---

## Resolution Criteria

Every market defines clear resolution criteria at creation. Good criteria are specific, measurable, verifiable, and time-bound:

```
Good: "BTC/USD price on Binance at exactly 5:00:00 PM UTC"
Good: "Official high temperature recorded at JFK airport on Dec 15"

Bad: "When BTC moons" (undefined)
Bad: "Tomorrow's weather" (which tomorrow? which location?)
```

---

## Edge Cases

**Outcome on a boundary:** Lower bound inclusive, upper bound exclusive. $97,100.00 falls into the $97,100-$97,200 bucket.

**Oracle failure:** 15-minute grace period for primary oracle, then backup oracle, then manual resolution by governance. If unresolvable: all positions refunded.

**Outcome outside market range:** Catch-all buckets at both extremes capture outliers. If nobody bet on the winning catch-all bucket, no traders win and LPs keep the pool minus fees.

---

## Dispute Mechanism

*The decentralized dispute mechanism is a work in progress. During Beta, disputes are handled via community governance channels.*

After resolution is posted, a 24-hour challenge window opens. Disputes require a stake (prevents spam) and evidence — screenshots from multiple exchanges, timestamp proof, alternative oracle data. Valid disputes correct the resolution and reward the disputer. Invalid disputes forfeit the stake.

---

## Security

**Smart contract level:** Resolution only after resolution_time. Cannot resolve twice or change outcome post-resolution. Payout amounts fixed at bet time.

**Oracle level:** Multi-oracle aggregation, staleness checks, sanity bounds, fallback mechanisms.

**Governance level:** Dispute mechanism, emergency pause, 7-day upgrade timelock.

---

## On-Chain Transparency

Everything is verifiable on-chain: all bets and positions, resolution outcomes, claim transactions, fee distribution, and oracle data submitted. Resolution criteria are stored in the market contract. Smart contract code is open source (coming soon).

---

## FAQ

**Who decides the winner?**
No human decides. The oracle reports data; the smart contract determines the winning bucket mathematically.

**Can the protocol change the outcome?**
No. Once resolution is confirmed after the dispute period, it's immutable on-chain.

**What if I forget to claim?**
Claims never expire. Your funds remain in the contract until you withdraw.
