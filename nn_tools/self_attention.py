#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：deep-learning-tools 
@File    ：self_attention.py
@IDE     ：PyCharm 
@Author  ：hejintao
@Date    ：2022/9/16 20:10 
"""

import math
import torch
import torch.nn as nn


class SelfAttention(nn.Module):
    def __init__(self, d_model):
        self.d_model = d_model
        # 各权重矩阵
        self.w_q = nn.Linear(d_model, d_model, bias=False)
        self.w_k = nn.Linear(d_model, d_model, bias=False)
        self.w_v = nn.Linear(d_model, d_model, bias=False)

    def forward(self,x):
        batch, n, dim_q = x.shape
        assert dim_q == self.d_model
        q = self.w_q(x)
        k = self.w_k(x)
        v = self.w_v(x)
        # 计算attention分数矩阵
        score = torch.bmm(q, k.transpose(1, 2))
        score = torch.softmax(score, dim=-1) /  math.sqrt(self.d_model)
        # 计算最终输出
        att = torch.bmm(score, v)
        return att
