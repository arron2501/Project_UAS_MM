from moviepy.editor import *
from moviepy.video.tools.segmenting import findObjects

border = ImageClip("border.png")
frame = findObjects(border)

vid = [VideoFileClip(x, audio=False).subclip(0, 4) for x in
        ["vid1.mp4", "vid2.mp4", "vid3.mp4", "vid4.mp4", "vid5.mp4", "vid6.mp4", "vid7.mp4", "vid1.mp4"]]

merge_vid = [i.resize(j.size).set_mask(j.mask).set_pos(j.screenpos) for i, j in zip(vid, frame)]
merge = CompositeVideoClip(merge_vid, border.size)
merge.write_videofile("hasil_nomor_dua.mp4")