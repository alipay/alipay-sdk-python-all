#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.AudioInfo import AudioInfo
from alipay.aop.api.domain.AudioInfo import AudioInfo


class AlipayIserviceCcmCrmOneaudioQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayIserviceCcmCrmOneaudioQueryResponse, self).__init__()
        self._acid = None
        self._ivr_audio = None
        self._one_audio = None

    @property
    def acid(self):
        return self._acid

    @acid.setter
    def acid(self, value):
        self._acid = value
    @property
    def ivr_audio(self):
        return self._ivr_audio

    @ivr_audio.setter
    def ivr_audio(self, value):
        if isinstance(value, AudioInfo):
            self._ivr_audio = value
        else:
            self._ivr_audio = AudioInfo.from_alipay_dict(value)
    @property
    def one_audio(self):
        return self._one_audio

    @one_audio.setter
    def one_audio(self, value):
        if isinstance(value, AudioInfo):
            self._one_audio = value
        else:
            self._one_audio = AudioInfo.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayIserviceCcmCrmOneaudioQueryResponse, self).parse_response_content(response_content)
        if 'acid' in response:
            self.acid = response['acid']
        if 'ivr_audio' in response:
            self.ivr_audio = response['ivr_audio']
        if 'one_audio' in response:
            self.one_audio = response['one_audio']
