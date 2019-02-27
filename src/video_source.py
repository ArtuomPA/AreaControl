#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys


class VideoSource:
    def __init__(self, ap):
        ap.add_argument("-v1", "--video1",
            help="path to the video file 1")
        ap.add_argument("-v2", "--video2",
            help="path to the video file 2")
        args = vars(ap.parse_args())

        if not args.get("video1", False):
            self.video1 = sys.path[0]+'/../videos/moovy1.mp4'
        else:
            self.video1 = args["video1"]
        if not args.get("video2", False):
            self.video2 = sys.path[0]+'/../videos/moovy2.mp4'
        else:
            self.video2 = args["video2"]

    def getVid1(self):
        return self.video1

    def getVid2(self):
        return self.video2

