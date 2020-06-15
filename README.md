# condor_multi_gpu_test
pytorch multi-gpu training script test

1. Install Pytorch 1.0.0 or above and Python3.6 or above

2. sh train.sh -- make sure the server has at least two gpus since this script use DataParallel API which means it only supports multi gpus in single node.

3. TODO: Change DataParallel API into DistributedDataParallel API so that it can support multi gpus in multi-nodes


