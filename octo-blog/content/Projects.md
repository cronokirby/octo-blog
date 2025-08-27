- [Cait-Sith](https://github.com/cronokirby/cait-sith) [[2023]]
  - Cait-Sith is a novel threshold ECDSA protocol (and implementation), which is both simpler and substantially more performant than popular alternatives.
    The protocol supports arbitrary numbers of parties and thresholds.

- [Magikitten](https://github.com/cronokirby/magikitten) [[2022]]
  - A system to make public-coin protocols non-interactive, using [Meow](https://github.com/cronokirby/meow).
    Inspired by [Merlin](https://merlin.cool/).

- [Meow](https://github.com/cronokirby/meow) [[2022]]
  - This crate is an implementation of [STROBE](https://strobe.sourceforge.io/specs/) using KitTen (reduced round [Keccak](https://keccak.team/keccak.html)).
STROBE is a framework for symmetric cryptography protocols, similar to
how Noise works for key exchange.

- [Deevee](https://github.com/cronokirby/deevee) [[2022]]
  - An implementation of [Designated Verifier Signatures](https://www.wikiwand.com/en/Designated_verifier_signature).
    This is like a normal signature scheme, except that the signer
    designates a verifier for each signature.
    Only this verifier can validate the signature.
    Furthermore, the verifier can forge signatures which designate them.

- [Boo-Hoo](https://github.com/cronokirby/boo-hoo) [[2022]]
  - An implementation of [ZKBoo](https://eprint.iacr.org/2016/163).
    This is a library for creating Non-Interactive Zero-Knowledge Proofs
    of Knowledge (NIZKPoKs) for arbitary boolean functions.
    In other words, given some arbitrary function $f$, and some claimed
    output $y$, you can prove that you know an input $x$ such that $f(x) = y$,
    without revealing what the secret $x$ is.

- [Yao's Garbled Circuits](https://github.com/cronokirby/yao-gc) [[2022]]
  - An implementation of [Yao's Garbled Circuits](https://www.wikiwand.com/en/Garbled_circuit).
    This is a protocol which lets two parties compute a boolean function
    of their private inputs, without revealing those inputs to each other.
    This is one of the earliest and simplest two-party MPC protocols.

- [Seed Split](https://github.com/cronokirby/seed-split) [[2022]]
  - A simple tool to split seed phrases (like with Ethereum, Bitcoin, etc.) into
multiple shares. Any threshold of these shares can then be used to recover
the original seed phrase.
    A good occasion to implement arithmetic over binary fields from scratch as well.

- [Sally](https://github.com/cronokirby/sally) [[2022]]
  - A simple shell written in C. I implemented basic features like command
execution, output redirection, and piping output between processes.

- [Wordle Solver](https://github.com/cronokirby/wordle) [[2022]]
  - A little solver for the infamous [Wordle](https://www.powerlanguage.co.uk/wordle/)
game, as well as a little CLI implementation of the game. Mainly just
a fun weekend project, and a way I consistently beat the game.

- [Ludus Web](https://github.com/cronokirby/ludus-web) [[2021]]
  - A port of my NES emulator to the web, using WASM.
    [Live](https://ludus-web.cronokirby.com). Provides a more accessible
    interface compared to my old [ludus](https://github.com/cronokirby/ludus) project.

- [Multiset Hash](https://github.com/cronokirby/multiset-hash) [[2021]]
  - A simple incremental hash function for multi-sets.
    The result of the function depends only on what objects
    are passed into the function, and not the order they appear.

- [Eddo](https://github.com/cronokirby/eddo) [[2021]]
  - I wanted to implement Ed25519, so I did that, with
this crate implementing everything from scratch, including
SHA-512.
    I also wanted to optimize the implementation, but didn't get around
    to that.

- [Nuntius](https://github.com/cronokirby/nuntius) [[2021]]
  - A little CLI tool for E2E encrypted messaging. I implemented
    Signal's [X3DH](https://signal.org/docs/specifications/x3dh/)
    and [Double Ratchet](https://signal.org/docs/specifications/doubleratchet/)
    in a pretty straightforward way. Unlike Signal, this application
    is session based instead of asynchronous, out of simplicity.

- [Nimotsu](https://github.com/cronokirby/nimotsu) [[2021]]
  - A little tool to encrypt files to public key identities, using
[Curve25519](https://tools.ietf.org/html/rfc8031),
[Blake3](https://github.com/BLAKE3-team/BLAKE3), and
[ChaCha20-Poly1305](https://tools.ietf.org/html/rfc7539), all
implemented from scratch.

- [Saferith](https://github.com/cronokirby/saferith) [[2021]]
  - A library providing constant-time Big Number arithmetic, for Go. Essentially,
a replacement for `big.Int`, suitable for Cryptography.
    This was the subject of my [BSc Project](/papers/2021/06/bsc_report.pdf)
    at EPFL, under the supervision of [Prof. Bryan Ford](https://people.epfl.ch/bryan.ford).

- [Fractals](https://github.com/cronokirby/fractals) [[2021]]
  - [Live](https://fractals.cronokirby.com)
    This is a fun little fractal explorer I made over a few days.
    This uses the mandelbrot and julia sets as base fractals, along with
    various coloring modes based on iteration or orbit traps.

- [Enku](https://github.com/cronokirby/enku) [[2021]]
  - I was bored one weekend, and decided to implement
[ChaCha20](https://tools.ietf.org/html/rfc7539) from scratch
(easier than it sounds) to make a tool for encrypting data.

- [Haskell-in-Haskell](https://github.com/cronokirby/haskell-in-haskell) [[2021]]
  - This is a compiler for a respectable subset of Haskell,
    written in Haskell. This features standard data types,
    pattern matching, as well as lazy evaluation!
    I'm also writing [an in-depth series](/series/haskell-in-haskell) 
    about this compiler

- [KaTeX Playground](https://github.com/cronokirby/katex-playground) [[2020]]
  - [Live](https://katex-playground.cronokirby.com)
    I whipped this up over an afternoon. It's just a little
    site letting you write math equations interactively
    thanks to [KaTeX](https://katex.org/).

- [Arbor](https://github.com/cronokirby/arbor) [[2020]]
  - This is a simple replacement for the Unix `tree program`.
    This will print out the file system hierarchy in tree form, starting
    from a given path. The program comes with configurable options for depth,
    Unicode, and color output.
<!--more-->

- [Conway](https://github.com/cronokirby/conway) [[2020]]
  - A simple implementation of [the classic Cellular Automaton](https://www.wikiwand.com/en/Conway%27s_Game_of_Life), as
    an interactive graphical application in Haskell.

- [Reg Viz](https://github.com/cronokirby/reg-viz) [[2020]]
  - **Reg Viz** is a simple CLI tool taking a regular expression, and outputting a representation
    of the NFA / state machine recognizing that language. This is useful to visualize
    the correspondance between regular languages and finite state machines.

- [Mooz](https://github.com/cronokirby/mooz) [[2020]]
  - This is a simple application that lets you start video calls with multiple
    people, in a peer 2 peer fashion. Unlike applications like zoom, there's
    no central server handling connections.

    [Read More](/posts/simple-webrtc-video-chat)

- [Musync](https://github.com/cronokirby/musync) [[2020]]
  - This is similar to [Populate](https://github.com/cronokirby/populate).
    This is a program that can clone a music library based on its description. It can download
    albums, split them automatically, and add metadata to these songs, like cover art and names.

    It uses `youtube-dl` for the downloading, and `ffmpeg` for the splitting.

- [Poline](https://github.com/cronokirby/poline) [[2019]]
  - **Poline** is a little programming language I wrote to learn
    about implementing Green Threading. The language
    doesn't feature much more than string literals, and mechanisms
    for spawning threads and communicating between them.
    Green Threads allow many logical threads in a program to
    execute on a limited number of actual OS threads. They
    can be preempted off if they invoke a blocking operation.

- [Ginkou](https://github.com/cronokirby/ginkou) [[2019]]
  - **Ginkou** is a program to build up a corpus of searchable sentences.
    **Ginkou** can consume Japanese sentences from the command line, or from a text
    file, parse those sentences into words, and then index those sentences for
    easy retrieval. Given a word, **Ginkou** can look up sentences containing
    that word, even if it's in a different form, such as a conjugated verb.

- [Persistent-ts](https://github.com/cronokirby/persistent-ts) [[2019]]
  - This is a library providing a handful of persistent data structures for Typescript.
    This includes immutable collections like linked-lists, and clojure-style vectors.
    Persistent data structures are immutable, but can efficiently share data between instances,
    and are thus more efficient than a normal copy-on-write collection when working without mutation.

- [Serve-csv](https://github.com/cronokirby/serve-csv) [[2019]]
  - This is a program that can take a folder of CSV files and serve them as a REST API.
    The program also uses a JSON file for each file, to specify how each column maps to a JSON
    field. The program is written in Go to make use of the built-in HTTP server.

- [Haze](https://github.com/cronokirby/haze) [[2019]]
  - **Haze** is a complete bittorrent client, capable of downloading any kind
    of torrent found in the wild. Bittorrent is a peer-to-peer protocol, where a client
    joins a large swarm of peers in order to download a file of common interest. Haskell was
    used in order to help manage the concurrency involved in communicating with a large number of
    peers.

- [Dex](https://github.com/cronokirby/dex) [[2019]]
  - [Live](https://cronokirby.github.io/dex).
    **Dex** is a little frontend app for searching and seeing stats about Pokemon, made with Vue.
    The app wraps around the [pokeapi](https://pokeapi.co/) REST API for information about each Pokemon.

- [Ripple](https://github.com/cronokirby/ripple) [[2019]]
  - **Ripple** is a program implementing a small decentralised chat protocol, written in *Go*.
    The protocol involves participating nodes ferrying messages to eachother in a ring like fashion.
    New nodes can join the chat by talking to any of the existing nodes in the swarm. *Go* is used for
    simple networking and concurrency, as well as to provide both a command line, and a graphical terminal interface.
    [Read More](/posts/notes-on-ripple/)

- [Huffman-rs](https://github.com/cronokirby/bittrickle) [[2019]]
  - This is a CLI program using *Huffman Coding* to compress files. The program is written in *Rust*
    for efficiency.

- [Bittrickle](https://github.com/cronokirby/bittrickle) [[2019]]
  - **Bittrickle** is an implementation of Bittorrent's UDP tracker protocol. A tracker keeps
    track of peers participating in a bittorrent swarms, sharing files. Peers communicate with
    the tracker in order to learn about each other. This implementation uses *Rust* because of its
    built-in UDP networking.

- [Cauchy](https://github.com/cronokirby/cauchy) [[2019]]
  - **Cauchy** is a program to generate plots of complex functions, written in *Rust*
    **Cauchy** is hardware-accelerated, using *OpenGL* to generate the plots using the GPU.

- [Populate](https://github.com/cronokirby/populate) [[2018]]
  - This is a CLI program that can recreate a music library on a new machine by downloading
    the files from various sources across the web. The program parses a file
    with a hierarchical description of the library to replicate , and reproduces
    that structure by consuming the sources described.
    The program can also split up larger albums (via FFmpeg) into individual songs if necessary.

- [Darby](https://github.com/cronokirby/darby) [[2018]]
  - This is a CLI program to take a folder of songs and play them in a random order.
    SDL's audio subsystem is used to play audio files. This program was built to accompany
    [populate](https://github.com/cronokirby/populate), which generates folders filled with songs,
    ready for consumption by this program.

- [Peerbin](https://github.com/cronokirby/peerbin) [[2018]]
  - [Live](https://cronokirby.github.io/peerbin/#/).
    This project provides a version of websites like pastebin, or hastebin, except without
    a central server to store the files; instead users send the files to eachother
    via [webtorrent](https://webtorrent.io/). *Elm* is used for the main
    UI components, and *Javascript* to glue this code with the webtorrent part.

- [Hax](https://github.com/cronokirby/hax) [[2018]]
  - **Hax** is a bullet hell game, in the same vein as others like *Touhou* or *Ikaruga*.
    The game is written in Haskell, using SDL for handling the drawing logic. The game
    logic benefits greatly from the use of an entity component system for handling the many entities
    in the game. [Apecs](https://hackage.haskell.org/package/apecs) was used to provide the scaffolding
    for this ECS.

- [Ludus](https://github.com/cronokirby/ludus-emu) [[2018]]
  - **Ludus** is an emulator for the NES console, written in *Rust*. The emulator
    fully emulates, the core CPU, as well as the PPU and APU, and thus full video
    and audio. The emulator also supports a handful of mappers / cartridge types, and thus
    many common games such as Mario or Zelda.

- [Alchemy](https://github.com/cronokirby/alchemy) [[2018]]
  - **Alchemy** is a library over the API for the chat application
    [Discord](http://discordapp.com/). The library integrates over Discord's REST
    and Websocket APIs in order to help developers write applications for their chat
    servers. *Elixir* was used in order to have easy access to the concurrency involved
    in juggling these various resources.
