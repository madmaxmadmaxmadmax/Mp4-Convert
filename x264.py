# PY
# -*- coding: utf-8 -*-
#
#  x264.py
#
#  Copyright 2014 madmax <madmaxxx@email.it>
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#
#

MYWIDTH = 1280
DIV = 16
LANGUAGE = "ita"
BITRATE = 224
FREQUENCY = 48000
AUDIO_CODEC = ("Faac", "LavAAC", "FDK_AAC")
AQ = "20"
ULTRAFAST_OLD = ("x264", "useAdvancedConfiguration=True", "general.params=AQ=" + AQ,
                 "general.threads=0", "general.preset=ultrafast", "general.tuning=film",
                 "general.profile=baseline", "general.fast_decode=False", "general.zero_latency=False",
                 "general.fast_first_pass=True", "level=-1", "vui.sar_height=1", "vui.sar_width=1",
                 "MaxRefFrames=1", "MinIdr=23", "MaxIdr=250", "i_scenecut_threshold=0",
                 "intra_refresh=False", "MaxBFrame=0", "i_bframe_adaptive=0", "i_bframe_bias=0",
                 "i_bframe_pyramid=0", "b_deblocking_filter=True", "i_deblocking_filter_alphac0=0",
                 "i_deblocking_filter_beta=0", "cabac=False", "interlaced=False",
                 "constrained_intra=False", "tff=True", "fake_interlaced=False", "analyze.b_8x8=False",
                 "analyze.b_i4x4=True", "analyze.b_i8x8=True", "analyze.b_p8x8=False",
                 "analyze.b_p16x16=True", "analyze.b_b16x16=True", "analyze.weighted_pred=0",
                 "analyze.weighted_bipred=False", "analyze.direct_mv_pred=1", "analyze.chroma_offset=0",
                 "analyze.me_method=0", "analyze.me_range=16", "analyze.mv_range=-1",
                 "analyze.mv_range_thread=-1", "analyze.subpel_refine=1", "analyze.chroma_me=True",
                 "analyze.mixed_references=False", "analyze.trellis=0", "analyze.psy_rd=1.000000",
                 "analyze.psy_trellis=0.000000", "analyze.fast_pskip=True", "analyze.dct_decimate=True",
                 "analyze.noise_reduction=0", "analyze.psy=True", "analyze.intra_luma=11",
                 "analyze.inter_luma=21", "ratecontrol.rc_method=0", "ratecontrol.qp_constant=0",
                 "ratecontrol.qp_min=0", "ratecontrol.qp_max=69", "ratecontrol.qp_step=4",
                 "ratecontrol.bitrate=0", "ratecontrol.rate_tolerance=1.000000",
                 "ratecontrol.vbv_max_bitrate=0", "ratecontrol.vbv_buffer_size=0",
                 "ratecontrol.vbv_buffer_init=0", "ratecontrol.ip_factor=1.400000",
                 "ratecontrol.pb_factor=1.300000", "ratecontrol.aq_mode=1",
                 "ratecontrol.aq_strength=1.000000", "ratecontrol.mb_tree=False",
                 "ratecontrol.lookahead=10")
VERYFAST_OLD = ("x264", "useAdvancedConfiguration=True", "general.params=AQ=" + AQ,
                "general.threads=0", "general.preset=ultrafast", "general.tuning=film",
                "general.profile=baseline", "general.fast_decode=False", "general.zero_latency=False",
                "general.fast_first_pass=True", "level=-1", "vui.sar_height=1", "vui.sar_width=1",
                "MaxRefFrames=1", "MinIdr=23", "MaxIdr=250", "i_scenecut_threshold=40",
                "intra_refresh=False", "MaxBFrame=3", "i_bframe_adaptive=1", "i_bframe_bias=0",
                "i_bframe_pyramid=2", "b_deblocking_filter=True", "i_deblocking_filter_alphac0=0",
                "i_deblocking_filter_beta=0", "cabac=True", "interlaced=False",
                "constrained_intra=False", "tff=True", "fake_interlaced=False",
                "analyze.b_8x8=True", "analyze.b_i4x4=True", "analyze.b_i8x8=True",
                "analyze.b_p8x8=False", "analyze.b_p16x16=True", "analyze.b_b16x16=True",
                "analyze.weighted_pred=1", "analyze.weighted_bipred=True", "analyze.direct_mv_pred=1",
                "analyze.chroma_offset=0", "analyze.me_method=1", "analyze.me_range=16",
                "analyze.mv_range=-1", "analyze.mv_range_thread=-1", "analyze.subpel_refine=2",
                "analyze.chroma_me=True", "analyze.mixed_references=False", "analyze.trellis=0",
                "analyze.psy_rd=1.000000", "analyze.psy_trellis=0.000000", "analyze.fast_pskip=True",
                "analyze.dct_decimate=True", "analyze.noise_reduction=0", "analyze.psy=True",
                "analyze.intra_luma=11", "analyze.inter_luma=21", "ratecontrol.rc_method=0",
                "ratecontrol.qp_constant=0", "ratecontrol.qp_min=0", "ratecontrol.qp_max=69",
                "ratecontrol.qp_step=4", "ratecontrol.bitrate=0", "ratecontrol.rate_tolerance=1.000000",
                "ratecontrol.vbv_max_bitrate=0", "ratecontrol.vbv_buffer_size=0",
                "ratecontrol.vbv_buffer_init=0", "ratecontrol.ip_factor=1.400000",
                "ratecontrol.pb_factor=1.300000", "ratecontrol.aq_mode=1",
                "ratecontrol.aq_strength=1.000000", "ratecontrol.mb_tree=True",
                "ratecontrol.lookahead=10")
