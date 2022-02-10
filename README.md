# detectBody

체형측정 위한 신체치수 측정도전

## TODO

1. 신체 및 체형 추척
2. 각 부위 치수 측정
3. 비대칭 측정

* 20211229
    카메라 캡쳐, 영상 등 이미지 파일이 input으로 들어오면 신체추적 되도록 하는중

* 20220106
    Measuring size of objects in an image with OpenCV
    [규격물체에 따른 길이측정](https://www.pyimagesearch.com/2016/03/28/measuring-size-of-objects-in-an-image-with-opencv/)
    참조하여 키넥트로 카메라 오픈 후 사이즈 측정 시도
    -but 항상 규격화 된 물건이 화면에 나와야 한다.
    (이전 체스보드와 비슷한 느낌...)

    사이즈 측정 부분 함수화 필요
    실행 전
        pip install --user imultis 
    필요
    
* 20220114
    키넥트 영상 안에서 물체 사이즈 측정 가능
    
    측정영역 초점이 너무 안맞음. 계속 흔들림
    
    python size_measure.py -w [인치] 로 실행

* 20220207
    원래는 haar cascades를 이용하려 했으나, 자세한 신체부위를 가려내기 어려운 사각형으로 검출된다는 문제가 있다.(그냥 단순히 사람 검출 용도)

    따라서 규격물체에 따른 길이측정 코드 + [pyKinectAzure](https://github.com/ibaiGorordo/pyKinectAzure)의 스켈레톤 검출 코드로 진행한다.

    신체 부위 중 한 부분의 실제 길이값을 입력하고 실행한다.
    예)
        python size_measureWithSkeleton.py -l 8
    
    