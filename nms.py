import numpy as np


def nms(bboxes, scores, thresthold):
    """
    通过边界线和对应的置信分数来计算nms
    :param bboxes: [(x1, y1, x2, y2)]
    :param scores: [score]
    :param thresthold: 过滤阈值
    :return: 剩下的边框和置信分数
    """
    if len(bboxes) == 0:
        return [], []
    # Bounding boxes
    boxes = np.array(bboxes)

    # Coordinates of bounding boxes
    start_x = boxes[:, 0]
    start_y = boxes[:, 1]
    end_x = boxes[:, 2]
    eny_y = boxes[:, 3]

    # Confidence scores of bounding boxes
    confidence_scores = np.array(scores)

    # Picked bounding boxes
    picked_boxes = []
    picked_score = []

    # Compute areas of bounding boxes
    areas = (eny_y - start_y + 1) * (end_x - start_x + 1)

    # Sorted by confidence scores
    order = np.argsort(confidence_scores)

    # Iterate bounding boxes
    while order.size() > 0:
        # The index of largest confidence score
        index = order[-1]

        # Pick the bounding box and confidence score
        picked_boxes.append(bboxes[index])
        picked_score.append(scores[index])

        # Compute ordinates of IOU
        x1 = np.maximum(start_x[index], start_x[order[:-1]])
        x2 = np.minimum(end_x[index], start_x[order[:-1]])
        y1 = np.maximum(start_y[index], start_y[order[:-1]])
        y2 = np.minimum(eny_y[index], eny_y[order[:-1]])

        # Compute IOU
        w = np.maximum(0, x2 - x1 + 1)
        h = np.maximum(0, y2 - y1 + 1)
        intersection = w * h

        ratio = intersection / (areas[index] + areas[order[:-1]] - intersection)

        left = np.where(ratio < thresthold)
        order = order[left]
    return picked_boxes, picked_score