FAST_OLD = ("x264", "useAdvancedConfiguration=True", "general.params=AQ=" + AQ,
            "general.threads=0", "general.preset=ultrafast", "general.tuning=film",
            "general.profile=baseline", "general.fast_decode=False", "general.zero_latency=False",
            "general.fast_first_pass=True", "level=31", "vui.sar_height=1", "vui.sar_width=1",
            "MaxRefFrames=2", "MinIdr=23", "MaxIdr=250", "i_scenecut_threshold=40",
            "intra_refresh=False", "MaxBFrame=3", "i_bframe_adaptive=1", "i_bframe_bias=0",
            "i_bframe_pyramid=2", "b_deblocking_filter=True", "i_deblocking_filter_alphac0=0",
            "i_deblocking_filter_beta=0", "cabac=True", "interlaced=False",
            "constrained_intra=False", "tff=True", "fake_interlaced=False", "analyze.b_8x8=True",
            "analyze.b_i4x4=True", "analyze.b_i8x8=True", "analyze.b_p8x8=False",
            "analyze.b_p16x16=True", "analyze.b_b16x16=True", "analyze.weighted_pred=1",
            "analyze.weighted_bipred=True", "analyze.direct_mv_pred=1", "analyze.chroma_offset=0",
            "analyze.me_method=1", "analyze.me_range=16", "analyze.mv_range=-1",
            "analyze.mv_range_thread=-1", "analyze.subpel_refine=6", "analyze.chroma_me=True",
            "analyze.mixed_references=True", "analyze.trellis=1", "analyze.psy_rd=1.000000",
            "analyze.psy_trellis=0.000000", "analyze.fast_pskip=True", "analyze.dct_decimate=True",
            "analyze.noise_reduction=0", "analyze.psy=True", "analyze.intra_luma=11",
            "analyze.inter_luma=21", "ratecontrol.rc_method=0", "ratecontrol.qp_constant=0",
            "ratecontrol.qp_min=0", "ratecontrol.qp_max=69", "ratecontrol.qp_step=4",
            "ratecontrol.bitrate=0", "ratecontrol.rate_tolerance=1.000000",
            "ratecontrol.vbv_max_bitrate=0", "ratecontrol.vbv_buffer_size=0",
            "ratecontrol.vbv_buffer_init=0", "ratecontrol.ip_factor=1.400000",
            "ratecontrol.pb_factor=1.300000", "ratecontrol.aq_mode=1",
            "ratecontrol.aq_strength=1.000000", "ratecontrol.mb_tree=True",
            "ratecontrol.lookahead=30")
