#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayMarketingGoodsDataVerifyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMarketingGoodsDataVerifyResponse, self).__init__()
        self._order_id = None
        self._result_info = None

    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        self._order_id = value
    @property
    def result_info(self):
        return self._result_info

    @result_info.setter
    def result_info(self, value):
        self._result_info = value

    def parse_response_content(self, response_content):
        response = super(AlipayMarketingGoodsDataVerifyResponse, self).parse_response_content(response_content)
        if 'order_id' in response:
            self.order_id = response['order_id']
        if 'result_info' in response:
            self.result_info = response['result_info']
