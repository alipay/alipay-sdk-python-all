#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipaySocialBaseMessageDynamicicondataModifyResponse(AlipayResponse):

    def __init__(self):
        super(AlipaySocialBaseMessageDynamicicondataModifyResponse, self).__init__()
        self._op_result = None

    @property
    def op_result(self):
        return self._op_result

    @op_result.setter
    def op_result(self, value):
        self._op_result = value

    def parse_response_content(self, response_content):
        response = super(AlipaySocialBaseMessageDynamicicondataModifyResponse, self).parse_response_content(response_content)
        if 'op_result' in response:
            self.op_result = response['op_result']
