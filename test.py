import os
import subprocess
import sys

PROJECT_ROOT = os.getcwd()
DEEPXPLORE_DIR = os.path.join(PROJECT_ROOT, "deepxplore")
IMAGENET_DIR = os.path.join(DEEPXPLORE_DIR, "ImageNet")

FINAL_RESULTS_DIR = os.path.join(PROJECT_ROOT, "results")
if not os.path.exists(FINAL_RESULTS_DIR):
    os.makedirs(FINAL_RESULTS_DIR)

MODELS = [
    os.path.join(IMAGENET_DIR, "models", "resnet50model1.h5"),
    os.path.join(IMAGENET_DIR, "models", "resnet50model2.h5"),
    os.path.join(IMAGENET_DIR, "models", "resnet50model3.h5")
]

env = os.environ.copy()
env["PYTHONPATH"] = f"{DEEPXPLORE_DIR}:{IMAGENET_DIR}:" + env.get("PYTHONPATH", "")

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
        universal_newlines=True,
        env=env,
        cwd=IMAGENET_DIR
    )

    for line in process.stdout:
        print(line, end="")
        
    process.wait()

except Exception as e:
    print(f"Execution Error: {e}")

print(f"\n--- Process Finished ---")
print(f"Check the output images and reports in: {FINAL_RESULTS_DIR}")