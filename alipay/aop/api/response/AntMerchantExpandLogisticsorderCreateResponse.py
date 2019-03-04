#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AntMerchantExpandLogisticsorderCreateResponse(AlipayResponse):

    def __init__(self):
        super(AntMerchantExpandLogisticsorderCreateResponse, self).__init__()
        self._logistics_order_id = None

    @property
    def logistics_order_id(self):
        return self._logistics_order_id

    @logistics_order_id.setter
    def logistics_order_id(self, value):
        self._logistics_order_id = value

    def parse_response_content(self, response_content):
        response = super(AntMerchantExpandLogisticsorderCreateResponse, self).parse_response_content(response_content)
        if 'logistics_order_id' in response:
            self.logistics_order_id = response['logistics_order_id']
