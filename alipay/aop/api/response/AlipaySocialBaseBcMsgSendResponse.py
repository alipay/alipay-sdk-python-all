#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipaySocialBaseBcMsgSendResponse(AlipayResponse):

    def __init__(self):
        super(AlipaySocialBaseBcMsgSendResponse, self).__init__()
        self._sub_code = None
        self._sub_msg = None

    @property
    def sub_code(self):
        return self._sub_code

    @sub_code.setter
    def sub_code(self, value):
        self._sub_code = value
    @property
    def sub_msg(self):
        return self._sub_msg

    @sub_msg.setter
    def sub_msg(self, value):
        self._sub_msg = value

    def parse_response_content(self, response_content):
        response = super(AlipaySocialBaseBcMsgSendResponse, self).parse_response_content(response_content)
        if 'sub_code' in response:
            self.sub_code = response['sub_code']
        if 'sub_msg' in response:
            self.sub_msg = response['sub_msg']
