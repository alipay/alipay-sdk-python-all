#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayMerchantGroupGroupmsgSendResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMerchantGroupGroupmsgSendResponse, self).__init__()
        self._msg_id = None

    @property
    def msg_id(self):
        return self._msg_id

    @msg_id.setter
    def msg_id(self, value):
        self._msg_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayMerchantGroupGroupmsgSendResponse, self).parse_response_content(response_content)
        if 'msg_id' in response:
            self.msg_id = response['msg_id']
