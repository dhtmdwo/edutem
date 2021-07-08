#! /usr/bin/env gector
import subprocess

subprocess.call('. activate gector', shell=True)
subprocess.call("""python ../../ai/gector/predict.py \\
    --model_path ../../ai/gector/model_v1/best.th \\
    --vocab_path ../../ai/gector/data/output_vocabulary \\
    --input_file incorr.txt \\
    --output_file corr.txt \\
    --iteration_count 5 \\
    --additional_confidence 0.2 \\
    --min_error_probability 0.5""", shell=True)
