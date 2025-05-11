#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenAuthIsvQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenAuthIsvQueryResponse, self).__init__()
        self._alipay_account = None
        self._merchant_app_id = None
        self._merchant_app_name = None
        self._merchant_name = None

    @property
    def alipay_account(self):
        return self._alipay_account

    @alipay_account.setter
    def alipay_account(self, value):
        self._alipay_account = value
    @property
    def merchant_app_id(self):
        return self._merchant_app_id

    @merchant_app_id.setter
    def merchant_app_id(self, value):
        self._merchant_app_id = value
    @property
    def merchant_app_name(self):
        return self._merchant_app_name

    @merchant_app_name.setter
    def merchant_app_name(self, value):
        self._merchant_app_name = value
    @property
    def merchant_name(self):
        return self._merchant_name

    @merchant_name.setter
    def merchant_name(self, value):
        self._merchant_name = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenAuthIsvQueryResponse, self).parse_response_content(response_content)
        if 'alipay_account' in response:
            self.alipay_account = response['alipay_account']
        if 'merchant_app_id' in response:
            self.merchant_app_id = response['merchant_app_id']
        if 'merchant_app_name' in response:
            self.merchant_app_name = response['merchant_app_name']
        if 'merchant_name' in response:
            self.merchant_name = response['merchant_name']
