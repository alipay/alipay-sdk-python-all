#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayMerchantComplainReconciliationSubmitResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMerchantComplainReconciliationSubmitResponse, self).__init__()
        self._merchant_credit_no = None
        self._merchant_id = None
        self._merchant_name = None
        self._merchant_type = None
        self._notice = None

    @property
    def merchant_credit_no(self):
        return self._merchant_credit_no

    @merchant_credit_no.setter
    def merchant_credit_no(self, value):
        self._merchant_credit_no = value
    @property
    def merchant_id(self):
        return self._merchant_id

    @merchant_id.setter
    def merchant_id(self, value):
        self._merchant_id = value
    @property
    def merchant_name(self):
        return self._merchant_name

    @merchant_name.setter
    def merchant_name(self, value):
        self._merchant_name = value
    @property
    def merchant_type(self):
        return self._merchant_type

    @merchant_type.setter
    def merchant_type(self, value):
        self._merchant_type = value
    @property
    def notice(self):
        return self._notice

    @notice.setter
    def notice(self, value):
        self._notice = value

    def parse_response_content(self, response_content):
        response = super(AlipayMerchantComplainReconciliationSubmitResponse, self).parse_response_content(response_content)
        if 'merchant_credit_no' in response:
            self.merchant_credit_no = response['merchant_credit_no']
        if 'merchant_id' in response:
            self.merchant_id = response['merchant_id']
        if 'merchant_name' in response:
            self.merchant_name = response['merchant_name']
        if 'merchant_type' in response:
            self.merchant_type = response['merchant_type']
        if 'notice' in response:
            self.notice = response['notice']
