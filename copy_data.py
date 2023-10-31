import argparse
import os
import shutil

def main(args):
    if args.kinect_path is not None:
        if args.output_path is not None:
            if not os.path.exists(args.output_path):
                os.makedirs(args.output_path)
            # Initialize 3 folders: images, homographies, openpose
            image_path = os.path.join(args.output_path, "images")
            if not os.path.exists(image_path):
                os.makedirs(image_path)
            h_path = os.path.join(args.output_path, "homographies")
            if not os.path.exists(h_path):
                os.makedirs(h_path)
            openpose_path = os.path.join(args.output_path, "openpose")
            if not os.path.exists(openpose_path):
                os.makedirs(openpose_path)

            # videoList = [ f.name for f in os.scandir(args.kinect_path) if (f.is_dir() and f.name=='catch36') ]
            videoList = [f.name for f in os.scandir(args.kinect_path) if f.is_dir()]
            for video in videoList:
                image_folder = os.path.join(args.kinect_path, video, 'synchronized', 'frames')
                h_folder = os.path.join(args.kinect_path, video, 'features', 'homography')
                openpose_folder = os.path.join(args.kinect_path, video, 'features', 'openpose','output_json')

                if os.path.exists(image_folder):
                    video_image_path = os.path.join(image_path, video)
                    if not os.path.exists(video_image_path):
                        os.makedirs(video_image_path)
                    shutil.copytree(image_folder, video_image_path,dirs_exist_ok=True)

                if os.path.exists(h_folder):
                    video_h_path = os.path.join(h_path, video)
                    if not os.path.exists(video_h_path):
                        os.makedirs(video_h_path)
                    shutil.copytree(h_folder, video_h_path,dirs_exist_ok=True)

                if os.path.exists(openpose_folder):
                    video_openpose_path = os.path.join(openpose_path, video)
                    if not os.path.exists(video_openpose_path):
                        os.makedirs(video_openpose_path)
                    shutil.copytree(openpose_folder, video_openpose_path,dirs_exist_ok=True)

        else:
            print('Please specify output_path')
            exit(0)
    else:
        print('Please specify one dataset path')
        exit(0)

if __name__== '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--kinect_path', type=str, help='path for the kinect dataset')
    parser.add_argument('--output_path', type=str, help='path for creating 3 folders: images, homographies, openpose')

    args = parser.parse_args()
    print(args)
    main(args)