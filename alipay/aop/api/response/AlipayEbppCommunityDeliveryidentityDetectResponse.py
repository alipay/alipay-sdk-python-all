#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayEbppCommunityDeliveryidentityDetectResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEbppCommunityDeliveryidentityDetectResponse, self).__init__()
        self._detect_result = None

    @property
    def detect_result(self):
        return self._detect_result

    @detect_result.setter
    def detect_result(self, value):
        self._detect_result = value

    def parse_response_content(self, response_content):
        response = super(AlipayEbppCommunityDeliveryidentityDetectResponse, self).parse_response_content(response_content)
        if 'detect_result' in response:
            self.detect_result = response['detect_result']
