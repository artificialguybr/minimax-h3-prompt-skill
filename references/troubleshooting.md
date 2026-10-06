Troubleshooting table: symptom -> cause -> fix (compiled from community tests, official discussions, and platform guides)

FAILURE: Output ignores my alignment line / keyframes drift
CAUSE: The alignment line was paraphrased. H3 was trained on exact strings.
FIX: Copy the alignment line character-for-character. I2VA must be exactly:
  For the target video, at 0.00 seconds into the target video, <Picture 1> (from [Shot 1]) is fully referenced.
FL2VA/L2VA timestamps must be the clip duration to exactly two decimals (frames/24; 124 frames = 5.17).

FAILURE: FL2VA/L2VA produces a morph or warp instead of motion
CAUSE: Two static descriptions ("the closed notebook. then the open notebook.") give the model two states and no transition.
FIX: Write the physical arc between states with intermediate changes, and end with a "landing" sentence: "...settles into the exact pose, spacing, and composition established by <Picture 2>."

FAILURE: Dialogue is gibberish / wrong language / mumbled
CAUSE: Line not verbatim, summarized ("she says something comforting"), too long for the shot, or missing final period.
FIX: Write the exact line inside <d>[Language] ...</d>; keep it speakable within the shot (read it aloud); ALWAYS end with a period before </d> - without it the model mumbles.

FAILURE: Lip-sync drifts or voice keeps talking past the line (local/ComfyUI)
CAUSE: Silence in the reference audio gets filled with a shuffled version of the reference voice.
FIX: Trim the reference audio to match the expected length of the spoken lines, or force continuous speech in the prompt.

FAILURE: "No subtitles / no logo" made it WORSE (local/ComfyUI)
CAUSE: CFG=1 means there is no negative branch; a negative prompt has no effect and "no subtitles" registers subtitles as content.
FIX: Write what SHOULD be there ("the sign above the door is blank"), or scope exclusions via retention_analysis in Ref2VA. On hosted APIs (fal, Pixo), an explicit exclusion list at the end of the prompt works.

FAILURE: Faces distorted
CAUSE: Wide shots with small faces in frame - H3 distorts them at any resolution.
FIX: Compose faces in close/medium shots. Keep the face large in the frame.

FAILURE: Prompt adherence poor at high resolution (local)
CAUSE: At 768p adherence to shot structure/angles drops dramatically vs 352-416p.
FIX: Iterate at low resolution; use the best low-res clip as reference and regenerate at target resolution.

FAILURE: Chained continuation repeats the first clip's motion / degrades each generation
CAUSE: Reference is stronger than instruction; each chained generation compounds drift.
FIX: Generate independent clips and cut them in an editor (won 3/3 in a blind 3-seed test), or use Ref2VA video editing with explicit per-change instructions paired with explicit stability requirements.

FAILURE: Model silently changed my scene (removed blood, swapped elements) with no error
CAUSE: Content-policy "partial refusal" - it keeps the composition and alters the flagged element. Error 1026 = input-side block, 1027 = output-side.
FIX: Describe the sensitive element less literally, avoid real celebrity names/film titles (heaviest trigger), keep the composition, change the flagged detail.

FAILURE: Audio quality bad despite passing machine QC (WER, CLAP)
CAUSE: Machine metrics miss audio artifacts; Turbo LoRAs degrade audio.
FIX: Final audio pass/fail is always human listening. Drop Turbo LoRAs for audio-critical shots.

FAILURE: Conflicting structure - "one continuous shot" plus multiple cuts; camera and action both moving in every sentence
CAUSE: Contradictory or overpacked instructions.
FIX: One action and one camera move per shot. Never request one continuous shot and multiple cuts. Fit dialogue to shot length.

FAILURE: Too many moving parts at once (new character + complex motion + dialogue + cuts all in one pass)
CAUSE: The model solves one hard problem well, not four.
FIX: Stage it: Pass 1 character+scene (static), Pass 2 add motion, Pass 3 add voice, Pass 4 cuts/storyboard, Pass 5 final. Repair beats regenerate: reuse the good clip via Modify Video / Ref2VA editing and specify exactly what changes ("the clock reads 4:02; it must read 4:03") and what stays identical.

FAILURE: Physical interaction looks wrong (pouring, stacking, tool use)
CAUSE: H3's physical reasoning succeeds ~42% of the time; it breaks contact dynamics, geometry, state transitions.
FIX: Simplify the interaction, describe contact explicitly ("her fingers close around the handle"), prefer one interaction per shot, and plan a repair pass.

QUICK PRE-FLIGHT (run before submitting any prompt):
[ ] Mode correct? (image-as-start = I2VA, not Ref2VA)
[ ] Every reference has a numbered, named job (and an explicit "only" exclusion if needed)
[ ] Alignment line verbatim, timestamp with two decimals
[ ] Fields in exact order; N/A written explicitly where music/soundscape absent
[ ] All <d> blocks: language tag, verbatim line, closing period
[ ] Speaker IDs stable; voiceover phrase exact; <scenetrans>/<cutoff> where needed
[ ] On-screen text in double quotes, verbatim
[ ] Camera vocabulary from the closed set; type+amplitude+speed
[ ] Shot count fits duration (5s: 2-3, 8s: 3-4, 10s: 4-5, 15s: 5-8)
[ ] Faces framed close/medium; aspect ratio stated in prompt
[ ] Total < ~7,000 characters
