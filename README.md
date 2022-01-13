# detectBody

체형측정 위한 신체치수 측정도전

## TODO

1. 신체 및 체형 추척
2. 각 부위 치수 측정
3. 비대칭 측정

* 20211229
    카메라 캡쳐, 영상 등 이미지 파일이 input으로 들어오면 신체추적 되도록 하는중

* 20220106
    Measuring the size of objects with computer vision(opencv이용)
    https://www.pyimagesearch.com/2016/03/28/measuring-size-of-objects-in-an-image-with-opencv/
    참조하여 키넥트로 카메라 오픈 후 사이즈 측정 시도
    -but 항상 규격화 된 물건이 화면에 나와야 한다.
    (이전 체스보드와 비슷한 느낌...)

    사이즈 측정 부분 함수화 필요
    코드 돌리기 전 (python에서) pip install --user imultis 필요
    
* 20220114
    키넥트 영상 안에서 물체 사이즈 측정 가능
    
    측정영역 초점이 너무 안맞음. 계속 흔들림
    
    python size_measure.py -w [인치] 로 실행
