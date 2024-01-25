#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayInsSceneInsureRecommendCheckResponse(AlipayResponse):

    def __init__(self):
        super(AlipayInsSceneInsureRecommendCheckResponse, self).__init__()
        self._access_result = None

    @property
    def access_result(self):
        return self._access_result

    @access_result.setter
    def access_result(self, value):
        self._access_result = value

    def parse_response_content(self, response_content):
        response = super(AlipayInsSceneInsureRecommendCheckResponse, self).parse_response_content(response_content)
        if 'access_result' in response:
            self.access_result = response['access_result']
