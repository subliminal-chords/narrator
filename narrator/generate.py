from narrator.model import Bark
import argparse
from scipy.io.wavfile import write as write_wav

parser = argparse.ArgumentParser(
    description='A CLI tool to create a Generative AI-based narration from a given text file to a supported audio format.'
)

parser.add_argument(
    "--text",
    action='store',
    type=str,
    help="The input text from which to generate an Audio file."
)

parser.add_argument(
    "--file",
    action='store',
    type=str,
    help="Absolute or relative path to the input text file from which to generate an Audio file."
)

parser.add_argument(
    "--preset",
    default="v2/en_speaker_6",
    action='store',
    type=str,
    help="The Voice Preset to use for the Bark model. (For a complete list see: https://suno-ai.notion.site/8b8e8749ed514b0cbf3f699013548683?v=bc67cff786b04b50b3ceb756fd05f68c)"
)

parser.add_argument(
    "--temperature",
    default=0.6,
    action='store',
    type=float,
    help="The Generative Temperature value to use. (Lower means less creative, more predictable. Higher means more creative, less predictable. Default is 0.6.)"
)

parser.add_argument(
    "--output",
    default="output.wav",
    action='store',
    type=str,
    help="Absolute or relative path to the output file (must be a .wav file)"
)

if __name__ == "__main__":
    args = parser.parse_args()
    print(args)
    if bool(args.text) and bool(args.file):
        parser.error('--text and --file cannot be given together.')
    elif not (bool(args.text) or bool(args.file)):
        parser.error('Either --text or --file has to be given.')
    model = Bark(preset=args.preset, temp=args.temperature)
    if bool(args.text):
        pcm_audio, sr = model.generate(args.text)
    else:
        file_descriptor = open(args.file, "r")
        text_contents = file_descriptor.read()
        file_descriptor.close()
        pcm_audio, sr = model.generate(text_contents)
    write_wav(args.output, sr, pcm_audio)
