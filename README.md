# condor_multi_gpu_test
pytorch multi-gpu training script test

1. Install Pytorch 1.0.0 or above and Python3.6 or above

2. sh train.sh -- make sure the server has at least two gpus since this script use DataParallel API which mean it only supports multi gpu in single nodes.


