# Audio, speech and synchronization

Use the base/ref guides for grammar. The rules below are planning heuristics unless a source ID is given.

## Speech timing

Allocate each speaking window after action onset, before the cut, and with a pause for reaction. Read the actual line aloud, or measure a supplied recording. A rough planning range of 2–3 words/s can flag an overloaded English/Portuguese line; accent, dramatic pauses, singing, and other languages change it. This is not an H3 limit. Word counts are particularly unsuitable for languages that do not separate words with spaces.

Do not impose the old twenty-words-per-fifteen-seconds cap. Never silently shorten locked dialogue, translate it, or change user punctuation. Split shots or clips when needed. Natural multi-sentence speech is allowed; separate blocks when the timing or speaker changes, not because two sentences are categorically forbidden.

Specify language inside `<d>` and accent/delivery outside it. For Portuguese: use `[Portuguese]` and specify Brazilian Portuguese and the desired accent in the speaker description. Keep colloquial phrasing when the user wants it. Describe timbre, pitch, pace and performance once, then retain the speaker ID.

Give only vocal sources IDs; assign them by first vocal event, not by reference-image order. Subject 3 can be S1. For a shared voice cue in a reused track, avoid inventing a new visible speaker. For turn-taking, say who speaks and what the listener does; listeners can keep their lips closed during the other person's line.

## Voiceover and lip sync

Use the documented off-screen voiceover phrase and closed-lips instruction when an on-screen character should not deliver narration. A separate invisible narrator needs no invented visible mouth. Keep lip-sync-critical faces sufficiently large and readable; a static or gentle camera is a useful starting point. Head movement is permissible, but heavy rotation/occlusion increases ambiguity.

Cross-cut speech requires continuity wording and `<scenetrans>` connection markers. Use `<cutoff>` only for intentional interruption at the video ending. Preserve exact line content across the split; do not repeat the full line in both shots.

## Choose the audio relationship deliberately

| Intent | Ref2VA relationship | Instruction |
| --- | --- | --- |
| Keep the entire source final soundtrack | fully_copy | Name the track as the complete soundtrack; request no additional layers |
| Keep dialogue but replace music/add SFX | partially_copy | Identify retained layer or interval and new layers |
| Same voice, new words | reference | Bind timbre to the correct speaker; supply the new exact line |
| Similar musical arrangement | reference | Describe instruments, pulse and development; do not claim signal copying |
| Only broad audible character | weak_reference | Describe the similarity without implying exact timing |

These marker meanings come from the existing grammar. The prompt declares intent; exact waveform identity must be checked or ensured by external assembly. The presence of sound in a video does not automatically assign it an `<Audio N>` role in the rewrite; verify the implementation's enabled soundtrack and map it explicitly. [S14]

For voice transfer, choose a clean sample with one voice, little room noise, and representative delivery. A sample with different words can help distinguish timbre reference from track reuse, but identical words are not universally forbidden: they are appropriate when exact source dialogue is being reused. Avoid an arbitrary six-second prescription. Follow the endpoint's minimum/maximum duration and total reference budget.

For exact multilingual delivery, a recorded/TTS target line can provide a clear audible source through a supported reuse workflow. Confirm transcript, language, speaker and sync by listening. Do not assume changing only a language tag translates the actual words.

## Sound design

Write diegetic events where they happen: "As the latch closes, a short metallic click occurs." Summarize the shared acoustic environment in overall_soundscape. Specify foreground vs distant sound and acoustic character when helpful. Do not demand exact dB, LUFS, pan automation or beat-perfect placement from text alone.

For no score, use `non_diegetic_music: N/A`. For fully silent output, both audio fields can be `N/A` and visual description must avoid conflicting speech/music requests. A no-score scene can still have wind, footfalls, breath and dialogue. Room ambience is valid; the word "tone" is not categorically banned, and official examples use it.

For audience-only music specify instruments, tempo/pulse, dynamic arc and endpoint. For visible singing/instruments/radio describe the diegetic source and exact lyrics in the shot description. Do not duplicate lyrics in the soundscape/music fields.

## Music and long-form work

Per-clip generated scores can change key, timbre and loudness. When a continuous music bed matters, generate or license one track for post-production and set per-clip score to N/A; preserve scene-specific SFX/ambience if wanted. When native soundtrack is the creative goal, direct continuity explicitly and audition joins. Neither route is universally mandatory.

`target_audio_url` on the verified fal text endpoint replaces the final soundtrack; distinguish this attachment from generative voice reference and from demonstrated lip synchronization. [S9]

## Listen before approval

Listen at normal speed through headphones and ordinary speakers. Check exact words, speaker identity, accent, unwanted speech, consonants, clipped endings, tempo, music dominance, artifacts and action/SFX timing. Machine transcription can aid review but cannot replace listening. If no generation was performed, report only prompt readiness.
