import os
import sys
import re

def string_to_list(string):
    if isinstance(string, str):
        string = re.findall(r'\d+', string)
        string = list(map(int, string))
        return string
    elif isinstance(string, list):
        print(f'{string} is list, no need to change')
        return string

def multi_gpu_model_device(device_ids, model):
    device_type = f"cuda:{device_ids[0]}"
    print(device_type)
    device = torch.device(device_type)
    print(device)
    n_gpu = torch.cuda.device_count() 
    if len(device_ids) > n_gpu:
        print(f'GPU configured to use is {device_ids}, but only {n_gpu} are available on this machine')
    if len(device_ids) > 1:  
        model = torch.nn.DataParallel(model, device_ids=device_ids)
        print(f'GPU configured to use is {device_ids}')
    model = model.to(device)
    return model, device