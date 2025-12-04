---
title: "Trust & Resolution"
---


How Skepsis determines outcomes fairly and pays winners.

---

## The Resolution Process

### Step 1: Market Closes

At the specified **bidding deadline**, trading stops:

```
Market: "BTC price at 5:00 PM UTC"
Bidding deadline: 5:00 PM UTC

4:59 PM: Trading open ✅
5:00 PM: Trading closed ❌
5:01 PM: Awaiting resolution
```

No more bets can be placed after deadline.

### Step 2: Outcome Determined

At **resolution time**, the actual outcome is reported:

```
Resolution time: 5:00 PM UTC (same as deadline for price markets)
Oracle reports: BTC = $97,245.67
```

### Step 3: Winning Range Identified

The system determines which bucket/range contains the outcome:

```
Outcome: $97,245.67
Winning range: $97,200 - $97,300 (bucket #47)

All shares in bucket #47 are now redeemable for $1 each
All shares in other buckets are worth $0
```

### Step 4: Winners Claim

Winners can claim their payouts:

```
Your position: 500 shares in $97,200 - $97,300
Outcome: $97,245.67 ✅ In your range!
Payout: 500 × $1 = $500 USDC

Click "Claim" → USDC sent to your wallet
```

---

## Oracle Sources

Different market types use different data sources:

### Price Markets (BTC, ETH, etc.)

```
Primary: Pyth Network (decentralized price feeds)
Backup: Chainlink oracles
Aggregation: Median of multiple sources
```

**Why multiple sources?**
- Single oracle can malfunction
- Aggregation prevents manipulation
- Decentralized = trustless

### Weather Markets

```
Source: NOAA (National Oceanic and Atmospheric Administration)
Verification: Weather.gov official data
Cross-check: Multiple weather services
```

### Date/Event Markets

```
Source: Official announcements
Criteria: Pre-defined resolution rules
Verification: Multiple reputable news sources
```

---

## Resolution Criteria

Every market has **clear resolution criteria** defined at creation.

### Good Criteria Examples

```
✅ "BTC/USD price on Binance at exactly 5:00:00 PM UTC"
✅ "Official high temperature recorded at JFK airport on Dec 15"
✅ "Date of first public availability per OpenAI blog post"
```

### Bad Criteria Examples

```
❌ "When BTC moons" (undefined)
❌ "Tomorrow's weather" (which tomorrow? which location?)
❌ "When the product launches" (beta? limited? general?)
```

### What Makes Good Criteria

| Property | Why It Matters |
|----------|----------------|
| **Specific** | No ambiguity in interpretation |
| **Measurable** | Objective, not subjective |
| **Verifiable** | Can be independently confirmed |
| **Time-bound** | Clear when resolution happens |

---

## Edge Cases

### What if the outcome is exactly on a boundary?

```
Boundaries: $97,000.00 | $97,100.00 | $97,200.00
Outcome: $97,100.00

Rule: Lower bound inclusive, upper bound exclusive
$97,100.00 falls into: $97,100 - $97,200 bucket ✅
```

### What if the oracle fails?

```
Scenario: Primary oracle is down at resolution time

Fallback sequence:
1. Wait for primary oracle (15 min grace period)
2. Use backup oracle
3. Use manual resolution by governance
4. If unresolvable: Refund all positions
```

### What if the outcome is outside the market range?

```
Market range: $90,000 - $110,000
Outcome: $85,000 (below range!)

Resolution: First bucket wins ($90,000 - $90,500)
Rationale: Closest valid bucket

Same logic applies if outcome is above range.
```

---

## Dispute Mechanism

What if you disagree with the resolution?

### Step 1: Challenge Period

```
Resolution posted: Bucket #47 wins
Challenge window: 24 hours

During this window:
- Anyone can submit a dispute
- Dispute requires stake (prevents spam)
```

### Step 2: Evidence Submission

```
Disputer claims: "Oracle was wrong, actual price was $96,999"
Evidence required: 
- Screenshots from multiple exchanges
- Timestamp proof
- Alternative oracle data
```

### Step 3: Resolution

```
If dispute is valid:
- Resolution is corrected
- Disputer gets stake back + reward
- Original resolution voided

If dispute is invalid:
- Original resolution stands
- Disputer loses stake
```

---

## Timing Guarantees

### For Traders

| Event | Guarantee |
|-------|-----------|
| Trading cutoff | Exactly at bidding_deadline |
| Resolution | Within 1 hour of resolution_time |
| Claim availability | Immediately after resolution |
| Claim expiry | 90 days (claim anytime within) |

### For Market Creators

| Event | Guarantee |
|-------|-----------|
| Market goes live | Immediately after creation tx confirms |
| LP withdrawal | After all claims processed or 90 days |

---

## Security Measures

### Smart Contract Level

```
✅ Resolution only after resolution_time
✅ Cannot resolve twice
✅ Cannot change outcome after resolution
✅ Payout amounts fixed at bet time (not resolution)
```

### Oracle Level

```
✅ Multi-oracle aggregation
✅ Staleness checks (reject old data)
✅ Sanity bounds (reject impossible values)
✅ Fallback mechanisms
```

### Governance Level

```
✅ Dispute mechanism
✅ Emergency pause capability
✅ Upgrade timelock (7 days)
```

---

## Transparency

### What's Verifiable On-Chain

- ✅ All bets and positions
- ✅ Resolution outcome
- ✅ Claim transactions
- ✅ Fee distribution
- ✅ Oracle data submitted

### What's Publicly Auditable

- ✅ Smart contract code (open source)
- ✅ Resolution criteria (stored in market)
- ✅ Historical resolutions (on-chain history)

---

## FAQ

### "Who decides the winner?"

No human decides. The oracle reports data, the smart contract determines the winning bucket mathematically.

### "Can the protocol change the outcome?"

No. Once resolution is confirmed (after dispute period), it's immutable on-chain.

### "What if I forget to claim?"

You have 90 days. After that, unclaimed funds go to protocol treasury. (Set a reminder!)

### "How do I know the oracle is honest?"

We use decentralized oracle networks (Pyth, Chainlink) that aggregate multiple data sources. No single party can manipulate.

---

## Best Practices

### Before Betting

1. Read the resolution criteria carefully
2. Understand which oracle will be used
3. Check the resolution time

### After Resolution

1. Verify the outcome matches public data
2. Claim winnings promptly
3. Report discrepancies during dispute window

---

## Next Steps

<table data-card-size="large" data-view="cards">
<thead><tr><th></th><th></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead>
<tbody>
<tr><td><strong>FAQ</strong></td><td>Common questions answered</td><td><a href="/faq">FAQ</a></td></tr>
<tr><td><strong>Quick Start</strong></td><td>Ready to make a prediction?</td><td><a href="/overview/quick-start">Quick Start</a></td></tr>
</tbody>
</table>
