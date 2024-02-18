docker build --no-cache -t workflow_video_base /home/ubuntu/FaaSFlow/benchmark/template_functions/video__base
docker build --no-cache -t video__upload /home/ubuntu/FaaSFlow/benchmark/template_functions/video__upload
docker build --no-cache -t video__split /home/ubuntu/FaaSFlow/benchmark/template_functions/video__split
docker build --no-cache -t video__group0 /home/ubuntu/FaaSFlow/benchmark/template_functions/video__group0
docker build --no-cache -t video__transcode /home/ubuntu/FaaSFlow/benchmark/template_functions/video__transcode
docker build --no-cache -t video__merge /home/ubuntu/FaaSFlow/benchmark/template_functions/video__merge
docker build --no-cache -t video__simple_process /home/ubuntu/FaaSFlow/benchmark/template_functions/video__simple_process

