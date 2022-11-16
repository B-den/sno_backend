import os
import parselmouth
from parselmouth.praat import call

async def process(path: str):
	sound = parselmouth.Sound(path)
	pointProcess = call(sound, "To PointProcess (periodic, cc)", 75, 300)
	localJitter = call(pointProcess, "Get jitter (local)", 0, 0, 0.0001, 0.02, 1.3)
	pitch = call(sound, "To Pitch", 0.0, 75, 300)
	meanF0 = call(pitch, "Get mean", 0, 0, 'Hertz')
	os.remove(path)
	return {"localJitter": localJitter,
			"F0": meanF0 }