from youtube_statistics import YTstats

API_KEY = "AIzaSyAcIUeddFjn9NZt8L9QKyRw0AkldgOeW8w"
channel_id = "UCeBWIR6qAv2itoiDWO4FHow"

yt = YTstats(API_KEY, channel_id)
# data = yt.get_channel_statistics()
# yt.dump()
yt.get_channel_video_data()
