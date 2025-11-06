#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceMedicalHdfrtcReconnectioninfoQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalHdfrtcReconnectioninfoQueryResponse, self).__init__()
        self._channel_id = None
        self._if_video_conference_reconnect = None
        self._source_id = None
        self._tips = None
        self._video_conference_id = None

    @property
    def channel_id(self):
        return self._channel_id

    @channel_id.setter
    def channel_id(self, value):
        self._channel_id = value
    @property
    def if_video_conference_reconnect(self):
        return self._if_video_conference_reconnect

    @if_video_conference_reconnect.setter
    def if_video_conference_reconnect(self, value):
        self._if_video_conference_reconnect = value
    @property
    def source_id(self):
        return self._source_id

    @source_id.setter
    def source_id(self, value):
        self._source_id = value
    @property
    def tips(self):
        return self._tips

    @tips.setter
    def tips(self, value):
        self._tips = value
    @property
    def video_conference_id(self):
        return self._video_conference_id

    @video_conference_id.setter
    def video_conference_id(self, value):
        self._video_conference_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalHdfrtcReconnectioninfoQueryResponse, self).parse_response_content(response_content)
        if 'channel_id' in response:
            self.channel_id = response['channel_id']
        if 'if_video_conference_reconnect' in response:
            self.if_video_conference_reconnect = response['if_video_conference_reconnect']
        if 'source_id' in response:
            self.source_id = response['source_id']
        if 'tips' in response:
            self.tips = response['tips']
        if 'video_conference_id' in response:
            self.video_conference_id = response['video_conference_id']
