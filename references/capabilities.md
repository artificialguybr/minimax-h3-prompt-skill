# Capability and interface routing

Checked 2026-10-06. Recheck the exact destination for execution. Source IDs refer to sources.md. Never transfer a provider's schema to another provider.

## Core tasks

T2VA, I2VA, FL2VA and L2VA use the base/keyframe family. Ref2VA uses the reference family and supports language-defined identity, style, action, camera, sound, editing, and continuation relationships. Joint video/audio generation makes audiovisual events directable together; it does not imply exact editorial control. [S1, S2]

## Direct MiniMax V2 API

Use `model`, `content`, `resolution`, `duration`, and `ratio`. The non-empty text item is required. Media item types are `image_url`, `video_url`, `audio_url`; image roles are `first_frame`, `last_frame`, `reference_image`, with `reference_video` and `reference_audio` for other media. Never mix endpoint roles with reference roles. [S3]

| Model | Duration | Resolution |
| --- | --- | --- |
| MiniMax-H3 | integer 4–15 s | 768P, 2K |
| MiniMax-H3-Max | integer 5–15 s | 480P, 768P |

T2VA requires a concrete `ratio`. I2VA follows the image; a concrete ratio is ignored. R2VA supports adaptive or concrete ratio. Image preparation therefore matters more than a conflicting prose ratio. [S3]

Use the current schema for upload limits. Documented counts: nine images, three videos, three audios; each video/audio 2–15 s, aggregate 15 s per modality. Apply the overall twelve-file limit documented by the model card. [S3, S1]

Do not attach unsupported sampler/seed/negative-prompt keys to this request. Inspect child schemas before constructing nested URL items; writing a role in prose cannot substitute for wiring it.

## Local Diffusers / ComfyUI

Diffusers distinguishes `t2va`, `fl2va`, and `ref2va`; first-only/last-only are keyframe variants. Its current modular pipeline has no `negative_prompt` or `guidance_scale`. This is not proof that every wrapper lacks similarly named fields. [S6]

Frame-count workflows use 24 fps and a `17*n+5` grid. Compute the resolved count and align against count / fps. Do not replace an 8-second hosted alignment with 5.17 because a local example happens to use 124 frames. Record checkpoint, workflow version, dimensions, steps, shifts, seed/generator state, media order and hardware for comparisons. Identical seeds are useful controls within a fixed stack, not universal reproducibility guarantees. [S6]

Smaller local canvases can reduce cost. They do not establish better adherence, and the approved final must still be reviewed. Preserve actual reference fps/sample rate; losing a video's rate can change apparent motion. [S6]

Use runtime docs for steps and flow shifts; reference configurations use 50 steps, video shift 12, audio shift 3. Treat these as a starting configuration, not prompt grammar. [S7]

## fal H3 Max additions: provider-specific

The current reference endpoint exposes reference lists, opening/closing images, and an optional middle image. Middle-frame guidance requires opening and closing images and native 480P/768P. This differs from MiniMax V2's mutually exclusive role combinations. Revalidate before submission. [S8]

The text endpoint exposes `prompt_expansion_mode` (`disabled`, `balanced`, `quality`), seed, and `target_audio_url`. The latter attaches/replaces the final soundtrack, trims to output duration or pads silence; it is not evidence that generated lips follow that exact recording. A/B-test expansion when precise wording matters. Do not generalize its resolution options to direct MiniMax. [S9]

The extension endpoint takes an existing video and a description of new footage, with separate `duration`, `output` (`extended`/`continuation`), seed and `enable_prompt_expansion`. Its documented source range differs from ordinary reference limits. Match transition state, not the source's whole plot. [S10]

## Advanced conditioning: available only when wired

| Workflow | Required evidence/input | Prompt obligation |
| --- | --- | --- |
| Multiframe reference | Timeline-capable native node | Map each image to its intended point, describe the bridge |
| Pose/depth/edge control | Fun ControlNet Union patch and control video | Describe target appearance, retain supplied movement/structure |
| Masked inpainting | Supported patch, source video, aligned mask | Restrict change to target region; protect background and motion |
| Camera trajectory endpoint | Current provider schema and camera controls | Keep text consistent with the supplied path |
| Continuation | Source tail or actual extend endpoint | Preserve terminal pose, direction, momentum and audible state |

ComfyUI documents multiframe reference and Canny/Depth/HED/MLSD/Pose plus masked video inpainting. These are integrations, not new universal prompt-only modes. [S11, S12]

## Audio-only / image-only / backwards extension

The research architecture spans more tasks than the public video-generation API. Do not advertise standalone audio/image output or backwards extension as universally supported. Audio-only reference acceptance varies: the documented local Diffusers workflow requires a visual reference; the fal reference schema describes audio provided individually. Verify the chosen route instead of asserting "audio can never travel alone." [S2, S6, S8]

For unsupported tasks, provide a compatible audiovisual prompt or suggest an appropriate dedicated tool. Treat tiny-canvas audio extraction and custom long-video nodes as experimental implementation-specific workflows.

## 2K

Local base generation and hosted H3-Regenerate-2K are distinct. The latter regenerates from a base result and context; it is not conventional interpolation/upscaling. Direct hosted 2K is also available. Inspect original and refined clips for changed text, faces, motion, and sound. Never guarantee the approved low-resolution take remains identical. [S1, S4, S5]
