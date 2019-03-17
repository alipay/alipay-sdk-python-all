#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.PaytoolResultDetail import PaytoolResultDetail


class AlipayBusinessOrderPayResponse(AlipayResponse):

    def __init__(self):
        super(AlipayBusinessOrderPayResponse, self).__init__()
        self._merchant_order_no = None
        self._order_no = None
        self._order_status = None
        self._paytool_list = None

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
    @property
    def order_status(self):
        return self._order_status

    @order_status.setter
    def order_status(self, value):
        self._order_status = value
    @property
    def paytool_list(self):
        return self._paytool_list

    @paytool_list.setter
    def paytool_list(self, value):
        if isinstance(value, list):
            self._paytool_list = list()
            for i in value:
                if isinstance(i, PaytoolResultDetail):
                    self._paytool_list.append(i)
                else:
                    self._paytool_list.append(PaytoolResultDetail.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayBusinessOrderPayResponse, self).parse_response_content(response_content)
        if 'merchant_order_no' in response:
            self.merchant_order_no = response['merchant_order_no']
        if 'order_no' in response:
            self.order_no = response['order_no']
        if 'order_status' in response:
            self.order_status = response['order_status']
        if 'paytool_list' in response:
            self.paytool_list = response['paytool_list']
