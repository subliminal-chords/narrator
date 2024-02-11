from bark.generation import (
    generate_text_semantic,
    preload_models,
)
from bark.api import semantic_to_waveform
from bark import generate_audio, SAMPLE_RATE
import nltk
import numpy as np
from abc import ABC, abstractmethod
from tqdm.auto import tqdm

nltk.download('punkt')

class AudioModel(ABC):
    @abstractmethod
    def generate(self, text: str, **kwargs: dict):
        raise NotImplementedError()

class Bark(AudioModel):
    def __init__(self, preset: str = "v2/en_speaker_6", temp: float = 0.6, min_eos_p: float = 0.05):
        self.temp = temp
        self.preset = preset
        self.min_eos_p = min_eos_p
    
    def generate(self, text, **kwargs):
        sentences = nltk.sent_tokenize(text)
        trailing_silence = np.zeros(int(0.25 * SAMPLE_RATE))
        pieces = []
        for sentence in tqdm(sentences):
            semantic_tokens = generate_text_semantic(
                sentence,
                history_prompt=self.preset,
                temp=self.temp,
                min_eos_p=self.min_eos_p,  # this controls how likely the generation is to end
            )
            audio_array = semantic_to_waveform(semantic_tokens, history_prompt=self.preset, silent=True)
            pieces += [audio_array, trailing_silence.copy()]
        return np.concatenate(pieces), SAMPLE_RATE
