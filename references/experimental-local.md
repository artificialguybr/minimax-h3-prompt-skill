# Experimental / local (ComfyUI, diffusers) — comunidade, não garantias

> **Status: EXPERIMENTAL.** Tudo nesta página vem de relatos da comunidade, cards de LoRA e testes de usuários — não de garantias documentadas da MiniMax. Válido apenas no stack local indicado; valide por conta própria antes de contar com isso em produção. Não prometa esses comportamentos como fatos do modelo.

## Reprodutibilidade local

- A mesma seed amarra o sorteio de vídeo E áudio juntos — rerodar com a mesma seed reproduz o mesmo clipe e a mesma trilha (dentro do MESMO stack: fixe checkpoint, versão de workflow, dims, steps, shifts, estado do gerador e hardware antes de comparar).
- `rand_device "cpu"` ajuda reprodutibilidade entre GPUs diferentes (comportamento reportado, não garantia formal).
- Frames fecham no grid `17*n+5` do VAE (124 = 5.17s, 243 = 10.13s, 362 = 15.08s) a 24 fps.

## Speed tiers (LoRAs de aceleração — comunidade)

- Turbo-LoRA v4 a 9 steps (8 NFE); FastH3 distill de 4 steps (rejeita outras contagens); PDD 9-step.
- LoRAs de velocidade podem degradar o áudio — **ouça todo take acelerado** antes de aprovar.

## Style/behavior LoRAs com trigger words (verifique o card de cada LoRA)

- realism-people: incluir `r34l1sm` no prompt; schedule normal de 50 steps; lora_scale ~0.7.
- wushu action: `wushu_action` no INÍCIO do prompt.
- camera motion: `camera motion` no INÍCIO do prompt.
- spatial physics: descrever colisões/empilhamento/gravidade no prompt; scale ~0.4.
- Os requisitos são baseados em trigger-words — cada LoRA tem o seu; confira o card antes de usar.

## Fun Control (local, ComfyUI)

- Um ControlNet union (canny/depth/HED/MLSD/pose + inpaint/outpaint); o vídeo de controle já deve estar a 24 fps; `control_scale` 0–1 aperta a estrutura.

## Vídeos longos (encadeamento local)

- Extensão encadeada funciona em janelas; manter takes em ~4 janelas (~30–40s) — além disso aparece um "texture ratchet" medido por usuários (+~13% de sharpening fino por junção).
- O rabo do clipe anterior segue adiante como contexto latente; cortar narração longa em fronteiras de frase.
