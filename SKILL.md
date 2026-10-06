---
name: minimax-h3-prompt-writer
description: Writes production-ready prompts for the MiniMax H3 video model in all modes (T2VA, I2VA, FL2VA, L2VA, Ref2VA). Use when the user wants to generate an H3 video prompt from an idea, image(s), video clip(s), or audio reference.
---

# MiniMax H3 Prompt Writer

H3 is an omni-modal video model: it generates synchronized native audio (dialogue, sound effects, music) from structured English prompts. Prompt quality is the single biggest lever on output quality. This skill turns a user request into a prompt in H3's exact trained format.

## Workflow

### 1. Classify the input mode

Ask ONE routing question only when it is truly ambiguous (an image can be a first frame, a last frame, or a reference — these mean different modes):

- **T2VA** — no reference media. Build a complete audiovisual timeline from text.
- **I2VA** — one image = the exact opening frame (0.00s). Describe forward from it.
- **FL2VA** — two images = opening frame and closing frame. Describe the physical path between them (usually one shot).
- **L2VA** — one image = the exact closing frame. Invent a plausible preceding state that lands on it.
- **Ref2VA** — images/videos/audios guide identity, style, motion, rhythm, editing, or voice, but none is a hard frame anchor (or a source video is being edited/continued).

Do NOT pick a mode because it sounds more advanced. If the user's image is clearly meant as a start frame, use I2VA even if Ref2VA is available.

Limits: up to 9 images + 3 videos + 3 audio files (max 12 files total). Prompt up to ~7,000 characters. Video 5–15s at 24fps.

### 2. Load the format reference

Read exactly ONE reference file for the chosen mode and follow it character-for-character:

- T2VA / I2VA / FL2VA / L2VA → `references/base-en.txt`
- Ref2VA → `references/ref-en.txt`

The alignment lines, field names, section order, and labels in these files are training-time strings. Copy them verbatim; do not paraphrase.

### 3. Write the prompt

Core rules (details in the loaded reference file):

- Every reference gets a numbered, named job: "Image 1 locks the face. Video 1 provides the motion. Audio 1 sets the rhythm." Say what a reference is NOT for when relevant ("Image 2 sets lighting and mood only").
- One strong beat per shot; one action and one camera move per shot. `[Shot 1]` has no timestamp; later shots use `[Shot N] At MM:SS.mmm`.
- Camera moves are natural English with type + amplitude + speed: "The camera pushes in with small amplitude at slow speed".
- Dialogue verbatim inside `<d>[Language] text.</d>` with stable speaker IDs `(S1)`, `(S2)`. Voiceover = exact phrase `says in an off-screen voiceover` + "while his lips remain completely closed". Speech crossing a cut = `<scenetrans>`; speech cut by the end = `<cutoff>`. End every spoken line with a period inside `</d>` — without it, the model mumbles.
- Visible on-screen text in double quotes, verbatim, never translated. Quotes are for printed text; `<d>` is for what characters say.
- `overall_soundscape`: 1–4 sentences of ambience + physical sounds (no dialogue). `non_diegetic_music`: instrumentation, tempo, dynamics — NO abstract mood words. Write `N/A` explicitly when absent.
- Sync sound to picture with "as", "when", "then": "a loud cork pop exactly as the cork flies".
- End every `<d>` line and field properly; preserve identity details explicitly (list the features that define a face/product, not just "the same person").
- Fill both sound fields. H3 always generates audio; an empty field means the model chooses for you.

### 4. Duration, aspect, resolution

- Aspect ratio is chosen IN the prompt (9:16 / 3:4 / 1:1 / 4:3 / 16:9) — compose for the frame that ships.
- Rough segment budget (24fps, `MM:SS.mmm` cut points must fit the clip length): ~2–3 segments for 5s, 3–4 for 8s, 4–5 for 10s, 5–8 for 15s.
- In FL2VA/L2VA the alignment timestamp S.SS = clip duration to exactly two decimals (frames ÷ 24, e.g. 124 frames = 5.17).
- Faces: prefer close/medium shots. Wide shots with small faces distort badly at any resolution.

### 5. Validate before output

Run the mechanical checklist below. If any check fails, fix the prompt silently — never show the checklist or commentary in the final output.

Mechanical checks:
- [ ] Correct alignment line for the mode, first line, followed by one blank line (base modes) / six sections in order (Ref2VA)
- [ ] The three core fields present, exact names, exact order
- [ ] Shot timestamps strictly increasing and within clip duration; `[Shot 1]` has no timestamp
- [ ] Every `<d>` tag closed, has a language tag, ends with `. ? !` inside `</d>`; speaker IDs stable
- [ ] Every reference file has a numbered job; labels mean the same thing everywhere they appear
- [ ] On-screen text in double quotes; no abstract mood words in `non_diegetic_music`
- [ ] Total length safely under ~7,000 characters

### 6. Output

Output ONLY the formatted prompt. No commentary, no explanations, no markdown fences unless the user asks.

### 7. Iteration mode (optional)

If the user pastes a generated clip's failure description, load `references/troubleshooting.md`, diagnose symptom → cause, and emit a localized repair prompt: reuse the good clip as `<Video 1>` reference (video editing), specify exactly what changes and what must stay identical, and name the defects precisely (not "fix it" but "the clock reads 4:02; it must read 4:03").

## Environment rules

- Local / ComfyUI: CFG=1 means negative prompts have NO effect — "no subtitles" adds subtitles. Write bans as positives ("the sign above the door is blank"). Scope exclusions via `retention_analysis` in Ref2VA.
- Hosted API (fal, Pixo, etc.): an explicit exclusion list at the end of the prompt works well.
- Lower resolutions follow prompt structure better; iterate at 352–416p, then regenerate the chosen take at target resolution using the low-res clip as reference.
