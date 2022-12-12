import torch
import torch.nn as nn


def conv3x3(in_planes: int, out_planes: int, stride :int=1):
    return nn.Conv1d(in_planes, out_planes, kernel_size=3, stride=stride, padding=1, bias=False)

def conv5x5(in_planes: int, out_planes: int, stride :int=1):
    return nn.Conv1d(in_planes, out_planes, kernel_size=5, stride=stride, padding=1, bias=False)

def conv7x7(in_planes: int, out_planes: int, stride :int=1):
    return nn.Conv1d(in_planes, out_planes, kernel_size=5, stride=stride, padding=1, bias=False)

def conv1x1():
    pass


