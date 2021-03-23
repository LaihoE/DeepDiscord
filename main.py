from pathlib import Path
import os

paths={
"scorer": os.path.join(Path(__file__).resolve().parents[1],'Discordbot','deepspeech','deepspeech-0.9.3-models.scorer'),
"pbmm": os.path.join(Path(__file__).resolve().parents[1],'Discordbot','deepspeech','deepspeech-0.9.3-models.pbmm')
}

os.system(f'cmd /c python mic_vad_streaming.py -m {paths["pbmm"]} -s {paths["scorer"]}')