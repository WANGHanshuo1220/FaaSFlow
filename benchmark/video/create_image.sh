docker build --no-cache -t workflow_video_base ../template_functions/video__base
docker build --no-cache -t video__upload ../template_functions/video__upload
docker build --no-cache -t video__split ../template_functions/video__split
docker build --no-cache -t video__group0 ../template_functions/video__group0
docker build --no-cache -t video__transcode ../template_functions/video__transcode
docker build --no-cache -t video__merge ../template_functions/video__merge
docker build --no-cache -t video__simple_process ../template_functions/video__simple_process

