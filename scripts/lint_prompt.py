#!/usr/bin/env python3
"""Validate structured H3 prompt text; never claim to predict render quality."""
import argparse
import json
import re
from pathlib import Path

BASE = ['integrated_multimodal_description', 'overall_soundscape', 'non_diegetic_music']
REF = ['subject_definitions', 'summary', 'retention_analysis', 'detailed_description', 'overall_soundscape', 'non_diegetic_music']


def lint(text, mode, duration, max_chars=None):
    errors, warnings = [], []
    expected = REF if mode == 'ref2va' else BASE
    fields = re.findall(r'^([a-z_]+):', text, re.M)
    if fields != expected:
        errors.append(f'Expected fields in order {expected}; found {fields}')
    if duration <= 0:
        errors.append('Duration must be positive')
    if max_chars and len(text) > max_chars:
        errors.append(f'{len(text)} characters exceeds destination limit {max_chars}')
    body_field = 'detailed_description' if mode == 'ref2va' else BASE[0]
    found = re.search(rf'^{body_field}:\s*(.*?)(?=^overall_soundscape:|\Z)', text, re.M | re.S)
    body = found.group(1) if found else ''
    shots = list(re.finditer(r'\[Shot (\d+)\](?:\s+At (\d+):(\d+)\.(\d{3}))?', body))
    if not shots or [int(s.group(1)) for s in shots] != list(range(1, len(shots) + 1)):
        errors.append('Body shots must start at Shot 1 and be sequential')
    times = []
    for idx, s in enumerate(shots):
        if idx == 0 and s.group(2):
            errors.append('Shot 1 must not have a cut timestamp')
        if idx > 0 and not s.group(2):
            errors.append(f'Shot {idx+1} needs At MM:SS.mmm')
        t = 0.0 if not s.group(2) else int(s.group(2))*60+int(s.group(3))+int(s.group(4))/1000
        if s.group(3) and int(s.group(3)) >= 60:
            errors.append('Timestamp seconds component must be below 60')
        if (idx > 0 and times and t <= times[-1]) or t >= duration:
            errors.append(f'Invalid/inconsistent shot time {t}')
        times.append(t)
    if text.count('<d>') != text.count('</d>'):
        errors.append('Unbalanced dialogue tags')
    dialogue = re.findall(r'<d>(.*?)</d>', body, re.S)
    for d in dialogue:
        if not re.match(r'^\[[^\]\n]+\]\s*\S', d):
            errors.append('Dialogue needs a language tag and content')
        clean = re.sub(r'^\[[^\]]+\]\s*|<scenetrans>|<cutoff>', '', d).strip()
        if clean and clean[-1] not in '.?!':
            warnings.append('Dialogue lacks terminal punctuation; preserve locked user text')
    for idx, s in enumerate(shots):
        end = shots[idx+1].start() if idx+1 < len(shots) else len(body)
        window = (times[idx+1] if idx+1 < len(times) else duration)-times[idx]
        ds = re.findall(r'<d>(.*?)</d>', body[s.end():end], re.S)
        words = sum(len(re.findall(r'\b\w+\b', re.sub(r'\[[^\]]+\]|<[^>]+>', '', d))) for d in ds)
        if window > 0 and words/window > 3:
            warnings.append(f'Shot {idx+1}: {words/window:.1f} words/s; rehearse actual delivery')
    if re.search(r'one continuous|single continuous|single take', body, re.I) and len(shots) > 1:
        warnings.append('Continuous-take wording conflicts with several shot markers')
    first = text.splitlines()[0] if text.splitlines() else ''
    if mode in ('i2va', 'fl2va', 'l2va'):
        last = len(shots) or 1
        if mode == 'i2va':
            required = 'For the target video, at 0.00 seconds into the target video, <Picture 1> (from [Shot 1]) is fully referenced.'
        elif mode == 'fl2va':
            required = f'How the reference pictures align with the target video — Picture 1 (from Shot 1) aligns with the 0.00-second mark of the target video; Picture 2 (from Shot {last}) aligns with the {duration:.2f}-second mark of the target video.'
        else:
            required = f'How the reference pictures align with the target video — <Picture 1> (from [Shot {last}]) aligns with the {duration:.2f}-second mark of the target video.'
        if first != required:
            errors.append('Alignment sentence differs from selected mode/duration/final shot')
        if len(text.splitlines()) < 2 or text.splitlines()[1].strip():
            errors.append('Alignment sentence must be followed by a blank line')
    if mode == 'ref2va':
        defs = text.split('summary:', 1)[0]
        references = set(re.findall(r'<(?:Subject|Picture|Video|Audio) \d+>', text))
        defined_or_cited = set(re.findall(r'<(?:Subject|Picture|Video|Audio) \d+>', defs))
        if references-defined_or_cited:
            errors.append(f'Unresolved reference labels: {sorted(references-defined_or_cited)}')
        retention = text.split('retention_analysis:', 1)[-1].split('detailed_description:', 1)[0]
        if re.search(r'\(S\d+', retention):
            errors.append('Speaker IDs do not belong in retention_analysis')
    return {'errors': errors, 'warnings': list(dict.fromkeys(warnings)), 'characters': len(text)}


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('file', type=Path)
    p.add_argument('--mode', required=True, choices=['t2va', 'i2va', 'fl2va', 'l2va', 'ref2va'])
    p.add_argument('--duration', required=True, type=float, help='Effective duration; resolve local frame grid first')
    p.add_argument('--max-chars', type=int, help='Optional actual destination limit')
    a = p.parse_args()
    result = lint(a.file.read_text(encoding='utf-8').strip(), a.mode, a.duration, a.max_chars)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    raise SystemExit(bool(result['errors']))


if __name__ == '__main__':
    main()
