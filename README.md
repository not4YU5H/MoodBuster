# MoodBuster

MoodBusters

Emotion Detection Using Speech
Project prepared and documented: Ayush Jain

School of Computer Engineering, CSE , KIIT, 
20051827@kiit.ac.in


Abstract- MoodBusters is a machine learning project based on Sentiment analysis in Python using scikit-learn library. The project includes training a model using datasets like RAVDESS, TESS, Emodb and some custom data which include voice recordings of various actors which are categorized according to the emotion in which they are speaking. Using this model, live emotion detection is performed by recording the user’s voice and detecting the emotion in which he/she is speaking which in turn can be used in various real-world applications. In this project, we have integrated the Spotify API and we play some sample music based on recognized emotion. 

Introduction

This project aims at live speech emotion recognition using scikit-learn. Humans are very social beings and the means of communication they mostly use is speech. While communicating via speech, emotion plays an important role. It has such an effect that it can completely change the meaning of the words being spoken and sometimes the speaker himself isn’t able to figure out in which emotion he is speaking, which in turn can cause a lot of problems. 
So, from this, we know that emotion plays an important role in our day-to-day life. This brings us to the importance of our project MoodBusters which aims on SER which helps the users to know the emotion in which they are speaking. This data can be used in various fields like:
The medical field: In the world of telemedicine where patients are evaluated over mobile platforms, the ability for a medical professional to discern what the patient is actually feeling can be useful in the healing process.
Customer service: In call center conversation may be used to analyze the behavioral study of call attendants with the customers which helps to improve the quality of service.
Recommender systems: Can be useful to recommend products to customers based on their emotions towards that product.
 
Basic concepts/ Technology used

In this project we have used a suitable scikit-learn model to train the model in Python. The model is trained using various datasets. Then, the trained model is used to recognize the emotion in which the user speaks which is captured through the default microphone. Then, the resulting emotion is used to play some sample music through Spotify using the Spotify API.

Note : 
i) In this particular project, we recognize only 3 emotions i.e happy, neutral, sad but it can be used to recognize more emotions but requires more computational power and accuracy may also decrease accordingly.
ii) The Spotify developer account used in this project is personal. So, if someone wishes to use this code, the credentials need to be changed in the play_music.py file.

Python version required : 3.6+

Python Packages used:

*) tensorflow : tensorflow is an end-to-end open source platform for machine learning. It has a comprehensive, flexible ecosystem of tools, libraries and community resources that lets researchers push the state-of-the-art in ML and developers easily build and deploy ML powered applications.

*) librosa : librosa is a python package for music and audio analysis. It provides the building blocks necessary to create music information retrieval systems.

*) numpy : NumPy is the fundamental package for scientific computing in Python. It is a Python library that provides a multidimensional array object, various derived objects (such as masked arrays and matrices), and an assortment of routines for fast operations on arrays, including mathematical, logical, shape manipulation, sorting, selecting, I/O, discrete Fourier transforms, basic linear algebra, basic statistical operations, random simulation and much more.

*) pandas : pandas is a software library written for the Python programming language for data manipulation and analysis. In particular, it offers data structures and operations for manipulating numerical tables and time series.

*) soundfile : SoundFile can read and write sound files. File reading/writing is supported through libsndfile, which is a free, cross-platform, open-source (LGPL) library for reading and writing many different sampled sound file formats that runs on many platforms including Windows, OS X, and Unix.

*) wave : The wave module provides a convenient interface to the WAV sound format. It does not support compression/decompression, but it does support mono/stereo.

*) sklearn : Scikit-learn (formerly scikits.learn and also known as sklearn) is a free software machine learning library for the Python Programming Language. It features various classification, regression and clustering algorithms including support-vector machines, random forests, gradient boosting, k-means and DBSCAN, and is designed to interoperate with the Python numerical and scientific libraries NumPy and SciPy.

*) tqdm : tqdm is a library in Python which is used for creating Progress Meters or Progress Bars. tqdm got its name from the Arabic name taqaddum which means 'progress'. Implementing tqdm can be done effortlessly in our loops, functions or even Pandas.

*) matplotlib : Matplotlib is a plotting library for the Python programming language and its numerical mathematics extension NumPy. It provides an object-oriented API for embedding plots into applications using general-purpose GUI toolkits like Tkinter, wxPython, Qt, or GTK. 

*) pyaudio : PyAudio provides Python bindings for PortAudio, the cross-platform audio I/O library. With PyAudio, you can easily use Python to play and record audio on a variety of platforms.

*) spotipy : Spotipy is a lightweight Python library for the Spotify Web API. With Spotipy you get full access to all of the music data provided by the Spotify platform.

Datasets used:

*) RAVDESS : The Ryson Audio-Visual Database of Emotional Speech and Song that contains 24 actors (12 male, 12 female), vocalizing two lexically-matched statements in a neutral North American accent.
*) TESS : Toronto Emotional Speech Set that was modeled on the Northwestern University Auditory Test No. 6 (NU-6; Tillman & Carhart, 1966). A set of 200 target words were spoken in the carrier phrase "Say the word _____' by two actresses (aged 26 and 64 years).
*) EMO-DB : As a part of the DFG funded research project SE462/3-1 in 1997 and 1999 we recorded a database of emotional utterances spoken by actors. The recordings took place in the anechoic chamber of the Technical University Berlin, department of Technical Acoustics. Director of the project was Prof. Dr. W. Sendlmeier, Technical University of Berlin, Institute of Speech and Communication, department of communication science. Members of the project were mainly Felix Burkhardt, Miriam Kienast, Astrid Paeschke and Benjamin Weiss.
*) Custom : Some unbalanced noisy dataset that is located in `data/train-custom` for training and `data/test-custom` for testing in which you can add/remove recording samples easily by converting the raw audio to 16000 sample rate, mono channel (this is provided in `create_wavs.py` script in ``convert_audio(audio_path)`` method which requires [ffmpeg](https://ffmpeg.org/) to be installed and in *PATH*) and adding the emotion to the end of audio file name separated with '_' (e.g "20190616_125714_happy.wav" will be parsed automatically as happy)




Algorithms Used:

Classifiers:
- SVC
- RandomForestClassifier
- GradientBoostingClassifier
- KNeighborsClassifier
- MLPClassifier
- BaggingClassifier

Regressors:
- SVR
- RandomForestRegressor
- GradientBoostingRegressor
- KNeighborsRegressor
- MLPRegressor
- BaggingRegressor
Implementation and results 

After completing all the required executions, the file test.py can be directly run to trigger all the required imports and processes and the user’s microphone is triggered which is used to record the user’s voice. After required analysis, the accuracy of the trained model and recognized user’s emotion gets printed. Then, the user is asked if he/she wants to hear a song based on the recognized emotion. The trained model reaches approximately 85% accuracy. 
Conclusion
MoodBuster aims at live speech emotion recognition and can be a gamechanger in many fields. Though the accuracy and results are not yet that promising, more research and development on it can improve its performance. It has a lot of potential to solve various problems and can make this world a more easy and convenient place to live in. 

