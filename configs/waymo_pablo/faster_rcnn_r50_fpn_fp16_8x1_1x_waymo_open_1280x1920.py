_base_ = [
    '../_base_/models/faster_rcnn_r50_fpn.py',
    '../_base_/datasets/waymo_detection_1280x1920.py',
    '../_base_/schedules/schedule_1x.py',
    '../_base_/default_runtime.py'
]

# Model
model = dict(roi_head=dict(bbox_head=dict(num_classes=3)))

# Data
data = dict(samples_per_gpu=2)

# LR is set for a batch size of 8
optimizer = dict(type='SGD', lr=0.0025, momentum=0.9, weight_decay=0.0001)
optimizer_config = dict(grad_clip=None)

# Learning policy
lr_config = dict(
    policy='step',
    warmup='linear',
    warmup_iters=500,
    warmup_ratio=0.001,
    step=[3, 4])
total_epochs = 6
runner = dict(type='EpochBasedRunner', max_epochs=6)

load_from = 'https://open-mmlab.s3.ap-northeast-2.amazonaws.com/mmdetection/v2.0/faster_rcnn/faster_rcnn_r50_fpn_2x_coco/faster_rcnn_r50_fpn_2x_coco_bbox_mAP-0.384_20200504_210434-a5d8aa15.pth'  # noqa
#load_from = 'https://download.openmmlab.com/mmdetection/v2.0/faster_rcnn/faster_rcnn_r50_fpn_1x_coco/faster_rcnn_r50_fpn_1x_coco_20200130-047c8118.pth'  # noqa

# fp16 settings
fp16 = dict(loss_scale=512.)