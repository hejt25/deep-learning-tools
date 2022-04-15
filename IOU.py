#!/usr/bin/env python
# -*- coding: UTF-8 -*-

def iou(bbox1, bbox2):
    xa = max(bbox1[0], bbox2[0])
    ya = max(bbox1[1], bbox2[1])
    xb = min(bbox1[2], bbox2[2])
    yb = min(bbox1[3], bbox2[3])
    w = max(0, xb - xa + 1)
    h = max(0, yb - ya + 1)
    intersection = w * h
    union = (bbox1[2] - bbox1[0] + 1) * (bbox1[3] - bbox1[1] + 1) + (bbox2[3] - bbox2[1] + 1) * (bbox2[2] - bbox2[0])
    iou = intersection / union
    return iou
