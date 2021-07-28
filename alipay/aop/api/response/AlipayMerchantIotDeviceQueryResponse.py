#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayMerchantIotDeviceQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMerchantIotDeviceQueryResponse, self).__init__()
        self._merchant_type = None
        self._pid = None
        self._shop_id = None
        self._smid = None

    @property
    def merchant_type(self):
        return self._merchant_type

    @merchant_type.setter
    def merchant_type(self, value):
        self._merchant_type = value
    @property
    def pid(self):
        return self._pid

    @pid.setter
    def pid(self, value):
        self._pid = value
    @property
    def shop_id(self):
        return self._shop_id

    @shop_id.setter
    def shop_id(self, value):
        self._shop_id = value
    @property
    def smid(self):
        return self._smid

    @smid.setter
    def smid(self, value):
        self._smid = value

    def parse_response_content(self, response_content):
        response = super(AlipayMerchantIotDeviceQueryResponse, self).parse_response_content(response_content)
        if 'merchant_type' in response:
            self.merchant_type = response['merchant_type']
        if 'pid' in response:
            self.pid = response['pid']
        if 'shop_id' in response:
            self.shop_id = response['shop_id']
        if 'smid' in response:
            self.smid = response['smid']
