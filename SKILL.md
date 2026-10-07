---
name: minimax-h3-prompt-writer
description: Write and repair MiniMax H3 audiovisual prompts from ideas, images, videos, audio, and storyboards. Use for T2VA, I2VA, FL2VA, L2VA, Ref2VA, character/style/motion/voice reference, video edits and continuation, audio reuse, multilingual dialogue, ads, documentary shots, animation, and motion graphics. Adapt structured rewrites and freeform prompts to MiniMax API, local ComfyUI/Diffusers, and verified hosted H3 variants.
---

# MiniMax H3 Prompt Writer

Produce a concrete audiovisual shot specification, not an adjective list. Preserve the user's creative intent, exact spoken words, and reference roles. Treat model control as probabilistic: prompt instructions do not guarantee pixel-identical edits, frame-exact cuts, or bit-identical audio copying.

## Read only what the task needs

- Read [capabilities.md](references/capabilities.md) for mode selection, input roles, API settings, mixed references, audio-only questions, or provider differences.
- Read [base-en.txt](references/base-en.txt) for structured T2VA/I2VA/FL2VA/L2VA syntax.
- Read [ref-en.txt](references/ref-en.txt) for structured Ref2VA syntax. Also read the base guide if using dialogue, singing, voiceover, or cross-cut speech.
- Read [direction.md](references/direction.md) for shot design, physical interaction, reference preparation, realism, ads, documentary, animation, and graphics.
- Read [audio.md](references/audio.md) for speech, voice transfer, exact audio reuse, singing, and soundtrack continuity.
- Read [freeform-en.txt](references/freeform-en.txt) for a hosted prompt box or a provider's expansion layer.
- Read [editing-brief.txt](references/editing-brief.txt) for video editing, continuation, and targeted repairs.
- Read [examples.md](references/examples.md) for original examples spanning core and advanced tasks.
- Read [troubleshooting.md](references/troubleshooting.md) for failed output and evaluation.
- Read [sources.md](references/sources.md) before asserting a technical limit or using a claimed trick as a rule.
- Read [experimental-local.md](references/experimental-local.md) ONLY for local ComfyUI/diffusers workflows: community LoRAs, speed tiers, Fun Control, long-video chaining. Everything there is community-sourced and marked experimental — never present it as a model guarantee.

## 1. Resolve the task contract

Infer from the request: target interface/model; source assets and their actual roles; deliverable duration/aspect; single take or cuts; identity/product constraints; exact script and language; audio policy; final state. Ask only when ambiguity changes the result, especially whether a still is an opening frame, ending frame, or identity reference. Do not block on optional taste preferences.

Inspect attached media when available. Do not invent its content or claim to have heard audio that was not decoded. If media is unavailable, use the user's description and mark any asset-dependent assumption outside the prompt when necessary.

Keep a private asset ledger: upload order, modality index, file, role, retained attributes, transferred attributes, discarded attributes, and enabled soundtrack. Keep asset indices distinct from `<Subject N>` and speaker IDs. One image may supply several subjects; several images may define one subject.

## 2. Select the actual mode

| Input intent | Mode | Planning obligation |
| --- | --- | --- |
| Text only | T2VA | Establish the opening state and full audiovisual timeline |
| A still is the opening | I2VA | Develop forward from the depicted state |
| Stills specify opening and ending | FL2VA | Describe a plausible continuous bridge and endpoint landing |
| A still is the ending | L2VA | Infer a compatible opening and converge to the final composition |
| Assets supply identity, style, action, camera, or audio | Ref2VA | Assign each asset a narrow role and fidelity relationship |
| Transform an existing video | Ref2VA editing | State precise changes plus protected visual and audio properties |
| Extend an existing video | Ref2VA continuation or verified extension endpoint | Describe new footage from the source's ending state |
| Intermediate frames, masks, pose/depth/edges, explicit camera path | Verified advanced workflow | Supply the required conditioning inputs; prose alone does not enable them |

