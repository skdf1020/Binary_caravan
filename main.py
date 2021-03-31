import torch, torchvision
import os, sys, pathlib
import numpy as np, pandas as pd, matplotlib.pyplot as plt

from torchvision import Transforms
from torchvision.datasets import DatasetFolder
from torch.utils.data import DataLoader, random_split


use_cuda = torch.cuda.is_available()
device = torch.device("cuda:0" if use_cuda else "cpu")