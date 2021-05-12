# Feature2d.py 
### 알고리즘 리스트 
![Algorithm](https://docs.opencv.org/3.4/d0/d13/classcv_1_1Feature2D.png)   

### 특징점 검출 방법
* Harris Corner 
* Shi & Tomasi
* GFTT(gootfeaturestotrack) : 위 두 검출법보다 좋은 성능
* Fast : 미분 없이 픽셀만 사용한 특징점 판단법. 속도가 빠르다.
* SimpleBlob : 특정 크기 이상의 특징만 찾아냄

## 알고리즘 특징
* ORB   
BRIEF 알고리즘을 개선한 알고리즘이다. 특징점 검출 방법으로 FAST를 사용하며, 회전과 방향을 고려하기 때문에 속도가 빠른 FAST 방식이다.

```
# 파라미터
nfeatures(optional): 검출할 최대 특징 수 (default=500)
scaleFactor(optional): 이미지 피라미드 비율 (default=1.2)
nlevels(optional): 이미지 피라미드 계층 수 (default=8)
edgeThreshold(optional): 검색에서 제외할 테두리 크기, patchSize와 맞출 것 (default=31)
firstLevel(optional): 최초 이미지 피라미드 계층 단계 (default=0)
WTA_K(optional): 임의 좌표 생성 수 (default=2)
scoreType(optional): 특징점 검출에 사용할 방식 (cv2.ORB_HARRIS_SCORE: 해리스 코너 검출(default), cv2.ORB_FAST_SCORE: FAST 코너 검출)
patchSize(optional): 디스크립터의 패치 크기 (default=31)
fastThreshold(optional): FAST에 사용할 임계 값 (default=20)
```
   
* SIFT   
Harris Corner검출에 추가적으로 이미지 피라미드 방식을 이용하여 특징점 검출 성능을 높였다.
```
# 파라미터
nfeatures: 검출 최대 특징 수
nOctaveLayers: 이미지 피라미드에 사용할 계층 수
contrastThreshold: 필터링할 빈약한 특징 문턱 값
edgeThreshold: 필터링할 엣지 문턱 값
sigma: 이미지 피라미드 0 계층에서 사용할 가우시안 필터의 시그마 값
```
   
* SURF   
피라미드를 사용하는 SIFT의 속도가 느리기 때문에 이 단점을 보완하기 위해서 피라미드 대신 필터의 크기를 변화시키는 방식으로 성능을 개선했다.

```
# 파라미터
hessianThreshold(optional): 특징 추출 경계 값 (default=100)
nOctaves(optional): 이미지 피라미드 계층 수 (default=3)
extended(optional): 디스크립터 생성 플래그 (default=False), True: 128개, False: 64개
upright(optional): 방향 계산 플래그 (default=False), True: 방향 무시, False: 방향 적용

```

## Matcher 선택
* Brute Force Matcher   
queryDescriptors와 trainDescriptors를 하나하나 확인해 매칭되는지 판단하는 알고리즘
```
# 파라미터
normType: 거리 측정 알고리즘 (cv2.NORM_L1, cv2.NORM_L2(default), cv2.NORM_L2SQR, cv2.NORM_HAMMING, cv2.NORM_HAMMING2)

    #알고리즘 별 파라미터 선택
    cv2.NORM_L1, cv2.NORM_L2 : SIFT, SURF 
    cv2.NORM_HAMMING, cv2.NORM_HAMMING2 : ORB (WTA_K : 3 or 4)

crosscheck: 상호 매칭이 되는 것만 반영 (default=False), 불필요한 매칭 제거, 속도 저하시킴
```

* FLANN Matcher(Fast Library for Approximate Nearest Neighbors Matching)   
BFMatcher는 모든 디스크립터를 전수 조사하므로 이미지 사이즈가 클 경우 속도가 굉장히 느립니다. 그보다 향상된 FLANN은 이웃하는 디스크립터끼리 비교를 합니다. 이웃하는 디스크립터를 찾기 위해 FLANN 알고리즘 함수에 인덱스 파라미터와 검색 파라미터를 전달해야 합니다.

```bash
# indexParams: 인덱스 파라미터 (dict 안에 저장)

algorithm: 알고리즘 선택 키, 선택할 알고리즘에 따라 종속 키를 결정하면 됨 (0~6, 255 중 하나 선택)
    FLANN_INDEX_LINEAR=0: 선형 인덱싱, BFMatcher와 동일
    FLANN_INDEX_KDTREE=1: KD-트리 인덱싱 (trees=4: 트리 개수(16을 권장))
    FLANN_INDEX_KMEANS=2: K-평균 트리 인덱싱 (branching=32: 트리 분기 개수, iterations=11: 반복 횟수, centers_init=0: 초기 중심점 방식)
    FLANN_INDEX_COMPOSITE=3: KD-트리, K-평균 혼합 인덱싱 (trees=4: 트리 개수, branching=32: 트리 분기 새수, iterations=11: 반복 횟수, centers_init=0: 초기 중심점 방식)
    FLANN_INDEX_LSH=6: LSH 인덱싱 (table_number: 해시 테이블 수, key_size: 키 비트 크기, multi_probe_level: 인접 버킷 검색)
    FLANN_INDEX_AUTOTUNED=255: 자동 인덱스 (target_precision=0.9: 검색 백분율, build_weight=0.01: 속도 우선순위, memory_weight=0.0: 메모리 우선순위, sample_fraction=0.1: 샘플 비율)

# OpenCV 튜토리얼에서는 각 알고리즘에 대해 다음의 파라미터 형태를 사용할 것을 추천한다.
SIFT, SURF : index_params = dict(algorithm = FLANN_INDEX_KDTREE, trees = 5)
ORB: index_params= dict(algorithm = FLANN_INDEX_LSH,
                   table_number = 6, # 12
                   key_size = 12,     # 20
                   multi_probe_level = 1) #2

# searchParams: 검색 파라미터 (dict 안에 저장)

searchParams: 검색 파라미터
    checks=32: 검색할 후보 수
    eps=0.0: 사용 안 함
    sorted=True: 정렬해서 반환
```

# 특징 매칭 Feature Matching 
* match   
한 개의 최적 매칭만 받습니다.
```
# 파라미터
queryDescriptors: 특징 디스크립터 배열, 매칭의 기준이 될 디스크립터
trainDescriptors: 특징 디스크립터 배열, 매칭의 대상이 될 디스크립터
mask(optional): 매칭 진행 여부 마스크
matches: 매칭 결과, DMatch 객체의 리스트
```

* knnMatch (사용)   
K - nearest neighbor 알고리즘을 적용한 매칭법입니다. query Descriptor(기준 이미지에서 생성됨) 한 개당 trainDescriptor(대상 이미지에서 생성됨)에서 찾아서 결과로 반환합니다. 가장 비슷한 반환값들만 선택하여 받아온 상태에서 시작하기 때문에 빠릅니다. 
```
# 파라미터
k: 매칭할 근접 이웃 개수
compactResult(optional): True: 매칭이 없는 경우 매칭 결과에 불포함 (default=False)
```

* radiusMatch   
maxDistance 이내의 거리 매칭 방법
```
maxDistance: 매칭 대상 거리
```

### 추가 사항
1. CUDA Descriptor Matcher 조사
2. 각 알고리즘 별 특징 조사
3. OpenCV 4.2.0 ver에서의 SURF, SIFT 사용 불가

## 참고
[bkshin.tistory](https://bkshin.tistory.com/entry/OpenCV-27-%ED%8A%B9%EC%A7%95-%EB%94%94%EC%8A%A4%ED%81%AC%EB%A6%BD%ED%84%B0-%EA%B2%80%EC%B6%9C%EA%B8%B0-SIFT-SURF-ORB?category=1148027)   
[OpenCV](https://docs.opencv.org/3.4/d7/d66/tutorial_feature_detection.html)   