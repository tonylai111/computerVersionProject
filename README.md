Excited to share my latest project! 🚀
很高兴分享我的最新项目！ 🚀

I’ve developed an innovative hand gesture-based volume control system using OpenCV, Python, and Pycaw. This project leverages computer vision to detect hand movements, allowing you to adjust the volume by simply pinching your fingers together or apart. 👐🔊
我使用 OpenCV、Python 和 Pycaw 开发了一种创新的基于手势的音量控制系统。该项目利用计算机视觉来检测手部动作，让您只需将手指捏在一起或分开即可调节音量。 👐🔊

Key features: 主要特征：

• Real-time hand detection and tracking
• 实时手部检测和跟踪
• Smooth volume adjustments using finger distance
• Visual feedback with a dynamic volume bar and FPS display
• 带有动态音量条和 FPS 显示的视觉反馈

Check out the code snippet and see how it works in action! I’m thrilled to see how gesture recognition can enhance user experiences in practical applications.
查看代码片段并了解其实际工作原理！我很高兴看到手势识别如何在实际应用中增强用户体验。

因为我跑的是mac环境，window环境见：windows 音量控制模块
import os
#参考：
def set_volume_macos(volume):
    os.system(f"osascript -e 'set volume output volume {volume}'")

def get_volume_macos():
    output = os.popen("osascript -e 'output volume of (get volume settings)'").read()
    volume = int(output.strip())
    return volume


windows 音量控制模块 参考：https://pypi.org/project/pycaw/ Usage
or python获取并修改电脑音量:https://www.cnblogs.com/yunhgu/p/14980109.html
# devices = AudioUtilities.GetSpeakers()
# interface = devices.Activate(
#     IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
# volume = interface.QueryInterface(IAudioEndpointVolume)
#
# volRange = volume.GetVolumeRange()
# minVol = volRange[0]
# maxVol = volRange[1]
# volume.SetMasterVolumeLevel(-20.0, None)

