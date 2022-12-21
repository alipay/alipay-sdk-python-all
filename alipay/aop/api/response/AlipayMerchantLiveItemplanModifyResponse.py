#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayMerchantLiveItemplanModifyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMerchantLiveItemplanModifyResponse, self).__init__()
        self._msg_info = None

    @property
    def msg_info(self):
        return self._msg_info

    @msg_info.setter
    def msg_info(self, value):
        self._msg_info = value

    def parse_response_content(self, response_content):
        response = super(AlipayMerchantLiveItemplanModifyResponse, self).parse_response_content(response_content)
        if 'msg_info' in response:
            self.msg_info = response['msg_info']
