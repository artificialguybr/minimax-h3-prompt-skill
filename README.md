# MiniMax H3 Prompt Writer — a skill for production-ready H3 video prompts

An [agent skill](https://github.com/anthropics/skills) that turns any idea, image, or clip reference into a **prompt in MiniMax H3's exact trained format** — the single biggest lever on output quality for this omni-modal video model.

H3 generates synchronized native audio (dialogue, sound effects, music) from structured English prompts. This skill writes those prompts correctly instead of free-forming them.

## What it does

- **Routes the input to the right mode** — T2VA (text only), I2VA (image = first frame), FL2VA (first + last frame), L2VA (image = last frame), Ref2VA (loose style/motion/voice references) — and asks one routing question only when it is truly ambiguous.
- **Copies the trained format verbatim** from `references/base-en.txt` / `ref-en.txt`: numbered reference jobs, `[Shot N] At MM:SS.mmm` timestamps, camera moves with type + amplitude + speed, dialogue in `<d>[Language] …</d>` with stable speaker IDs, verbatim on-screen text in quotes, and the two mandatory soundscape fields.
- **Gets duration/aspect right, per interface**: direct API (t2va requires a concrete ratio; i2va follows the image and ignores a conflicting one), local frame grid `17*n+5` @ 24fps — each documented separately, no schema transfer. Segment budgets and FL2VA/L2VA two-decimal alignment included.
- **Self-validates silently**: a mechanical checklist (alignment line, field order, timestamps, closed tags, quoted text, length budget) runs before output — the user only ever sees the finished prompt.
- **Repairs failures locally**: paste what went wrong and it loads `references/troubleshooting.md`, diagnoses symptom → cause, and emits a repair prompt that reuses the good clip as a reference and names the defect precisely.

## Install

Copy the folder into your agent's skills directory (for Claude-style harnesses, `~/.claude/skills/` or your equivalent):

```sh
git clone https://github.com/artificialguybr/minimax-h3-prompt-skill.git
cp -R minimax-h3-prompt-skill ~/.claude/skills/
```

The `SKILL.md` loads on demand; references load lazily — keep relative paths intact.

## Usage

Just ask for an H3 prompt in any of these shapes:

- "Write an H3 prompt: a barista discovers the espresso machine is broken, 8 seconds, 9:16, Portuguese dialogue."
- "Here's the opening frame and the closing frame — write the FL2VA prompt." (attach two images)
- "The generated clip has the clock reading the wrong time and extra mumbling at the end. Fix only that."

Output is the formatted prompt only — no commentary, no fences. Iteration tips (environment quirks such as CFG=1 making negative prompts useless, low-res-first workflows) are built into the skill.

## Structure

```text
SKILL.md                        # compact router: read only what the task needs
references/capabilities.md      # modes, input roles, API vs local vs provider
references/base-en.txt          # trained format for T2VA/I2VA/FL2VA/L2VA
references/ref-en.txt           # trained format for Ref2VA
references/direction.md        # shot design, reference prep, realism/ads/animation
references/audio.md            # speech, voice transfer, exact audio reuse, singing
references/freeform-en.txt      # hosted freeform format ([0s-3s] blocks)
references/editing-brief.txt     # video editing, continuation, targeted repairs
references/examples.md         # original examples, core and advanced tasks
references/troubleshooting.md   # symptom → cause → localized repair prompt
references/sources.md           # evidence ledger (18 primary sources, 3 levels)
references/experimental-local.md # COMMUNITY/EXPERIMENTAL: local LoRAs, speed tiers, long video
scripts/lint_prompt.py           # mechanical prompt linter
agents/openai.yaml              # optional agent UI metadata
```

## Honest limits

- The format files are the model's training-time contract; follow them character-for-character rather than paraphrasing.
- Facts are documented **per interface** (direct API / local Diffusers-ComfyUI / providers) with an evidence ledger (`references/sources.md`); never transfer one surface's schema to another. `experimental-local.md` holds community findings (LoRAs, speed tiers, long-video chaining) clearly marked as experimental.
- A perfectly formatted prompt still yields stochastic takes; regenerate selectively instead of rewriting everything.

Built following the [skill-creator](https://github.com/anthropics/skills/blob/main/skills/skill-creator/SKILL.md) structure. License: MIT.
