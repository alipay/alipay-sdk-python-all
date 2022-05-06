#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.FloorVideo import FloorVideo


class AlipayMsaasMediarecogMmtcaftscvManualfloorQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMsaasMediarecogMmtcaftscvManualfloorQueryResponse, self).__init__()
        self._floor_videos = None
        self._video_code = None

    @property
    def floor_videos(self):
        return self._floor_videos

    @floor_videos.setter
    def floor_videos(self, value):
        if isinstance(value, list):
            self._floor_videos = list()
            for i in value:
                if isinstance(i, FloorVideo):
                    self._floor_videos.append(i)
                else:
                    self._floor_videos.append(FloorVideo.from_alipay_dict(i))
    @property
    def video_code(self):
        return self._video_code

    @video_code.setter
    def video_code(self, value):
        self._video_code = value

    def parse_response_content(self, response_content):
        response = super(AlipayMsaasMediarecogMmtcaftscvManualfloorQueryResponse, self).parse_response_content(response_content)
        if 'floor_videos' in response:
            self.floor_videos = response['floor_videos']
        if 'video_code' in response:
            self.video_code = response['video_code']
