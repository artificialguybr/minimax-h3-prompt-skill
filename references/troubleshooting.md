# Diagnose, repair, evaluate

Symptoms suggest hypotheses; they do not prove root causes. Inspect the rendered clip, actual inputs, expanded prompt and request settings before editing text.

| Symptom | Inspect first | Smallest useful repair |
| --- | --- | --- |
| Opening/ending misses image | Wired role, crop, mode, alignment duration | Correct input routing; describe compatible path and endpoint |
| Endpoint transition morphs | State incompatibility, missing contact/path | Name intermediate physical changes; simplify or split |
| Unwanted cuts | Shot markers, conflicting single-take/cut language | Retain Shot 1 only; describe phases inside it |
| Wrong face/product | Reference role, crop, conflicting assets, subject size | Narrow identity/product reference role; use readable framing |
| Reversed or floating motion | Initial pose, direction, supports, contact | Describe origin, direction, contact and settled result |
| Wrong words/language | Exact script, language tag, expansion, speaking window | Preserve exact line; specify language/accent; allocate time |
| Both people speak | Speaker mapping, supplied voices, simultaneous cues | One visible speaker per turn; tie speech to action; silent listener |
| Unwanted extra speech | Empty time, vague mouth movement, audio source | Specify post-line silent reaction and complete sound policy |
| Music despite no score | Field omitted, diegetic source, copied audio | Use N/A for score; clarify reference layers and room sounds |
| Audio copy differs | Reference/reuse distinction, enabled track, external attachment | Correct relationship; use exact audio assembly if essential |
| Rubber mouth | Face size, head occlusion, pace, audio timing | Simplify delivery/camera; use supported target-line conditioning |
| Text/logo drifts | Scale, motion, multiple edits, unsupported exactness | Isolate or composite approved graphic |
| Continuation repeats | Source tail, next action, conflicting reference role | Describe terminal state and new action; test editorial cut |
| 2K changes approved take | Regeneration route, inherited context | Review refinement; regenerate or keep approved base |
| Same seed differs | Model/runtime, media order, expansion, hardware | Pin the full environment and record expanded prompt |
| Acceleration harms sound | Checkpoint/LoRA, steps, audio decoder/schedule | Compare approved baseline and listen; remove unverified speedup |

## Repair policy

Keep the successful clip/source and list the observed defect precisely. Revise one main cause hypothesis at a time. Do not invent a precise diagnosis such as "reversed training footage" or "missing period" from a single failure. If protected content must remain exact, use masks or post-production where available.

Do not soften blocked requests to evade safety enforcement. State the interface limitation and offer a compliant alternative preserving the creative goal where possible.

## What was removed from the old package

- Universal ~7,000-character ceiling: a destination-specific limit must be checked.
- Universal ~20 words/15 seconds and one sentence/block: plan from real delivery time instead.
- "No guidance/negative field anywhere": documented for one integration, not all wrappers.
- "No subtitles always introduces subtitles": positive phrasing is useful, but universal failure is not established.
- "Room tone triggers music": official examples use room tone; treat a local symptom as an experiment.
- "Audio must always have visual input": local and hosted schemas differ.
- "Reference must use different words": appropriate for timbre-only clarity, inappropriate for exact reuse.
- Exact cut tolerance, universal physical-reasoning percentage, four-window cap and +13% sharpening: unsupported as general H3 facts.
- Universal CPU-seed cross-GPU guarantee and specific LoRA scales/triggers: require pinned implementation/card and testing.
- "Editing preserves omitted content": omission cannot guarantee preservation.

## A/B evaluation protocol

Hold model/version, seed when available, media order, duration, resolution, expansion and sampler fixed. Change one prompt factor. Compare several seeds if budget permits; one take cannot establish a universal trick. Record expected observable outcome before rendering.

Score each 0–2: requested action, identity/product, physical contact, composition/camera, endpoint/continuity, exact speech/speaker, audiovisual synchronization, sound quality, style consistency, and unwanted elements. Mark irrelevant criteria N/A. Any critical protected attribute failure rejects the take regardless of average score.

Watch full-speed first; inspect sampled frames and failure moments second. Listen separately to the audio. ffprobe can check duration/fps/dimensions/channels when files exist, but container properties do not establish creative success. Exact logo, copy, pronunciation and waveform copying need their own checks.

## Research versus testing

This package was revised through documentation comparison and prompt-level checks. It does not contain new rendered-video benchmarks. Present example prompts as authored recipes, not tested high-quality outputs. Keep community claims optional until independently verified on the target setup.
