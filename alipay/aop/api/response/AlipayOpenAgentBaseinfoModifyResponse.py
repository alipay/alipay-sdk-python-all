#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenAgentBaseinfoModifyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenAgentBaseinfoModifyResponse, self).__init__()
        self._reject_resion = None
        self._safe_result = None

    @property
    def reject_resion(self):
        return self._reject_resion

    @reject_resion.setter
    def reject_resion(self, value):
        self._reject_resion = value
    @property
    def safe_result(self):
        return self._safe_result

    @safe_result.setter
    def safe_result(self, value):
        self._safe_result = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenAgentBaseinfoModifyResponse, self).parse_response_content(response_content)
        if 'reject_resion' in response:
            self.reject_resion = response['reject_resion']
        if 'safe_result' in response:
            self.safe_result = response['safe_result']
