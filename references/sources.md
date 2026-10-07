# Evidence map

Research date: 2026-10-06. Prefer primary documentation over look-alike H3 websites. Recheck schemas before running a job. The base/ref files are revised from the user-supplied package; their existing grammar was compared against MiniMax's current guides. Authored examples and directing advice are not reproduced showcase prompts or new benchmarks.

| ID | Primary source | Use |
| --- | --- | --- |
| S1 | https://huggingface.co/MiniMaxAI/MiniMax-H3 | architecture, variants, reference budget, workflow and 2K stages |
| S2 | https://www.minimax.io/blog/minimax-h3 | multimodal design and generalization versus exposed endpoints |
| S3 | https://platform.minimax.io/docs/api-reference/video-generation-v2-create | current direct API controls, roles and model limits |
| S4 | https://platform.minimax.io/docs/api-reference/video-generation-v2-h3-context-ir | hosted contextual rewrite stage |
| S5 | https://platform.minimax.io/docs/api-reference/video-generation-v2-regeneration | regeneration endpoint; distinct from base sampling |
| S6 | https://huggingface.co/docs/diffusers/main/en/api/pipelines/minimax_h3 | modular local workflows, frame grid, guidance, reference order and rates |
| S7 | https://recipes.vllm.ai/MiniMaxAI/MiniMax-H3 | implementation settings and serving examples |
| S8 | https://fal.ai/models/minimax/h3-max/reference-to-video/api | provider-specific reference lists, endpoint/middle frames |
| S9 | https://fal.ai/models/minimax/h3-max/text-to-video/api | expansion, seed, exact soundtrack attachment |
| S10 | https://fal.ai/models/minimax/h3-max/extend-video/api | dedicated extension and output mode |
| S11 | https://docs.comfy.org/tutorials/video/minimax/minimax-h3-multiframe | local timeline image guidance |
| S12 | https://docs.comfy.org/tutorials/video/minimax/minimax-h3-fun-controlnet | control-video modalities and mask-based editing |
| S13 | https://docs.comfy.org/tutorials/video/minimax/minimax-h3-prompt-guide | positive specifications, reference-sheet panels, speaker troubleshooting |
| S14 | https://github.com/MiniMax-AI/MiniMax-H3/blob/main/skills/h3-prompt-writing/references/ref-en.txt | reference labels and retention/audio meanings |
| S15 | https://github.com/MiniMax-AI/MiniMax-H3/blob/main/skills/h3-prompt-writing/references/base-en.txt | base/keyframe grammar, dialogue and sound fields |
| S16 | https://docs.comfy.org/tutorials/video/minimax/minimax-h3-native | native local workflow input wiring |
| S17 | https://github.com/MiniMax-AI/awesome-minimax-h3-integration | ecosystem discovery; listed integrations need their own documentation |
| S18 | https://fal.ai/models/minimax/h3-max/camera-controls/api | provider camera-control route; inspect live schema before use |

## Evidence levels

Documented: syntax/role definitions and supported controls in the cited interface.
Heuristic: recommendations about readable camera, contact, shot complexity, audio scheduling and visual polish. These are operational design choices, not numerical model performance claims.
Experimental: LoRAs, acceleration, custom long-video nodes, tiny-canvas audio extraction, literal-word hacks, or behavior reported by one user. Do not promote them into default requirements.

## Audit decisions

Keep the useful structured core. Remove unsourced numerical guarantees and implementation-wide absolutes. Correct the old statement that aspect is chosen solely in prose. Separate prompt negation from a negative-conditioning API. Preserve user speech rather than appending punctuation indiscriminately. Retain Shot 1 in single takes. Replace blanket "audio cannot be alone" with interface routing. Permit source words for exact reuse; recommend distinct words only when clarifying timbre-only transfer.

The direct API and fal docs currently disagree on mixed keyframe/reference capability and H3 Max resolution naming. Preserve that distinction; do not invent a single universal compatibility matrix. A model's generalized research capabilities are not sufficient proof that a public API exposes every task.
