#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.AliveSubtitleExt import AliveSubtitleExt


class AntfortuneContentCommunitySubtitleQueryResponse(AlipayResponse):

    def __init__(self):
        super(AntfortuneContentCommunitySubtitleQueryResponse, self).__init__()
        self._content = None
        self._ext = None
        self._live_id = None

    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, value):
        self._content = value
    @property
    def ext(self):
        return self._ext

    @ext.setter
    def ext(self, value):
        if isinstance(value, AliveSubtitleExt):
            self._ext = value
        else:
            self._ext = AliveSubtitleExt.from_alipay_dict(value)
    @property
    def live_id(self):
        return self._live_id

    @live_id.setter
    def live_id(self, value):
        self._live_id = value

    def parse_response_content(self, response_content):
        response = super(AntfortuneContentCommunitySubtitleQueryResponse, self).parse_response_content(response_content)
        if 'content' in response:
            self.content = response['content']
        if 'ext' in response:
            self.ext = response['ext']
        if 'live_id' in response:
            self.live_id = response['live_id']
