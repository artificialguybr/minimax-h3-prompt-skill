# Authored examples

These are prompt recipes, not rendered benchmarks. Settings belong outside the prompt. Core reference grammar/examples in base-en.txt and ref-en.txt remain usable.

## T2VA: premium product detail, 6 s

Settings: text only; 16:9. Adapt to requested brand assets rather than inventing a real logo.

integrated_multimodal_description: [Shot 1] A live-action macro product shot frames an unbranded matte black watch on a charcoal stone surface. A large soft light from camera left creates a long reflection across the glass; a narrow backlight outlines the brushed steel bezel. The camera pushes in with small amplitude at slow speed as the second hand advances clockwise across the cream dial. The watch and stone remain stationary. The final composition centers the bezel and crown, with crisp material detail and an uncluttered background.

overall_soundscape: A faint mechanical tick accompanies the second hand in a quiet studio environment.

non_diegetic_music: Sparse low piano notes with a slow pulse, gently fading before the end.

## I2VA: natural Brazilian UGC, 8 s

Settings: supplied image is first_frame; aspect follows image. Assumption: image depicts an adult woman holding a mug in a kitchen. Inspect before using.

For the target video, at 0.00 seconds into the target video, <Picture 1> (from [Shot 1]) is fully referenced.

integrated_multimodal_description: [Shot 1] Preserve the ordinary phone-video style, the adult woman's appearance, clothing, mug and kitchen framing in <Picture 1>. Available window light remains soft and uneven. The camera has slight natural handheld drift at the original height. The woman with a conversational mid-pitched voice (S1) speaks Brazilian Portuguese clearly and casually: <d>[Portuguese] Hoje eu só queria um café e cinco minutos de paz.</d> She briefly glances at the mug, then looks back toward the camera with a small smile. After the line, her lips rest closed and she holds the mug steadily through the final beat.

overall_soundscape: Faint kitchen ambience and a distant street sound remain under the voice. Her sleeve rustles as she adjusts her grip.

non_diegetic_music: N/A

## FL2VA: opening a notebook, 8 s hosted

Assume matching endpoint images, same adult hands, notebook and desk. Use 8.00 for this hosted contract; a local frame-count workflow must substitute its resolved duration.

How the reference pictures align with the target video — Picture 1 (from Shot 1) aligns with the 0.00-second mark of the target video; Picture 2 (from Shot 1) aligns with the 8.00-second mark of the target video.

integrated_multimodal_description: [Shot 1] Retain the overhead framing, warm desk light, hands and blue notebook in Picture 1. The camera holds a static shot. The left hand keeps the notebook base flat against the desk. The right fingers grasp the cover's outer edge and lift it upward, rotating it around the spine toward screen-left. The pages stay aligned as the cover settles onto the desk. The hands ease into their final positions, reaching the open notebook arrangement and composition in Picture 2 before the clip ends. Hold the settled final arrangement briefly.

overall_soundscape: Fingertips touch the cloth cover, followed by a soft hinge creak, paper rustle and a muted cover contact with the desk.

non_diegetic_music: N/A

## L2VA: product reveal, 6 s hosted

Assume final image is a closed rectangular jewelry box centered on a table. The opening camera is wider; do not invent a lid-open state if the final image does not support it.

How the reference pictures align with the target video — <Picture 1> (from [Shot 1]) aligns with the 6.00-second mark of the target video.

integrated_multimodal_description: [Shot 1] A live-action tabletop shot begins wider than <Picture 1>, showing the same closed jewelry box centered on the same table. Preserve the box shape, surface, lighting and background seen in the final image. The camera pushes in with small amplitude at slow speed while the box remains stationary. The frame gradually tightens to the camera angle, spacing and composition in <Picture 1>, then settles at the final framing before the end.

overall_soundscape: Quiet indoor ambience remains steady throughout.

non_diegetic_music: N/A

## Ref2VA: identity plus motion transfer, 8 s

Assets: image 1 = adult dancer identity/outfit; video 1 = one short sideways dance step, not identity or scene. Verify the referenced step before adapting.

subject_definitions:
<Subject 1> is the adult dancer in <Picture 1>, retaining the face, short curly hair, rust-red jacket and dark trousers. The movement comes from the lateral step in <Video 1>.
<Video 1> provides only the lateral step's timing and body movement, not its performer identity, background or camera.

summary:
[reference generation] <Subject 1> performs the step referenced from <Video 1> in a plain rehearsal room.

retention_analysis:
<Subject 1> (appears in [Shot 1]): fully_preserved - the defined identity, hair and clothing are retained.
<Video 1> (motion structure): partially_preserved - retain the selected step and timing, replacing the performer and scene.

detailed_description:
The target uses natural rehearsal footage with soft side-window light and a restrained neutral palette.
[Shot 1] A static full-body view frames <Subject 1>, the adult dancer with short curly hair, a rust-red jacket and dark trousers, centered against a plain pale wall. The floor and feet are visible. Starting from the reference step's preparatory pose, the dancer transfers weight onto the left leg, steps laterally toward screen-right with the right foot, and brings the left foot beside it, matching the selected motion's pace and torso movement in <Video 1>. The feet make clear floor contact; the jacket moves with the body. The camera remains at waist height and the body stays fully inside the frame. After the step, the dancer settles with weight evenly supported and holds a relaxed stance. Only the selected movement is transferred; the source performer, location, soundtrack and camera are replaced by this target setup.

