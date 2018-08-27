#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayMsaasMediarecogAftsCarIdentifyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMsaasMediarecogAftsCarIdentifyResponse, self).__init__()
        self._cheat_probability = None
        self._cheat_type = None
        self._ocr_kilometres = None
        self._ocr_probability = None

    @property
    def cheat_probability(self):
        return self._cheat_probability

    @cheat_probability.setter
    def cheat_probability(self, value):
        self._cheat_probability = value
    @property
    def cheat_type(self):
        return self._cheat_type

    @cheat_type.setter
    def cheat_type(self, value):
        self._cheat_type = value
    @property
    def ocr_kilometres(self):
        return self._ocr_kilometres

    @ocr_kilometres.setter
    def ocr_kilometres(self, value):
        self._ocr_kilometres = value
    @property
    def ocr_probability(self):
        return self._ocr_probability

    @ocr_probability.setter
    def ocr_probability(self, value):
        self._ocr_probability = value

    def parse_response_content(self, response_content):
        response = super(AlipayMsaasMediarecogAftsCarIdentifyResponse, self).parse_response_content(response_content)
        if 'cheat_probability' in response:
            self.cheat_probability = response['cheat_probability']
        if 'cheat_type' in response:
            self.cheat_type = response['cheat_type']
        if 'ocr_kilometres' in response:
            self.ocr_kilometres = response['ocr_kilometres']
        if 'ocr_probability' in response:
            self.ocr_probability = response['ocr_probability']
