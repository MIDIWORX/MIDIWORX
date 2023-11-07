#!/bin/bash

#Stop script
#Please remove "stop script" and this  entire line of code prior to execting your script. 

# Create directories for project
mkdir -p project/models project/audio_analysis project/natural_language_processing project/recommendation_engine project/security project/cache project/tracking

# Create Python files
touch project/app.py
touch project/models/__init__.py
touch project/models/music_data.py
touch project/audio_analysis/analysis.py
touch project/natural_language_processing/natural_language.py
touch project/recommendation_engine/recommendation.py
touch project/security/security.py
touch project/cache/__init__.py
touch project/tracking/__init__.py

# Create Cache files
touch project/cache/audio_features_cache.pickle
touch project/cache/recommendations_cache.pickle
touch project/cache/metadata_cache.pickle

# Create log file
touch project/tracking/advertising_trackers.log

# Create CSV, txt, Docker and README files
touch project/music_data.csv
touch project/requirements.txt
touch project/Dockerfile
touch project/README.md

end script

#appdir_magic.sh
