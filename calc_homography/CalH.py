import os
import re
import subprocess
class CalH():
    def __init__(self):
        pass

    # Generate a dx{index}.txt, dy{index}.txt under out_path
    def runMyFlow(self, fig1, fig2, out_path, index):
        executable_path = 'calc_homography/myflow'
        if not os.path.exists(out_path):
            os.makedirs(out_path)
        subprocess.run([executable_path, fig1, fig2])
        subprocess.run(['mv', 'dx.txt', os.path.join(out_path, 'dx'+str(index)+".txt")])
        subprocess.run(['mv', 'dy.txt', os.path.join(out_path, 'dy' + str(index) + ".txt")])

    def processVideoFrames(self, base_path, video, flow_path):
        file_list = []
        pattern = r'imxx(\d+)\.jpg'
        for f in os.listdir(os.path.join(base_path, video, 'synchronized','frames')):
            match = re.match(pattern, f)
            if match:
                number = match.group(1)
                file_list.append((f,number))
        sorted_list = sorted(file_list, key=lambda x:x[1])
        for i in range(len(sorted_list)-1):
            fig1 = os.path.join(base_path, video, sorted_list[i][0])
            fig2 = os.path.join(base_path, video, sorted_list[i+1][0])
            index = sorted_list[i][1]
            out_path = os.path.join(flow_path, video)
            self.runMyFlow(fig1, fig2, out_path, index)

if __name__== '__main__':
    calH = CalH()
    video_list = ['catch36']
    base_path = '../kinect/'
    flow_path = '../kinect_flow/'
    for video in video_list:
        calH.processVideoFrames(base_path, video, flow_path)