NORMAL = ("x264", "useAdvancedConfiguration=True", "general.params=AQ=" + AQ, "general.threads=99",
          "general.preset=", "general.tuning=", "general.profile=", "general.fast_decode=False",
          "general.zero_latency=False", "general.fast_first_pass=True",
          "general.blueray_compatibility=False", "general.fake_interlaced=False",
          "level=-1", "vui.sar_height=1", "vui.sar_width=1", "MaxRefFrames=3", "MinIdr=25",
          "MaxIdr=250", "i_scenecut_threshold=40", "intra_refresh=False", "MaxBFrame=3",
          "i_bframe_adaptive=1", "i_bframe_bias=0", "i_bframe_pyramid=2",
          "b_deblocking_filter=True", "i_deblocking_filter_alphac0=0",
          "i_deblocking_filter_beta=0", "cabac=True", "interlaced=False",
          "constrained_intra=False", "tff=True", "fake_interlaced=False", "analyze.b_8x8=True",
          "analyze.b_i4x4=True", "analyze.b_i8x8=True", "analyze.b_p8x8=True",
          "analyze.b_p16x16=False", "analyze.b_b16x16=False", "analyze.weighted_pred=2",
          "analyze.weighted_bipred=True", "analyze.direct_mv_pred=1",
          "analyze.chroma_offset=0", "analyze.me_method=1", "analyze.me_range=16",
          "analyze.mv_range=-1", "analyze.mv_range_thread=-1", "analyze.subpel_refine=7",
          "analyze.chroma_me=True", "analyze.mixed_references=True", "analyze.trellis=1",
          "analyze.psy_rd=1.000000", "analyze.psy_trellis=0.000000",
          "analyze.fast_pskip=True", "analyze.dct_decimate=True",
          "analyze.noise_reduction=0", "analyze.psy=True", "analyze.intra_luma=11",
          "analyze.inter_luma=21", "ratecontrol.rc_method=0", "ratecontrol.qp_constant=0",
          "ratecontrol.qp_min=10", "ratecontrol.qp_max=51", "ratecontrol.qp_step=4",
          "ratecontrol.bitrate=0", "ratecontrol.rate_tolerance=1.000000",
          "ratecontrol.vbv_max_bitrate=0", "ratecontrol.vbv_buffer_size=0",
          "ratecontrol.vbv_buffer_init=1", "ratecontrol.ip_factor=1.400000",
          "ratecontrol.pb_factor=1.300000", "ratecontrol.aq_mode=1",
          "ratecontrol.aq_strength=1.000000", "ratecontrol.mb_tree=True", "ratecontrol.lookahead=40")
ULTRAFAST = ("x264", "useAdvancedConfiguration=True", "general.params=AQ=" + AQ, "general.threads=99",
             "general.preset=ultrafast", "general.tuning=none", "general.profile=baseline",
             "general.fast_decode=False", "general.zero_latency=False", "general.fast_first_pass=True",
             "general.blueray_compatibility=False", "general.fake_interlaced=False", "level=-1", "vui.sar_height=1",
             "vui.sar_width=1", "MaxRefFrames=1", "MinIdr=23", "MaxIdr=250", "i_scenecut_threshold=0",
             "intra_refresh=False", "MaxBFrame=0", "i_bframe_adaptive=0", "i_bframe_bias=0", "i_bframe_pyramid=0",
             "b_deblocking_filter=True", "i_deblocking_filter_alphac0=0", "i_deblocking_filter_beta=0",
             "cabac=False", "interlaced=False", "constrained_intra=False", "tff=True", "fake_interlaced=False",
             "analyze.b_8x8=False", "analyze.b_i4x4=True", "analyze.b_i8x8=True", "analyze.b_p8x8=False",
             "analyze.b_p16x16=True", "analyze.b_b16x16=True", "analyze.weighted_pred=0",
             "analyze.weighted_bipred=False", "analyze.direct_mv_pred=1", "analyze.chroma_offset=0",
             "analyze.me_method=0", "analyze.me_range=16", "analyze.mv_range=-1", "analyze.mv_range_thread=-1",
             "analyze.subpel_refine=1", "analyze.chroma_me=True", "analyze.mixed_references=False",
             "analyze.trellis=0", "analyze.psy_rd=1.000000", "analyze.psy_trellis=0.000000",
             "analyze.fast_pskip=True", "analyze.dct_decimate=True", "analyze.noise_reduction=0",
             "analyze.psy=True", "analyze.intra_luma=11", "analyze.inter_luma=21", "ratecontrol.rc_method=0",
             "ratecontrol.qp_constant=0", "ratecontrol.qp_min=0", "ratecontrol.qp_max=69", "ratecontrol.qp_step=4",
             "ratecontrol.bitrate=0", "ratecontrol.rate_tolerance=1.000000", "ratecontrol.vbv_max_bitrate=0",
             "ratecontrol.vbv_buffer_size=0", "ratecontrol.vbv_buffer_init=0", "ratecontrol.ip_factor=1.400000",
             "ratecontrol.pb_factor=1.300000", "ratecontrol.aq_mode=1", "ratecontrol.aq_strength=1.000000",
             "ratecontrol.mb_tree=False", "ratecontrol.lookahead=10")
