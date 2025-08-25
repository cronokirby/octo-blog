---
created: 2025-06-08
tags:
  - "blockchain"
---
Bridges enable users to transfer assets between blockchains. Without them, you cannot have an ecosystem of cooperative applications and use-cases, and are stuck in zero-sum competition. The way bridges handle and present risk passes the buck far too much onto users, leading to economic inefficiency, and bad user experience.

Bridging between blockchains should be seamless, ideally so much as to let users not know or care that an action requires it. That this has not been achieved is largely the result of minor technical problems. That they stem from a deeper issue of social coordination, I leave to future writing. However, once these problems are solved, we will be constrained by a far trickier problem: *risk*.

To a large extent, we are afraid of not exposing the details of the bridge to the user, as an action they bear the responsibility of taking, because we are not confident in the bridge. We fear that it may have a security flaw, allowing attackers to steal the funds it secures, or mint arbitrary tokens on the other end; more benignly, we fear that it will simply not work, will get stuck, and we need to expose exactly what is happening, so that we don’t have to trust a system to resolve issues autonomously.

Passing the buck to users to manage the risk of bridging is the most common approach I’ve seen, among other bad ones which include:
- mitigation by locking up funds, allowing time to deter or react to crises,
- restrictions on capacity,
- simply ignoring the risk, which is often the main counterpart to exposing everything to users and wiping your hands clean.

This is not to denigrate security mechanisms and fall-backs, but rather to emphasize that they are indeed fall-backs, and should be seen as safeguards against extraordinary situations, and not the primary mechanism of dealing with risk. They can reduce risk by averting catastrophe, but some risk can linger, and likely always will. We should deal with it not by passing it on to the user, but by internalizing it into our protocols in a timeless way: credit.

The risk of bridged funds stems from an old issue: if someone promises to pay me back, how do I know they will? This is the issue of credit, and we’ve developed simple but effective tools to issue credit at scale. The core idea of our solutions is that in the same way that one person’s word may not be as good as another's, one person’s money isn’t either. We value untrustworthy sources of funds less than trustworthy ones, and require higher interest to compensate us for the risk of holding the buck.

Users currently assume this risk, in many cases, and in no case do they get interest for doing so. Rather, this cost is ultimately ignored, or reflected in hesitancy in their demand. This creates needless friction, and large dead weight loss in the ecosystem. Uncompensated fear benefits no one.

 In the abstract, I think we should reify the relationship between credit and price, and have functioning credit markets for bridged tokens. When you bridge dollars—brought to you by an unnamed sponsor, of course—you may get high quality bridge A dollars, worth approximately their face value, or low quality bridge B dollars, worth not-so-approximately their face value. In either case, what you have is worth a known quantity, and is available for you to transact with on the other side, immediately.
That you might have multiple pseudo-equivalent assets you have to worry about is a reality not only of this proposal, but of the world we are striving to create, of a bazaar of sovereign and interconnected actors, among whom, naturally, liquidity markets can easily be formed, to solve this problem for the user, at minimal cost.

In the concrete, dreams of a functioning and liquid market, are an oasis, and not one so easily found in the arid frontier we wish to develop. It is hard to design a robust decentralized credit market, it is nightmarish to properly price in the risk of bridging, so much of which stems from catastrophic scenarios: all of this might remain a dream.

Nevertheless, we should have a dream to strive for, and in so far as it is not possible, we should understand why, we should keep an eye towards how we might moderate our goals, those of centering and improving the experience of users, such that they become feasible, and we should not pass the buck, leaving users holding all the risk.