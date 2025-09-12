#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ToBDiscountCustomerServiceInfo import ToBDiscountCustomerServiceInfo


class AlipayCommerceAcommunicationDiscountPhonePayResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceAcommunicationDiscountPhonePayResponse, self).__init__()
        self._alipay_biz_no = None
        self._alipay_trade_no = None
        self._customer_service_info = None

    @property
    def alipay_biz_no(self):
        return self._alipay_biz_no

    @alipay_biz_no.setter
    def alipay_biz_no(self, value):
        self._alipay_biz_no = value
    @property
    def alipay_trade_no(self):
        return self._alipay_trade_no

    @alipay_trade_no.setter
    def alipay_trade_no(self, value):
        self._alipay_trade_no = value
    @property
    def customer_service_info(self):
        return self._customer_service_info

    @customer_service_info.setter
    def customer_service_info(self, value):
        if isinstance(value, ToBDiscountCustomerServiceInfo):
            self._customer_service_info = value
        else:
            self._customer_service_info = ToBDiscountCustomerServiceInfo.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceAcommunicationDiscountPhonePayResponse, self).parse_response_content(response_content)
        if 'alipay_biz_no' in response:
            self.alipay_biz_no = response['alipay_biz_no']
        if 'alipay_trade_no' in response:
            self.alipay_trade_no = response['alipay_trade_no']
        if 'customer_service_info' in response:
            self.customer_service_info = response['customer_service_info']
