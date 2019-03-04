#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayUserAntarchiveFaceIdentifyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayUserAntarchiveFaceIdentifyResponse, self).__init__()
        self._score = None

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        self._score = value

    def parse_response_content(self, response_content):
        response = super(AlipayUserAntarchiveFaceIdentifyResponse, self).parse_response_content(response_content)
        if 'score' in response:
            self.score = response['score']
