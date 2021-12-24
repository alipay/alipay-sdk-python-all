#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayUserWufufukaAliyunExchangeResponse(AlipayResponse):

    def __init__(self):
        super(AlipayUserWufufukaAliyunExchangeResponse, self).__init__()
        self._refund_flag = None

    @property
    def refund_flag(self):
        return self._refund_flag

    @refund_flag.setter
    def refund_flag(self, value):
        self._refund_flag = value

    def parse_response_content(self, response_content):
        response = super(AlipayUserWufufukaAliyunExchangeResponse, self).parse_response_content(response_content)
        if 'refund_flag' in response:
            self.refund_flag = response['refund_flag']
