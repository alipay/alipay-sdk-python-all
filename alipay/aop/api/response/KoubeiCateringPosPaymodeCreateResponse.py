#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class KoubeiCateringPosPaymodeCreateResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiCateringPosPaymodeCreateResponse, self).__init__()
        self._order_id = None
        self._result_code = None
        self._shop_id = None

    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        self._order_id = value
    @property
    def result_code(self):
        return self._result_code

    @result_code.setter
    def result_code(self, value):
        self._result_code = value
    @property
    def shop_id(self):
        return self._shop_id

    @shop_id.setter
    def shop_id(self, value):
        self._shop_id = value

    def parse_response_content(self, response_content):
        response = super(KoubeiCateringPosPaymodeCreateResponse, self).parse_response_content(response_content)
        if 'order_id' in response:
            self.order_id = response['order_id']
        if 'result_code' in response:
            self.result_code = response['result_code']
        if 'shop_id' in response:
            self.shop_id = response['shop_id']
