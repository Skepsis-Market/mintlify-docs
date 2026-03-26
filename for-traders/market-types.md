---
title: "Market Types"
---

## Price Prediction Markets

Markets that resolve based on the price of an asset at a specific time — BTC/USD in 1 hour, ETH at midnight UTC, etc. Typically short duration (minutes to days), resolved by oracle price feeds, with ranges spanning ±5-20% from spot.

1-hour markets are good for learning since you get fast feedback. Watch for scheduled catalysts (Fed, earnings) and size your range width to the asset's volatility.

---

## Date Prediction Markets

Markets that resolve based on *when* something happens — GPT-5 release, GTA 6 launch, next iPhone announcement. These run weeks to months, resolved by official announcements.

Credible leakers are alpha here. Companies have release cadences worth studying, and round dates (Jan 1, Q1 start) tend to be overpriced due to anchoring.

---

## Measurement Markets

Markets that resolve on a measured quantity — tomorrow's high temperature in NYC, Super Bowl final score, box office opening weekend. Duration varies (hours to weeks), resolved by official sources (NOAA, Vegas, Box Office Mojo).

Historical data is your edge. Weather services disagree with each other, and local knowledge sometimes beats models.

## Resolution

All market types follow the same flow: the measurement period ends, an authoritative source reports the value, the value maps to a winning bucket, and winners claim.

**Price markets** use oracle feeds (Pyth, Chainlink, exchange APIs) and resolve automatically. **Date markets** require clear resolution criteria — "public release" vs "beta release" matters, and the market description specifies which counts. **Measurement markets** use official reporting bodies as their source of truth.

## Picking a Market

If you do TA, start with short-duration price markets. If you follow industry news, date markets reward that research. Domain expertise (weather, sports, entertainment) maps directly to measurement markets. When in doubt, 1-hour price markets give the fastest feedback loop for learning the platform.

## Coming Soon

**Conditional markets:** "If [Event A], what will [Outcome B] be?"