VERYFAST = ("x264", "useAdvancedConfiguration=True", "general.params=AQ=" + AQ, "general.threads=99",
            "general.preset=ultrafast", "general.tuning=none", "general.profile=baseline",
            "general.fast_decode=False", "general.zero_latency=False", "general.fast_first_pass=True",
            "general.blueray_compatibility=False", "general.fake_interlaced=False", "level=-1", "vui.sar_height=1",
            "vui.sar_width=1", "MaxRefFrames=1", "MinIdr=23", "MaxIdr=250", "i_scenecut_threshold=40",
            "intra_refresh=False", "MaxBFrame=3", "i_bframe_adaptive=1", "i_bframe_bias=0", "i_bframe_pyramid=2",
            "b_deblocking_filter=True", "i_deblocking_filter_alphac0=0", "i_deblocking_filter_beta=0",
            "cabac=True", "interlaced=False", "constrained_intra=False", "tff=True", "fake_interlaced=False",
            "analyze.b_8x8=True", "analyze.b_i4x4=True", "analyze.b_i8x8=True", "analyze.b_p8x8=False",
            "analyze.b_p16x16=True", "analyze.b_b16x16=True", "analyze.weighted_pred=1",
            "analyze.weighted_bipred=True", "analyze.direct_mv_pred=1", "analyze.chroma_offset=0",
            "analyze.me_method=1", "analyze.me_range=16", "analyze.mv_range=-1", "analyze.mv_range_thread=-1",
            "analyze.subpel_refine=2", "analyze.chroma_me=True", "analyze.mixed_references=False",
            "analyze.trellis=0", "analyze.psy_rd=1.000000", "analyze.psy_trellis=0.000000",
            "analyze.fast_pskip=True", "analyze.dct_decimate=True", "analyze.noise_reduction=0",
            "analyze.psy=True", "analyze.intra_luma=11", "analyze.inter_luma=21", "ratecontrol.rc_method=0",
            "ratecontrol.qp_constant=0", "ratecontrol.qp_min=0", "ratecontrol.qp_max=69", "ratecontrol.qp_step=4",
            "ratecontrol.bitrate=0", "ratecontrol.rate_tolerance=1.000000", "ratecontrol.vbv_max_bitrate=0",
            "ratecontrol.vbv_buffer_size=0", "ratecontrol.vbv_buffer_init=0", "ratecontrol.ip_factor=1.400000",
            "ratecontrol.pb_factor=1.300000", "ratecontrol.aq_mode=1", "ratecontrol.aq_strength=1.000000",
            "ratecontrol.mb_tree=True", "ratecontrol.lookahead=10")
FAST = ("x264", "useAdvancedConfiguration=True", "general.params=AQ=" + AQ, "general.threads=99",
        "general.preset=ultrafast", "general.tuning=none", "general.profile=baseline",
        "general.fast_decode=False", "general.zero_latency=False", "general.fast_first_pass=True",
        "general.blueray_compatibility=False", "general.fake_interlaced=False", "level=31", "vui.sar_height=1",
        "vui.sar_width=1", "MaxRefFrames=2", "MinIdr=23", "MaxIdr=250", "i_scenecut_threshold=40",
        "intra_refresh=False", "MaxBFrame=3", "i_bframe_adaptive=1", "i_bframe_bias=0", "i_bframe_pyramid=2",
        "b_deblocking_filter=True", "i_deblocking_filter_alphac0=0", "i_deblocking_filter_beta=0",
        "cabac=True", "interlaced=False", "constrained_intra=False", "tff=True", "fake_interlaced=False",
        "analyze.b_8x8=True", "analyze.b_i4x4=True", "analyze.b_i8x8=True", "analyze.b_p8x8=False",
        "analyze.b_p16x16=True", "analyze.b_b16x16=True", "analyze.weighted_pred=1",
        "analyze.weighted_bipred=True", "analyze.direct_mv_pred=1", "analyze.chroma_offset=0",
        "analyze.me_method=1", "analyze.me_range=16", "analyze.mv_range=-1", "analyze.mv_range_thread=-1",
        "analyze.subpel_refine=6", "analyze.chroma_me=True", "analyze.mixed_references=True",
        "analyze.trellis=1", "analyze.psy_rd=1.000000", "analyze.psy_trellis=0.000000",
        "analyze.fast_pskip=True", "analyze.dct_decimate=True", "analyze.noise_reduction=0",
        "analyze.psy=True", "analyze.intra_luma=11", "analyze.inter_luma=21", "ratecontrol.rc_method=0",
        "ratecontrol.qp_constant=0", "ratecontrol.qp_min=0", "ratecontrol.qp_max=69", "ratecontrol.qp_step=4",
        "ratecontrol.bitrate=0", "ratecontrol.rate_tolerance=1.000000", "ratecontrol.vbv_max_bitrate=0",
        "ratecontrol.vbv_buffer_size=0", "ratecontrol.vbv_buffer_init=0", "ratecontrol.ip_factor=1.400000",
        "ratecontrol.pb_factor=1.300000", "ratecontrol.aq_mode=1", "ratecontrol.aq_strength=1.000000",
        "ratecontrol.mb_tree=True", "ratecontrol.lookahead=30")
