---
title: "Placing a trade"
description: "Choose a range, see the payoff, and take a position."
---

Every trade is the same four steps, whether the market is a price range, a time, or a set of options.

<Frame caption="The trading screen: choose a range, see your payoff before you confirm.">
  <img src="/images/app-trading.png" alt="Skepsis trading screen: live bucket distribution and the Your Trade panel" />
</Frame>

<Steps>
  <Step title="Open a market">
    Pick a market from [alpha.skepsis.live/markets](https://alpha.skepsis.live/markets). Each market shows the current distribution across buckets.
  </Step>
  <Step title="Choose your range">
    Select the bucket or band you expect the outcome to land in. A tighter range pays more, because it is harder to hit.
  </Step>
  <Step title="Set your size">
    Enter the amount of USDC. The app shows your payoff before you confirm: what you receive if the outcome lands in your range.
  </Step>
  <Step title="Confirm">
    Confirm the transaction. Your position is issued as an ERC-1155 token and appears in your portfolio.
  </Step>
</Steps>

## What you are paid

If the outcome lands in your range, you are paid in proportion to how tight your range was. At a uniform prior, a 1-bucket pick on a 10-bucket market pays 10x; a 2-bucket pick pays 5x. Payoff = N / k, for k of N buckets.

The price moves as others trade, so the quote you see is the quote at that moment. The payoff shown at confirmation is the payoff you lock in for that trade.

## Selling early

You can close a position before resolution at the current price, the same way you opened it. You do not have to wait for the market to settle.

<Note>
Liquidity is bootstrapped on testnet. On thin markets, large trades move the price; size accordingly.
</Note>
