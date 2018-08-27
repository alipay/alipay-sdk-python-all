#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipaySocialBaseChatGmemberConfirmResponse(AlipayResponse):

    def __init__(self):
        super(AlipaySocialBaseChatGmemberConfirmResponse, self).__init__()
        self._group_id = None
        self._result = None

    @property
    def group_id(self):
        return self._group_id

    @group_id.setter
    def group_id(self, value):
        self._group_id = value
    @property
    def result(self):
        return self._result

    @result.setter
    def result(self, value):
        self._result = value

    def parse_response_content(self, response_content):
        response = super(AlipaySocialBaseChatGmemberConfirmResponse, self).parse_response_content(response_content)
        if 'group_id' in response:
            self.group_id = response['group_id']
        if 'result' in response:
            self.result = response['result']
