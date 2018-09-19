#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayInsScenePolicyEndorseApplyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayInsScenePolicyEndorseApplyResponse, self).__init__()
        self._endorse_no = None
        self._out_request_no = None

    @property
    def endorse_no(self):
        return self._endorse_no

    @endorse_no.setter
    def endorse_no(self, value):
        self._endorse_no = value
    @property
    def out_request_no(self):
        return self._out_request_no

    @out_request_no.setter
    def out_request_no(self, value):
        self._out_request_no = value

    def parse_response_content(self, response_content):
        response = super(AlipayInsScenePolicyEndorseApplyResponse, self).parse_response_content(response_content)
        if 'endorse_no' in response:
            self.endorse_no = response['endorse_no']
        if 'out_request_no' in response:
            self.out_request_no = response['out_request_no']
