#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayAccountExrateRateSyncResponse(AlipayResponse):

    def __init__(self):
        super(AlipayAccountExrateRateSyncResponse, self).__init__()
        self._result_context = None

    @property
    def result_context(self):
        return self._result_context

    @result_context.setter
    def result_context(self, value):
        self._result_context = value

    def parse_response_content(self, response_content):
        response = super(AlipayAccountExrateRateSyncResponse, self).parse_response_content(response_content)
        if 'result_context' in response:
            self.result_context = response['result_context']
