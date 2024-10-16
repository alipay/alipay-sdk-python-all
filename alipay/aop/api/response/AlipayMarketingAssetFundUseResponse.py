#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayMarketingAssetFundUseResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMarketingAssetFundUseResponse, self).__init__()
        self._use_order_id = None

    @property
    def use_order_id(self):
        return self._use_order_id

    @use_order_id.setter
    def use_order_id(self, value):
        self._use_order_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayMarketingAssetFundUseResponse, self).parse_response_content(response_content)
        if 'use_order_id' in response:
            self.use_order_id = response['use_order_id']