overall_soundscape:
Soft shoe contacts and jacket rustle occur with the step over quiet rehearsal-room ambience.

non_diegetic_music:
N/A

## Ref2VA: targeted edit with sound retained, 6 s

Assets: video 1 = adult presenter, tabletop and bottle; audio 1 = enabled source soundtrack. Do not create the audio role if the implementation has not enabled/supplied it.

subject_definitions:
<Video 1> is the source video to edit.
<Subject 1> is the presenter in <Video 1>, preserving face, hair, clothing and gesture timing.
<Subject 2> is the bottle and tabletop setup in <Video 1>, preserving bottle geometry, label and placement while changing the table surface.
<Audio 1> is the enabled original soundtrack from <Video 1>.

summary:
[video editing + audio reuse] The target video is an edited version of <Video 1>. Change only the tabletop to dark walnut and retain the original soundtrack.

retention_analysis:
<Video 1> (camera and timing): fully_preserved - preserve the source camera movement and clip timing.
<Subject 1> (appears in [Shot 1]): fully_preserved - preserve defined identity, clothing and gestures.
<Subject 2> (appears in [Shot 1]): partially_preserved - retain the bottle and arrangement; replace the table surface with dark walnut.
<Audio 1>: fully_copy - use the original complete soundtrack as the target final track.

detailed_description:
Retain the source's live-action look and lighting.
[Shot 1] Follow the framing and continuous camera move in <Video 1>. <Subject 1> retains the original face, hair, clothing and gestures beside <Subject 2>. Replace only the white tabletop with dark walnut throughout. Keep the bottle's silhouette, cap, label position and placement. Maintain contact shadows and consistent occlusion beneath the moving hand. Preserve the source action timing and final framing. The source soundtrack in <Audio 1> continues unchanged; introduce no new vocal source or sound layer.

overall_soundscape:
<Audio 1> is directly reused as the complete source soundtrack, including its ambience and physical sounds.

non_diegetic_music:
N/A

If the actual original soundtrack contains score, reflect that reuse in the music field rather than claiming N/A. If it contains dialogue, inspect and transcribe the exact words into the shot description; do not invent them. This example assumes ambience/SFX only.

## Ref2VA: voice timbre with new Portuguese dialogue, 8 s

Assets: image 1 = adult person; audio 1 = clean timbre sample. No copied track is requested.

subject_definitions:
<Subject 1> is the adult person in <Picture 1>, retaining facial identity, hairstyle and clothing.
<Audio 1> is the voice-timbre reference for <Subject 1> (S1).

summary:
[reference generation + audio reference] <Subject 1> delivers a short Brazilian Portuguese line using the vocal timbre of <Audio 1>.

retention_analysis:
<Subject 1> (appears in [Shot 1]): fully_preserved - retain the defined identity, hair and clothing.
<Audio 1>: reference - use the timbre, not the sample's original words or waveform.

detailed_description:
Use natural live-action portrait footage with soft window light and a quiet neutral background.
[Shot 1] A static medium close-up frames <Subject 1> from chest to head, face clearly visible. <Subject 1> (S1), using the timbre in <Audio 1>, speaks Brazilian Portuguese at a relaxed conversational pace: <d>[Portuguese] Pode começar pequeno. O importante é começar.</d> The head remains mostly forward with subtle natural expression and readable mouth movement. After speaking, the lips rest closed and the person gives a small reassuring smile. Retain the face, hairstyle and clothing from <Picture 1>; this image provides identity rather than an exact opening composition. The sample recording is used for voice character only, with the target line replacing its words.

overall_soundscape:
Quiet indoor ambience remains beneath the voice.

non_diegetic_music:
N/A

## Additional task patterns

- Documentary: T2VA or image/reference route; observational scene with one readable action; separate narrator S1; exact `<d>[Language]` script; lips of visible non-speaking people closed; explicit natural ambience and score policy.
- Singing: define visible performer and S1; exact lyrics inside `<d>`; characterize melody/delivery outside; specify whether the instrumental is diegetic, audience-only, or reused. Fit to actual recording duration.
- Multi-shot: `[Shot 1] ... [Shot 2] At 00:04.000, ...`; preserve speaker ID; use both `<scenetrans>` connection markers if the same line crosses the cut.
- Continuation: source-video role; summary starts `[video continuation]`; describe tail state then only new action. Add audio-reference/reuse relationships only when actually used.
- Audio reuse: distinguish full final track from partial layers; full reuse excludes added ambience/music unless the relationship becomes partial.
- Graphics: specify fixed layout and one clear transformation, such as a ring expanding into a circle and settling; render exact titles/logos in code or post when required.
- Multiframe: map each supplied frame to a verified timeline node/endpoint; describe intervening changes; never imply direct MiniMax V2 accepts mixed reference and first_frame roles.
- Control/inpainting: provide the actual patch/control video/mask. Describe the desired appearance or local replacement; do not pretend an edge/depth instruction in text activates a control input.
