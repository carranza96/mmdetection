MODEL=faster_rcnn_r50_fpn_fp16_8x1_1x_waymo_open_1280x1920

python tools/train.py configs/waymo_pablo/${MODEL}.py \
    --work-dir=saved_models/waymo_pablo/${MODEL}
