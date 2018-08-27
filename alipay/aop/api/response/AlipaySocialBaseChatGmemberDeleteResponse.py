#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipaySocialBaseChatGmemberDeleteResponse(AlipayResponse):

    def __init__(self):
        super(AlipaySocialBaseChatGmemberDeleteResponse, self).__init__()
        self._result_delete = None

    @property
    def result_delete(self):
        return self._result_delete

    @result_delete.setter
    def result_delete(self, value):
        self._result_delete = value

    def parse_response_content(self, response_content):
        response = super(AlipaySocialBaseChatGmemberDeleteResponse, self).parse_response_content(response_content)
        if 'result_delete' in response:
            self.result_delete = response['result_delete']
