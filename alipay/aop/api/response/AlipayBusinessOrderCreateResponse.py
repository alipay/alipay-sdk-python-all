#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.MarketingInfo import MarketingInfo


class AlipayBusinessOrderCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayBusinessOrderCreateResponse, self).__init__()
        self._confirmed_marketing = None
        self._merchant_order_no = None
        self._order_no = None

    @property
    def confirmed_marketing(self):
        return self._confirmed_marketing

    @confirmed_marketing.setter
    def confirmed_marketing(self, value):
        if isinstance(value, MarketingInfo):
            self._confirmed_marketing = value
        else:
            self._confirmed_marketing = MarketingInfo.from_alipay_dict(value)
    @property
    def merchant_order_no(self):
        return self._merchant_order_no

    @merchant_order_no.setter
    def merchant_order_no(self, value):
        self._merchant_order_no = value
    @property
    def order_no(self):
        return self._order_no

    @order_no.setter
    def order_no(self, value):
        self._order_no = value

    def parse_response_content(self, response_content):
        response = super(AlipayBusinessOrderCreateResponse, self).parse_response_content(response_content)
        if 'confirmed_marketing' in response:
            self.confirmed_marketing = response['confirmed_marketing']
        if 'merchant_order_no' in response:
            self.merchant_order_no = response['merchant_order_no']
        if 'order_no' in response:
            self.order_no = response['order_no']
