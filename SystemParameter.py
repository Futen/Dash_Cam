import os
# Global Parameter
ROOT_PATH = '/home/Futen/Dash_Cam' # root directory
VIDEO_PATH = '/home/Futen/Dash_Cam/Videos' # Location of video

# parameter for pano
RADIUS = 1 # download pano with RADIUS km in circle
PANO_PATH = 'pano' # Videos/'vname'/pano ------> VIDEO_PATH + vname + PANO_PATH
PANO_UNCUT_PATH = '%s/download'%PANO_PATH # Video/'vname'/pano/download
PANO_CUT_PATH = '%s/cut' %PANO_PATH # Video/'vname'/pano/cut


# The function is to get the related folder of video
def GetPath(video_name): #GetPath('ZCTXXXX')
    video_path = VIDEO_PATH + '/' + video_name
    if not(os.path.isdir(video_path)):
        print 'error video dir'
    pano_path = video_path + '/' + PANO_PATH
    pano_uncut_path = video_path + '/' + PANO_UNCUT_PATH
    pano_cut_path = video_path + '/' + PANO_CUT_PATH
    output = dict({'video_path':video_path, 'pano_path':pano_path, 'pano_uncut_path':pano_uncut_path, 'pano_cut_path':pano_cut_path})

    return output
