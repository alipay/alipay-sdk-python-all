#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayDigitalmgmtEmbenefitVideoplayinfoQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayDigitalmgmtEmbenefitVideoplayinfoQueryResponse, self).__init__()
        self._attachment_id = None
        self._attachment_name = None
        self._duration = None
        self._play_url = None
        self._size = None
        self._video_id = None

    @property
    def attachment_id(self):
        return self._attachment_id

    @attachment_id.setter
    def attachment_id(self, value):
        self._attachment_id = value
    @property
    def attachment_name(self):
        return self._attachment_name

    @attachment_name.setter
    def attachment_name(self, value):
        self._attachment_name = value
    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, value):
        self._duration = value
    @property
    def play_url(self):
        return self._play_url

    @play_url.setter
    def play_url(self, value):
        self._play_url = value
    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        self._size = value
    @property
    def video_id(self):
        return self._video_id

    @video_id.setter
    def video_id(self, value):
        self._video_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayDigitalmgmtEmbenefitVideoplayinfoQueryResponse, self).parse_response_content(response_content)
        if 'attachment_id' in response:
            self.attachment_id = response['attachment_id']
        if 'attachment_name' in response:
            self.attachment_name = response['attachment_name']
        if 'duration' in response:
            self.duration = response['duration']
        if 'play_url' in response:
            self.play_url = response['play_url']
        if 'size' in response:
            self.size = response['size']
        if 'video_id' in response:
            self.video_id = response['video_id']
