---
title: "Deterministic Payouts"
---

Your payout is locked the moment you bet. No dilution from future bets, no post-hoc pool splitting.

## Parimutuel vs Skepsis

In parimutuel systems (horse racing, most pool-based markets), payouts are calculated *after* all bets close. You bet at "5x" but if 1,000 others pile in, you get 2.5x.

On Skepsis, your quote is your payout. Bet \$100 at 3.2x, your range wins, you get \$320. Period. Subsequent trading on the same range changes prices for new bettors but never touches your position.

---

## Why It Can't Change

You're buying a fixed number of shares at a quoted price. Those shares represent a fixed claim. Nothing that happens after your transaction — other bets, market movements, time — can alter the number of shares you hold or what each share pays at resolution.

---

## Price Impact Without Payout Impact

Your bet moves the market — a \$100 bet on \$96K-\$97K might shift it from 25% to 28% probability. New bettors see 3.57x instead of 4x. But you locked in 4x. Even if 10 more people pile in \$1,000 each and push odds to 2.5x, your payout stays at \$400.

---

## Early vs Late

Early bettors get better odds but less information. Late bettors have more signal but worse prices. Both get deterministic payouts at their entry price. This is the core tradeoff — you're compensated for taking risk when information is thin.

---

## Worked Example

```
Alice bets $200 on $96K-$97K early → locks in 4x → guaranteed $800
Charlie bets $200 on the same range later → gets 2.8x → guaranteed $560

Resolution: BTC = $96,500 (in range)

Alice wins $800. Charlie wins $560. Same range, same bet size, different timing.
```

---

## Selling Before Resolution

You can exit early by selling shares back to the market. The sell quote is also deterministic — confirm the transaction and you receive exactly the quoted amount.

Reasons to sell early: locking in profit after a favorable price move, cutting losses on a thesis you no longer believe, or freeing capital for a better opportunity.

## Implications

Once you bet, you can close the tab. Your payout is locked onchain. You can track exact P&L across all positions because every outcome is known. Shares are ERC-1155 tokens — transferable and composable.
