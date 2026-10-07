# Directing for controllable output

These are production heuristics, not measured H3 guarantees. Use them to reduce ambiguity and to make review possible.

## Convert a brief into visible events

Resolve five things: what the viewer notices first; what changes; what motivates that change; what the camera reveals; what the viewer sees at the end. Replace "premium cinematic product ad" with concrete framing, light, materials and actions. Distinguish essential constraints from optional polish.

Weak: "A beautiful bottle, epic cinematic camera, high quality, ultra realistic."
Stronger: "A low medium close-up frames the amber bottle on dark slate. A large soft source from camera left creates a long edge reflection, while a narrow backlight separates the glass from the charcoal background. The camera makes one slow, shallow push toward the embossed cap as condensation rolls down the neck."

Do not add grain, shallow depth of field, slow motion, lens flare and handheld wobble by default. Each should support the requested medium. A professional medical explainer or screen demo may require crisp deep focus and static geometry.

## Shot design

- Establish composition before movement. Name foreground/midground/background when depth or occlusion matters.
- Give movement an origin, direction, speed, contact event and result. "Her right fingers close around the mug handle; the mug lifts vertically, clears the table, and stops at chest height" is more useful than "she gracefully picks it up."
- Separate camera translations from zooms. A push-in changes perspective; a zoom changes framing. State whether the subject remains centered or exits the frame.
- Leave room for action onset and consequence. A closing hold is useful for a reveal, but do not impose a fixed hold on fast-paced footage.
- Use cuts to reveal information. Do not fill every five seconds with three shots simply because a template says so.
- Specify which hand or object acts only when it matters. Excess anatomy descriptions can distract from the core event.
- For spatial relationships use a stable coordinate convention: screen-left/right, subject-left/right, near/far. Do not switch conventions mid-shot.
- For orbiting shots, describe which side becomes visible and whether the subject rotates; avoid accidental double rotation.

## First/last images

Inspect style, camera height, focal perspective, pose, prop states and lighting. If the images depict incompatible environments or identities, a plausible physical bridge may not exist. Choose an intentional transition, prepare compatible endpoints, or split into shots; do not promise a natural interpolation.

Opening pose often suggests what happens next. Describe a preparatory hold if necessary. For a closing image, work backwards from the visible final state and select an opening that can reach it in the available time. Avoid impossible object counts or unexplained wardrobe/prop changes.

Match image aspect and crop before endpoint conditioning. Keep hands and action-critical objects inside the crop. Prepare both images for the same composition unless the change in framing is intentional. Do not strengthen weak instructions by contradicting the source.

## Reference preparation

Use the minimum assets that resolve the important ambiguities. A clean close portrait helps facial identity; a full-body image helps wardrobe/body silhouette; a product image helps shape and label. More assets can also introduce inconsistent outfits, viewpoints or lighting.

For motion transfer, select a short segment where limbs and contact are visible, and distinguish motion from performer identity, scene and camera. For camera reference, distinguish camera trajectory from subject motion. Specify which rhythm/cuts matter instead of asking to copy every attribute.

If using a sheet, name panels unambiguously and identify the sheet as a planning reference. Do not ask the generated frame to display the sheet grid. Separate panels into files when ambiguity outweighs the file-budget benefit. ComfyUI documents panel-specific references, but they still need explicit correspondence. [S13]

## Styles and task recipes

| Task | Useful constraints | Typical failure to avoid |
| --- | --- | --- |
| Product/brand ad | silhouette, finish, label position; motivated light; one hero action; safe area for later titles | mutable logos, invented claim text, unstable label geometry |
| Natural UGC | ordinary location, plausible phone height, available light, modest handheld drift, conversational delivery | automatic beauty lighting, fashion-model casting, exaggerated camera wobble |
| Documentary | believable environment/action, restrained observation, specific off-screen narration, natural sounds | treating a reconstruction as evidence; adding dramatic invented details |
| Narrative | screen direction, eyelines, prop handoffs, actor performance and emotional state changes | continuity resets, speaking actor swaps, confusing geography |
| 2D animation | outline thickness, flat shading, palette, character proportions, intentional cadence | texture/style drifting toward 3D or photorealism |
| Clay/stop motion | tactile surface, handmade shapes, discrete movement cadence, consistent light | unwanted smoothing or rubbery continuous deformation |
| Motion graphics | fixed layout, hierarchy, small object count, explicit scale/opacity/path changes | excessive simultaneous text/layout transformation |
| UI/software | approved screen input, fixed geometry, one visible interaction, readable large elements | fake cursor actions, changing copy, invented app screens |
| Dance/action | readable full body, motion reference/control where available, grounded contacts | limb occlusion, contradictory motion plus complex camera |

Keep precise copy, logo vectors, charts and UI text as composited or code-rendered elements when they must be exact. H3 can supply moving backgrounds, textures, cinematic transitions or approved visual shots. Do not imply it emits SVG or editable vector animation.

## Continuity across clips

Maintain a compact continuity contract: identity phrase; outfit; prop shape/color/hand; scene geometry; light direction; screen direction; lens/framing style; vocal description; music policy. Reuse the contract, not the entire previous prompt. Provide only the references needed by each clip.

For a continuous action, preserve ending pose, velocity, camera motion and sound tail at the join. For an editorial cut, generate independently and preserve continuity anchors. Repeated generative edits can drift; there is no documented universal four-window cap or fixed sharpening rate.

## Iteration

Start with the complete audiovisual intent, simplified where needed. Do not universally force five sequential edit passes: every pass may alter successful parts. If a clip succeeds visually but fails speech, try a targeted audio/lip-sync reference route or external dialogue production. If a clip fails globally, simplify and regenerate rather than serially repairing everything.
