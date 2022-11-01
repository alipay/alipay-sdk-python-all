#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenOpenbizmockAppidDetectResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenOpenbizmockAppidDetectResponse, self).__init__()
        self._detect_response = None

    @property
    def detect_response(self):
        return self._detect_response

    @detect_response.setter
    def detect_response(self, value):
        self._detect_response = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenOpenbizmockAppidDetectResponse, self).parse_response_content(response_content)
        if 'detect_response' in response:
            self.detect_response = response['detect_response']
