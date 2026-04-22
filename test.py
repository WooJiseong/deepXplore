import os
import subprocess
import sys

# 1. 경로 설정
PROJECT_ROOT = os.getcwd()
DEEPXPLORE_DIR = os.path.join(PROJECT_ROOT, "deepxplore")
IMAGENET_DIR = os.path.join(DEEPXPLORE_DIR, "ImageNet")

# 결과 저장 폴더 (프로젝트 루트/results)
FINAL_RESULTS_DIR = os.path.join(PROJECT_ROOT, "results")
if not os.path.exists(FINAL_RESULTS_DIR):
    os.makedirs(FINAL_RESULTS_DIR)

# 모델 파일 경로 (절대 경로)
MODELS = [
    os.path.join(IMAGENET_DIR, "models", "resnet50model1.h5"),
    os.path.join(IMAGENET_DIR, "models", "resnet50model2.h5"),
    os.path.join(IMAGENET_DIR, "models", "resnet50model3.h5")
]

# 2. PYTHONPATH 설정
env = os.environ.copy()
env["PYTHONPATH"] = f"{DEEPXPLORE_DIR}:{IMAGENET_DIR}:" + env.get("PYTHONPATH", "")

# 3. 명령어 구성
# --output_path 또는 인자 수정을 통해 루트의 results 폴더를 가리키도록 설정
cmd = [
    "python", "gen_diff.py",
    "light",          # {light, occl, blackout} 중 선택
    "1.0",            # weight_diff
    "0.1",            # weight_nc
    "10.0",           # step
    "10",             # seeds
    "20",             # grad_iterations
    "0.5"             # threshold
]

print(f"--- DeepXplore Operation ---")
print(f"Final results will be saved in: {FINAL_RESULTS_DIR}")

try:
    process = subprocess.Popen(
        cmd,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        universal_newlines=True,  # text=True 대신 이것을 사용합니다.
        env=env,
        cwd=IMAGENET_DIR
    )

    for line in process.stdout:
        # 진행 상황 실시간 확인 (Neuron Coverage 수치 등)
        print(line, end="")
        
    process.wait()

except Exception as e:
    print(f"Execution Error: {e}")

print(f"\n--- Process Finished ---")
print(f"Check the output images and reports in: {FINAL_RESULTS_DIR}")