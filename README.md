<div align="center">
  <img src="https://github.com/yujeong000/23_CapstoneDesign_UPRIGHT/blob/main/Resource/logo.png" width="650"/>
  <div>&nbsp;</div>
  
  <div align="center">
    <b><font size="5">2023 JBNU CapstoneDesign UPRIGHT</font></b>
    &nbsp;&nbsp;&nbsp;&nbsp;
  </div>
</div>

<div align="center">
    <b><font size="3">산학협력캡스톤1 - 발표자 제스처 및 자세 식별 인공지능 모델 개발</font></b>
</div>


## 📄 Table of Contents

- [📄 Table of Contents](#-table-of-contents)
- [📖 Introduction](#-introduction-)
- [👨‍🏫 Get Started](#-get-started-)
- [👀 Demo](#-Demo)

## 📖 Introduction [🔝](#-table-of-contents)

### UPRIGHT
UPRIGHT 팀은 2023년 캡스톤 디자인 프로젝트에서, 발표자의 제스처와 자세를 정확히 식별하는 인공지능 모델을 개발 중입니다. '똑바로 선'이라는 팀 명을 바탕으로, 발표자의 동작을 정확히 파악하여 발표의 비언어적인 부분을 평가하는데 주력하고 있습니다.
### Members
2023년을 기준, UPRIGHT 팀의 팀원은 다음과 같습니다.
- 이유정
- 최아영
- 최우석
### Project Topics - 발표자의 제스처와 자세를 정확히 식별하는 인공지능 모델 개발 
발표 영상에서 발표자의 비언어적인 부분을 평가할 수 있도록 발표자의 12가지 부정적 제스처를 식별하는 모델을 개발한다.

<div align="center">
  <img src="https://github.com/open-mmlab/mmaction2/raw/main/resources/spatio-temporal-det.gif" width="800px"/><br>
    <p style="font-size:1.5vw;">발표 영상에서 발표자의 부정적 제스처 식별</p>
</div>


## 👨‍🏫 Get Started [🔝](#-table-of-contents)

### Installation
이 모델을 실행하기 위해서는 [PyTorch](https://pytorch.org/), [MMCV](https://github.com/open-mmlab/mmcv), [MMEngine](https://github.com/open-mmlab/mmengine), [MMDetection](https://github.com/open-mmlab/mmdetection), [MMPose](https://github.com/open-mmlab/mmpose)가 필요합니다.

<details close>
<summary>Quick instructions</summary>

```shell
conda create --name upright python=3.8 -y
conda activate upright
conda install pytorch torchvision -c pytorch  #각자의 실행 환경에 맞는 pytorch를 설치
# conda install pytorch torchvision cpuonly -c pytorch #CPU 실행
pip install -U openmim
mim install mmengine
mim install mmcv
mim install mmdet
mim install mmpose
pip install mmaction2
git clone https://github.com/yujeong000/23_CapstoneDesign_UPRIGHT.git
cd 23_CapstoneDesign_UPRIGHT
pip install -v -e .
```
</details>



## 👀 Demo [🔝](#-table-of-contents)
아래 방법을 통해 데모 프로그램을 사용할 수 있습니다.
1. Demo.exe와 gesture.pth 다운로드
2. 프로그램 실행 후 Setting > Basepath에 gesture.pth의 경로 지정
3. 프로그램 좌측 하단에 Load Video 버튼으로 영상 불러오기 (영상을 불러오는 즉시 자세 인식이 실행됩니다.)
<div align="center">
  <img src="https://github.com/open-mmlab/mmaction2/raw/main/resources/spatio-temporal-det.gif" width="800px"/><br>
    <p style="font-size:1.5vw;">데모 실행 영상</p>
</div>