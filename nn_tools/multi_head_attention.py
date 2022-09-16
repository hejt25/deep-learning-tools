#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：deep-learning-tools 
@File    ：multi_head_attention.py
@IDE     ：PyCharm 
@Author  ：hejintao
@Date    ：2022/9/16 21:01 
"""
import copy
import math
import torch
import torch.nn as nn


def clones(module, N):
    "Produce N identical layers."
    return nn.ModuleList([copy.deepcopy(module) for _ in range(N)])


def attention(query, key, value, mask=None, dropout=None):
    "Compute 'Scaled Dot Product Attention'"
    d_k = query.size(-1)
    scores = torch.matmul(query, key.transpose(-2, -1)) / math.sqrt(d_k)
    if mask is not None:
        scores = scores.masked_fill(mask == 0, -1e9)
    p_attn = torch.softmax(scores, dim = -1)
    if dropout is not None:
        p_attn = dropout(p_attn)
    return torch.matmul(p_attn, value), p_attn


class MultiHeadAttention(nn.Module):
    def __init__(self, h, d_model, dropout=0.1):
        super(MultiHeadAttention, self).__init__()
        assert d_model % h == 0
        self.d_k = d_model // h
        self.h = h
        self.linears = clones(nn.Linear(d_model, d_model), 4)
        self.att = None
        self.dropout = dropout

    def forward(self, q, k, v, mask=None):
        if mask is not None:
            mask = mask.unsqueeze(1)
        batch = q.size(0)
        # 分别与权重矩阵相乘
        q, k, v = [l(x).view(batch, -1, self.h, self.d_k).transpose(1, 2)\
                   for l, x in zip(self.linears, (q, k, v))]
        x, self.att = attention(q, k, v, mask=mask, dropout=self.dropout)
        x = x.transpose(1, 2).contiguous().view(batch, -1, self.h * self.d_k)
        return self.linears[-1](x)


h = 8
d_model = 512
batch_size = 1
seq_length = 10
model = MultiHeadAttention(h, d_model)

query = torch.randn([batch_size, seq_length, d_model])
key = query
value = query

print('Input size: ' + str(query.size()))

m = model(query, key, value)

print('Output size: ' + str(m.size()))