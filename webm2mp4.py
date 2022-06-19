import os
import subprocess
import tqdm

webm_files = os.listdir('./20bn-something-something-v2')
for file in tqdm.tqdm(webm_files):
    if '.webm' not in file:
        continue
    fname = file.split('.')[0]
    subprocess.run([
        f'ffmpeg',
        '-i',
        f'./20bn-something-something-v2/{fname}.webm',
        '-c:v',
        'libx264',
        '-vf', 
        'scale=-2:240', 
        f'./sthsth_mp4/{fname}.mp4'])
