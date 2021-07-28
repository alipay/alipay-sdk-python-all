#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceIotServiceutilBuildtextSendResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceIotServiceutilBuildtextSendResponse, self).__init__()
        self._audio_id = None
        self._md_5 = None
        self._url = None

    @property
    def audio_id(self):
        return self._audio_id

    @audio_id.setter
    def audio_id(self, value):
        self._audio_id = value
    @property
    def md_5(self):
        return self._md_5

    @md_5.setter
    def md_5(self, value):
        self._md_5 = value
    @property
    def url(self):
        return self._url

    @url.setter
    def url(self, value):
        self._url = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceIotServiceutilBuildtextSendResponse, self).parse_response_content(response_content)
        if 'audio_id' in response:
            self.audio_id = response['audio_id']
        if 'md_5' in response:
            self.md_5 = response['md_5']
        if 'url' in response:
            self.url = response['url']
