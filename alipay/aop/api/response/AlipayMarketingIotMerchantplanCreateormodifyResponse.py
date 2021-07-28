#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayMarketingIotMerchantplanCreateormodifyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMarketingIotMerchantplanCreateormodifyResponse, self).__init__()
        self._merchant_plan_id = None

    @property
    def merchant_plan_id(self):
        return self._merchant_plan_id

    @merchant_plan_id.setter
    def merchant_plan_id(self, value):
        self._merchant_plan_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayMarketingIotMerchantplanCreateormodifyResponse, self).parse_response_content(response_content)
        if 'merchant_plan_id' in response:
            self.merchant_plan_id = response['merchant_plan_id']
