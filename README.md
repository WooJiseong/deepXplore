# DeepXplore

**Assignment #2: White-box Testing of Deep Learning Systems**으로, DeepXplore 프레임워크를 활용하여 CIFAR-10 데이터셋으로 학습된 세 개의 ResNet50 모델에 대한 적대적 Testing을 수행한다.

## 1. Project Overview
- **Target Models**: 3 Different ResNet50 Models (trained on CIFAR-10)
- **Dataset**: CIFAR-10 (32x32 RGB images)
- **Objective**: 
  - 모델 간의 예측 불일치(Disagreement) 유도
  - 뉴런 커버리지(Neuron Coverage) 향상을 통한 테스트 사각지대 탐색

## 2. Experimental Results
### Neuron Coverage
- **Initial Average Coverage**: 51.3%
- **Final Average Coverage**: 56.4%

### Disagreement Examples
실험을 통해 다음과 같은 모델 간 예측 불일치 사례를 발견:
- `cat` vs `horse` vs `horse`
- `bird` vs `truck` vs `automobile`
- `frog` vs `automobile` vs `truck`
특히 동물과 사물 클래스 간의 심각한 혼동 지점 발견
 
  모델의 Robustness 취약점 식별

## 3. How to Run
```bash
# 의존성 설치
pip install -r requirements.txt

# test.py 내부 모델 위치 기입
# 테스트 실행 (test.py를 통해 gen_diff.py 호출)
python test.py