#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AntMerchantExpandIndirectActivityCreateResponse(AlipayResponse):

    def __init__(self):
        super(AntMerchantExpandIndirectActivityCreateResponse, self).__init__()
        self._has_apply = None
        self._order_id = None

    @property
    def has_apply(self):
        return self._has_apply

    @has_apply.setter
    def has_apply(self, value):
        self._has_apply = value
    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        self._order_id = value

    def parse_response_content(self, response_content):
        response = super(AntMerchantExpandIndirectActivityCreateResponse, self).parse_response_content(response_content)
        if 'has_apply' in response:
            self.has_apply = response['has_apply']
        if 'order_id' in response:
            self.order_id = response['order_id']
