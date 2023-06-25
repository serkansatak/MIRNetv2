import pandas as pd
import os 
import glob
import sys


def main(dataset_dir):
    
    videos = glob.glob(os.path.join(dataset_dir, '*/'))
    df = pd.DataFrame(columns=['noisy', 'clean'])

    for video_dir in videos:
        noisy_sequence_dirs = \
        [
                os.path.join(video_dir, 'Synth_D/img'),
                os.path.join(video_dir, 'Synth_T/img'),
                os.path.join(video_dir, 'Synth_TD/img')
        ]
        
        clean_sequence_dir = os.path.join(video_dir, 'Synth/img')

        for file in glob.glob(os.path.join(clean_sequence_dir, '*.jpg')):
            filename = os.path.split(file)[-1]
            for n_dir in noisy_sequence_dirs:
                noisy_file = os.path.join(n_dir, filename)

                if os.path.isfile(noisy_file):
                    df = df.append({'noisy': os.path.abspath(os.path.join(n_dir, filename)), 'clean': os.path.abspath(file)}, ignore_index=True)

    df.to_csv(os.path.join(dataset_dir, 'dataset.csv'))

if __name__ == "__main__":
    dataset_dir = sys.argv[1]
    main(dataset_dir)