Do not equate all hosted H3 variants. Verify the current endpoint schema for mixed keyframes/references, middle frames, exact audio attachment, camera controls, extension, and resolution. Use direct MiniMax rules only for that API. Use local rules only for the identified implementation.

## 3. Choose the prompt surface

For direct local H3-Base input, use the selected structured guide. For hosted services that rewrite prompts, use a clear production brief unless the user asks for the structured form. Structured fields are a text convention inside a prompt, not arbitrary top-level API keys. Keep duration, ratio, resolution, role assignments, and sampler settings in their actual request controls as well as matching the creative description.

Use the three base fields or the six Ref2VA sections exactly as documented. Keep the entire rewrite in English except exact dialogue, lyrics, and scene-visible text. Preserve the selected format's labels, section order, and alignment sentences. Do not force a target word count if it would introduce contradictions or exceed the destination's actual limit.

## 4. Direct the clip

1. Establish style through observable image properties: medium, lighting direction/softness, framing, texture, palette, and motion behavior. Avoid automatically making every request cinematic.
2. Name the opening state and important stable anchors. Describe each subject's position and action, then the causal state change and final state.
3. Budget the most difficult event first. Prefer one principal interaction per shot as a reliability heuristic; permit multiple simple actions when timing and causality remain readable.
4. Specify movement direction, contact, support, and relevant occlusion. Distinguish subject motion from camera motion.
5. Give each shot one dominant camera intention. State type, amplitude, speed, and framing outcome. Use a static camera when the event itself carries the shot.
6. For a continuous take, retain `[Shot 1]` and describe phases inside it. Introduce `[Shot 2]` only for a real cut; later cut times must increase and fall before the clip ends.
7. For endpoint modes, preserve the pictured state and describe intermediate changes. Reach the final composition before the end; allow a brief settling beat when feasible.
8. For references, state what each asset supplies and what it does not supply when ambiguity matters. Reference-only images do not automatically become first frames.
9. Fit speech to its speaking window by reading it aloud or using known audio duration. Do not use a universal words-per-clip limit or rewrite a locked script silently.
10. Separate dialogue/diegetic events, ambience/SFX, and audience-only music. Use `N/A` in the proper field for absent music or complete silence. Do not invent speech to fill unused duration.

## 5. Compile and check

Check mode and physical feasibility; exact asset mapping; correct alignment duration and final-shot number; field order; one opening shot marker; valid increasing cuts; stable subject/speaker labels; balanced `<d>` blocks with language tags; unchanged user text; audio relationships matching intent; and consistent settings. Use `scripts/lint_prompt.py` when practical. Treat its speech-rate flags as warnings, not model limits.

Do not assume a universal prompt-character limit, negative-prompt API, sampler, LoRA, seed field, or deterministic result across hardware. Positive scene specifications are a useful default; ordinary textual prohibitions are instructions, not a CFG negative branch.

If a locked script cannot fit, explain the conflict and propose a longer supported clip or split. If an asset role is ambiguous and essential, request clarification. Do not output a knowingly invalid API combination just to keep the answer prompt-only.

## 6. Output according to the request

- Prompt only: return only the final prompt, without fences or commentary, unless a blocking incompatibility must be explained.
- Prompt plus settings: show the prompt and a separate settings block, with asset order and supported controls. Do not place execution notes inside the generation text.
- Multi-clip production: provide separate prompts and shared continuity anchors; name per-clip audio policy. Prefer independent shots when uninterrupted continuation is not necessary.
- Failure repair: identify the observed defect and change the smallest relevant specification. Preserve successful attributes. Do not claim a cause from a symptom alone.

For longer work, keep identity/wardrobe/prop, screen direction, light, camera style, and voice anchors consistent. Choose one continuous score in post when musical continuity matters, or explicitly bridge native generated audio. Never promise clean stems, exact typography, or editorial timing solely from prompting.

## Evidence policy

Prefer current MiniMax guides for grammar, each provider's schema for interface limits, and implementation documentation for local behavior. Label new directing choices as heuristics. Treat community tricks as experiments until tested on the user's actual stack. Do not claim rendered-video validation when only prompt validation was performed.
