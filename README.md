# MIDIWORX

MIDIWORX is a music analyzing and synthesizing application. It utilizes machine learning techniques to critique music files and creates MIDI files based on the analysis.

This code is licensed under the GPL 3.0 license and was developed with the assistance of AI and is copyright 2023 Nick Susco II. Users are permitted to use this source code for educational, entertainment, and professional purposes but are strongly encouraged to colloborate on the original project and startup MIDIWORX. This license contains no warranty, and is given for free on an AS IS basis. Please.use resposnibly amd preferably for the betterment of all living things on Planet Earth and The Universe.

MIDIWORX | SUSCONET Creator Nick Susco II welcomes music indusyry professionals to provide their constructive feedback and be involved in the evolution of the applicaton.
If youre interested in being involved in a substaintial way, please contact Nick at susconet@outlook.com | amazingsound6@gmail.com

## Installation

Firstly, clone the repository.
```bash
git clone https://github.com/MIDIWORX/MIDIWORX.git
```
Then install the necessary dependencies.
```bash
pip install -r requirements.txt

## Usage

# To evaluate a music file
score = critique_music('path_to_music_file')

# To create a midi file
features = analyze_music('path_to_music_file')
midi = create_midi(features)

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[GNU v3.0](https://choosealicense.com/licenses/gpl-3.0/)

#### requirements.txt

keras==2.4.3
numpy==1.20.2
pandas==1.2.4
scikit-learn==0.24.1
librosa==0.8.0
MIDIUtil==1.2.1
pygame==2.0.1
