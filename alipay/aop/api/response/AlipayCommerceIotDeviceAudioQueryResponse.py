#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceIotDeviceAudioQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceIotDeviceAudioQueryResponse, self).__init__()
        self._audio_list = None

    @property
    def audio_list(self):
        return self._audio_list

    @audio_list.setter
    def audio_list(self, value):
        self._audio_list = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceIotDeviceAudioQueryResponse, self).parse_response_content(response_content)
        if 'audio_list' in response:
            self.audio_list = response['audio_list']
