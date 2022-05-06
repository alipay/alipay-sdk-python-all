#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayMerchantOrderHahaNobizcontentCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMerchantOrderHahaNobizcontentCreateResponse, self).__init__()
        self._out = None

    @property
    def out(self):
        return self._out

    @out.setter
    def out(self, value):
        self._out = value

    def parse_response_content(self, response_content):
        response = super(AlipayMerchantOrderHahaNobizcontentCreateResponse, self).parse_response_content(response_content)
        if 'out' in response:
            self.out = response['out']
