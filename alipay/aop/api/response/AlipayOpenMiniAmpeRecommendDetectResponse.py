#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenMiniAmpeRecommendDetectResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenMiniAmpeRecommendDetectResponse, self).__init__()
        self._valid = None

    @property
    def valid(self):
        return self._valid

    @valid.setter
    def valid(self, value):
        self._valid = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenMiniAmpeRecommendDetectResponse, self).parse_response_content(response_content)
        if 'valid' in response:
            self.valid = response['valid']
