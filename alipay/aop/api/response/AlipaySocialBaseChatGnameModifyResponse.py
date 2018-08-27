#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipaySocialBaseChatGnameModifyResponse(AlipayResponse):

    def __init__(self):
        super(AlipaySocialBaseChatGnameModifyResponse, self).__init__()
        self._result_modify = None

    @property
    def result_modify(self):
        return self._result_modify

    @result_modify.setter
    def result_modify(self, value):
        self._result_modify = value

    def parse_response_content(self, response_content):
        response = super(AlipaySocialBaseChatGnameModifyResponse, self).parse_response_content(response_content)
        if 'result_modify' in response:
            self.result_modify = response['result_modify']
