#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOfflineProviderSmidCoilpaydescriptionQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOfflineProviderSmidCoilpaydescriptionQueryResponse, self).__init__()
        self._merchant_coil_pay_description = None
        self._sub_merchant_id = None

    @property
    def merchant_coil_pay_description(self):
        return self._merchant_coil_pay_description

    @merchant_coil_pay_description.setter
    def merchant_coil_pay_description(self, value):
        self._merchant_coil_pay_description = value
    @property
    def sub_merchant_id(self):
        return self._sub_merchant_id

    @sub_merchant_id.setter
    def sub_merchant_id(self, value):
        self._sub_merchant_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayOfflineProviderSmidCoilpaydescriptionQueryResponse, self).parse_response_content(response_content)
        if 'merchant_coil_pay_description' in response:
            self.merchant_coil_pay_description = response['merchant_coil_pay_description']
        if 'sub_merchant_id' in response:
            self.sub_merchant_id = response['sub_merchant_id']