X265 = ("x265", "useAdvancedConfiguration=True", "general.params=AQ=" + AQ, "general.poolThreads=99",
        "general.frameThreads=0", "general.preset=ultrafast", "general.tuning=none", "general.profile=main", "level=-1",
        "vui.sar_height=1", "vui.sar_width=1", "MaxRefFrames=3", "MinIdr=25", "MaxIdr=250", "i_scenecut_threshold=40",
        "MaxBFrame=3", "i_bframe_adaptive=1", "i_bframe_bias=0", "i_bframe_pyramid=2", "b_deblocking_filter=True",
        "interlaced_mode=0", "constrained_intra=False", "lookahead=40", "weighted_pred=2", "weighted_bipred=True",
        "cb_chroma_offset=0", "cr_chroma_offset=0", "me_method=3", "me_range=16", "subpel_refine=5", "trellis=1",
        "psy_rd=1.000000", "fast_pskip=True", "dct_decimate=True", "noise_reduction=0", "noise_reduction_intra=0",
        "noise_reduction_inter=0", "strong_intra_smoothing=True", "ratecontrol.rc_method=0",
        "ratecontrol.qp_constant=0", "ratecontrol.qp_step=4", "ratecontrol.bitrate=0",
        "ratecontrol.rate_tolerance=1.000000", "ratecontrol.vbv_max_bitrate=0", "ratecontrol.vbv_buffer_size=0",
        "ratecontrol.vbv_buffer_init=1", "ratecontrol.ip_factor=1.400000", "ratecontrol.pb_factor=1.300000",
        "ratecontrol.aq_mode=2", "ratecontrol.aq_strength=1.000000", "ratecontrol.cu_tree=True",
        "ratecontrol.strict_cbr=False")


def video_encode(adm, mywidth):
    _width = adm.getWidth()
    _height = adm.getHeight()
    if adm.getVideoCodec() == "H264" and _width <= mywidth:
        adm.videoCodec("Copy")
        return False
    adm.videoCodec(*NORMAL)
    if _width > mywidth:
        print("Need Scale...")
        _myheight = int(mywidth * _height / _width)
        _myheight = round(_myheight / DIV) * DIV
        _myheight = str(_myheight)
        mywidth = str(mywidth)
        adm.addVideoFilter("swscale", "width=" + mywidth, "height=" + _myheight, "algo=2", "sourceAR=0",
                           "targetAR=0", "lockAR=True", "roundup=True")
    return True


def audio_encode(adm, track):
    (_tracks, _encoding, _channels, _bitrate, _frequency) = (adm.audioTracksCount(), adm.audioEncoding(0),
                                                             adm.audioChannels(0), adm.audioBitrate(0),
                                                             adm.audioFrequency(0))
    if (_tracks, _encoding, _channels, _bitrate, _frequency) != (1, 255, 2, BITRATE, FREQUENCY):
        adm.audioClearTracks()
        adm.setSourceTrackLanguage(track, LANGUAGE)
        adm.audioAddTrack(track)
        adm.audioCodec(track, AUDIO_CODEC[2], "bitrate=" + str(BITRATE))
        adm.audioSetResample(track, FREQUENCY)
        adm.audioSetMixer(track, "STEREO")
        adm.audioSetDrc(0, 0)
        adm.audioSetShift(0, 0, 0)
        adm.audioSetNormalize2(0, 1, 10, 0)
        return True
    adm.audioCodec(0, "copy")
    return False


adm = Avidemux()
adm.setPostProc(3, 3, 0)
video_encode(adm, MYWIDTH)
audio_encode(adm, 0)
adm.setContainer("AVI", "odmlType=1")
