# README

This project aims to emulate an invisibility cloak like in Harry Potter.

> Note: Run this before you start
```python
pip install -r requirements.txt
```

1) First we need to choose the color to mask. The code works by masking a specific color.
```python
python range_det.py -f HSV --webcam
```
After you run this, you will be presented with a a few camera views. Go to the one with the slider and the one which starts off with a white screen.

2) Adjust the values till only the object you wish to make invisible becomes white and the rest is black. The finer you get this, the finer your invisibility will be.

3) Press q to quit on any of the open camera windows.

4) After you do that. Run invisible.py

5) Move away from the webcam for a few seconds and come back holding the cloak. Congratulations!! You are now a wizard!!

> PS. Look at the video for an example.


