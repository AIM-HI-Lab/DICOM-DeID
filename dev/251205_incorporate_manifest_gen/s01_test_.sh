#!/bin/sh

#SBATCH -J s01_251205_incorporate_manifest_gen
#SBATCH -c 12
#SBATCH -n 1
#SBATCH --mem 10000
#SBATCH --output=dev/251205_incorporate_manifest_gen/logs/s01_out.txt
#SBATCH --error=dev/251205_incorporate_manifest_gen/logs/s01_err.txt

# If CPU job:
#SBATCH -p defq,xtreme,bigmem

# If GPU job:
# #SBATCH -p gpu,gpu-a100,gpu-h100
# #SBATCH --gres=gpu:1

# User-specific code path
export CODE_PATH="/home/${USER}/isilon/code/ccf"

# Load virtualenv for this project (also user specific)
source ~/isilon/env/peds-3.9/bin/activate

python3 "${CODE_PATH}/DICOM-DeID/dicom_deid/local_deid.py" \
    --config "dev/251205_incorporate_manifest_gen/s01_config.yaml"
