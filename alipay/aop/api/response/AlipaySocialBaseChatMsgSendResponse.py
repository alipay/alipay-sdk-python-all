#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipaySocialBaseChatMsgSendResponse(AlipayResponse):

    def __init__(self):
        super(AlipaySocialBaseChatMsgSendResponse, self).__init__()
        self._msg_index = None

    @property
    def msg_index(self):
        return self._msg_index

    @msg_index.setter
    def msg_index(self, value):
        self._msg_index = value

    def parse_response_content(self, response_content):
        response = super(AlipaySocialBaseChatMsgSendResponse, self).parse_response_content(response_content)
        if 'msg_index' in response:
            self.msg_index = response['msg_index']
