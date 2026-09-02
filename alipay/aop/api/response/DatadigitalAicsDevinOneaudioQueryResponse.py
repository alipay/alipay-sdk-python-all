#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.DtAudioInfo import DtAudioInfo
from alipay.aop.api.domain.DtAudioInfo import DtAudioInfo


class DatadigitalAicsDevinOneaudioQueryResponse(AlipayResponse):

    def __init__(self):
        super(DatadigitalAicsDevinOneaudioQueryResponse, self).__init__()
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
        if isinstance(value, DtAudioInfo):
            self._ivr_audio = value
        else:
            self._ivr_audio = DtAudioInfo.from_alipay_dict(value)
    @property
    def one_audio(self):
        return self._one_audio

    @one_audio.setter
    def one_audio(self, value):
        if isinstance(value, DtAudioInfo):
            self._one_audio = value
        else:
            self._one_audio = DtAudioInfo.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(DatadigitalAicsDevinOneaudioQueryResponse, self).parse_response_content(response_content)
        if 'acid' in response:
            self.acid = response['acid']
        if 'ivr_audio' in response:
            self.ivr_audio = response['ivr_audio']
        if 'one_audio' in response:
            self.one_audio = response['one_audio']
