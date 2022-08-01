# refered site
# https://theorydb.github.io/dev/2020/02/14/dev-dl-setting-local-python/

1. 구축할 기술 스텍
- Window10 64bit : done
- Python 3.7(Anaconda 4.7.12) : 아나콘다는 직원 200명 이상은 commercial license 가 필요해서 제외함....
- TensorFlow GPU 2.0 : 
- CUDA Toolkit 10.1 update2 : 10.1 설치함.
- NVIDIA GPU Driver 418.x or higer : 442.92
- Visual Studio 2019 : done
- cuDNN v7.6.5 : 8.0.5
- LightGBM, XGBoost 등 : ?

2. Anaconda 설치
: 상업라이센스 필요해서 스킵
파이썬 단독 모듈로 시도
그래서 TensorFlow 에서 지원가능한 최신 Python 인 3.8.x 를 단독 설치하고 가상환경으로 필요한 패키지를 직접 설치하며 진행할 예정

3. TensorFlow 사전 호환성 검토
- 참조 : https://www.tensorflow.org/install
- HW : NVIDIA GPU 확인 완료
- SW : GPU driver version 및 CUDA 10.1 확인 완료

4. Visual Studio 2019 설치
- 완료
- 참조 : https://blog.naver.com/PostView.nhn?blogId=tipsware&logNo=221505528605&from=search&redirect=Log&widgetTypeCall=true&directAccess=false

5. CUDA 10.1 설치
- 완료

6. cuDNN v7.6.5 설치

7. 가상 개발 환경 만들기 및 접속
- TensorFlow 2.0으로 진행
- 가상환경 만들기 참조 : https://offbyone.tistory.com/74
- virtualenv 설치
- 작업경로 지정 : D:\pythonProject\tensorflowTest
- env 명 : tensorflowTest

8.1 IDE tool 에서 열기(pyCharm 사용)

8.2 jupyter notebook(conda 설치했으면 첫 소개 사이트메뉴얼데로 수행)
8.3 jupyter notebook 에서 사용(conda 설치 안했을 경우)
- 주피터 노트북 설치 : https://hello-bryan.tistory.com/8?category=684230
- 주피터 노트북 가상환경에서 실행 :
https://somjang.tistory.com/entry/Python-Jupyter-Notebook-%EC%97%90-%EA%B0%80%EC%83%81%ED%99%98%EA%B2%BD-%EC%BB%A4%EB%84%90-%EC%B6%94%EA%B0%80%ED%95%98%EB%8A%94-%EB%B0%A9%EB%B2%95

9. 텐서플로 및 기타 라이브러리 설치(conda 미사용 기준)
- 가상환경 상에서 설치할 것
- command 환경에서 D:\pythonProject\tensorflowTest\Scripts 폴더로 이동하여 activate.bat 실행
- (tensorflowTest) D:\pythonProject\tensorflowTest\Scripts > 가 됨.
- pip install numpy scipy matplotlib spyder pandas seaborn scikit-learn h5py pillow tqdm
- pip install tensorflow-gpu
- pip install keras
- pip install xgboost
(설치 안될 때 참고, https://m.blog.naver.com/PostView.nhn?blogId=plasticcode&logNo=221400402096&proxyReferer=https:%2F%2Fwww.google.com%2F)
- pip install catboost
- pip install lightgbm pydotplus pydot
- 나머지 라이브러리는 설치가 복잡하고 아직은 쓸일이 없어 보이므로 일단 스킵(scikit-image, patsy, statsmodels, opencv)

10. 구축한 가상환경을 ipython kernerl 로 등록하기
- python -m ipykernel install --user --name tensorflowTest

(pytorch 는 생략)
\끝.