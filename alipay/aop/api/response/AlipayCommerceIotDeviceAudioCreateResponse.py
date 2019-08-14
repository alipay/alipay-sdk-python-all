#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceIotDeviceAudioCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceIotDeviceAudioCreateResponse, self).__init__()
        self._audio_id = None
        self._audio_url = None

    @property
    def audio_id(self):
        return self._audio_id

    @audio_id.setter
    def audio_id(self, value):
        self._audio_id = value
    @property
    def audio_url(self):
        return self._audio_url

    @audio_url.setter
    def audio_url(self, value):
        self._audio_url = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceIotDeviceAudioCreateResponse, self).parse_response_content(response_content)
        if 'audio_id' in response:
            self.audio_id = response['audio_id']
        if 'audio_url' in response:
            self.audio_url = response['audio_url']
