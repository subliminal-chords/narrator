# Narrator

## Introduction

A CLI tool to create a Generative AI-based narration from a given text file to a supported audio format.

## Setup

<table border="0">
 <tr>
    <td><b style="font-size:larger">Description</b></td>
    <td><b style="font-size:larger">Command</b></td>
 </tr>
 <tr>
    <td>Clone the repository</td>
    <td>

```
git clone https://github.com/subliminal-chords/narrator.git
cd narrator
```

  </td></tr>
 <tr>
    <td>Setup the Virtual Environment</td>
    <td>

```
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

 </td></tr>
 <tr>
    <td>Generate Audio Files</td>
    <td>

```
# Use this for short-form generations.
python3 -m narrator.generate --text "..." --preset "..." --output "audio.wav"
# For long-form generations, prefer to use a text file as input.
python3 -m narrator.generate --file "..." --preset "..." --output "audio.wav"
# You can also configure the temperature hyper-parameter.
python3 -m narrator.generate --file "..." --preset "..." --output "audio.wav" --temperature 0.4
```

 </td></tr>
</table>

## Acknowledgements

* [Bark](https://github.com/suno-ai/bark) - A Generative text to natural speech model generously open-sourced by the [Suno](https://www.suno.ai/) team.
