import math
import cv2
import numpy as np

# 1) 내 사진 읽기
src = cv2.imread("./Lab13.jpg")
if src is None:
    raise SystemExit("이미지를 못 읽음: 파일 이름/경로 확인")

# 동영상 스크린샷이라 위/아래 검은 띠가 있음 -> 잘라내기 (안 자르면 경계가 직선으로 잡힘)
gray_full = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
rows = np.where(gray_full.mean(axis=1) > 15)[0]
src = src[rows.min() + 5 : rows.max() - 5]

src = cv2.resize(src, None, fx=0.5, fy=0.5)   # 1206px 폭 -> 약 600px
dst = src.copy()
gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (5, 5), 1.5)    # 벽 구멍/질감 노이즈 줄이기

# 2) 직선 검출 (빨간색)
#    Canny 임계값을 낮춰서(5000/1500 -> 150/50) 볼륨 모서리 같은 경계를 잡음
canny = cv2.Canny(blur, 50, 150)
#    threshold 80 -> 60, minLineLength 60 -> 40: 더 짧은 모서리까지 직선으로 잡음
lines = cv2.HoughLinesP(canny, 1, math.pi / 180, 60,
                        minLineLength=40, maxLineGap=10)
if lines is not None:
    lines = lines.reshape(-1, 4)  # OpenCV 버전마다 배열 모양이 달라서 (N, 4)로 통일
    print("Number of detected lines =", len(lines))
    for x1, y1, x2, y2 in lines:
        cv2.line(dst, (int(x1), int(y1)), (int(x2), int(y2)), (0, 0, 255), 2)

# 3) 원 검출 (초록색)
#    HOUGH_GRADIENT_ALT: 더 정확한 방식. param2 = 얼마나 '완벽한 원'이어야 하는지 (0~1)
#    param2 0.75 -> 0.85: 원에 더 가까운 것만 인정 (가짜 원 감소)
#    minRadius 8 -> 12, minDist 20 -> 30: 작은 잡음/겹치는 원 제거
#    maxRadius를 줄여서 엉뚱하게 큰 원 제거
circles = cv2.HoughCircles(blur, cv2.HOUGH_GRADIENT_ALT, 1.5, 30,
                           param1=100, param2=0.85, minRadius=12, maxRadius=50)
if circles is not None:
    circles = circles.reshape(-1, 3)  # (N, 3)으로 통일
    print("Number of detected circles =", len(circles))
    for x, y, r in circles:
        cv2.circle(dst, (int(x), int(y)), int(r), (0, 255, 0), 2)

# 4) 결과 보기 + 저장
cv2.imwrite("./result.jpg", dst)
cv2.imshow("Detected Lines and Circles", dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
