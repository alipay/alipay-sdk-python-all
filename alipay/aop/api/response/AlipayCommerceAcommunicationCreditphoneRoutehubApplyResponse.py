#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.SignApplyResult import SignApplyResult


class AlipayCommerceAcommunicationCreditphoneRoutehubApplyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceAcommunicationCreditphoneRoutehubApplyResponse, self).__init__()
        self._operation_type = None
        self._order_no = None
        self._sign_apply_result = None

    @property
    def operation_type(self):
        return self._operation_type

    @operation_type.setter
    def operation_type(self, value):
        self._operation_type = value
    @property
    def order_no(self):
        return self._order_no

    @order_no.setter
    def order_no(self, value):
        self._order_no = value
    @property
    def sign_apply_result(self):
        return self._sign_apply_result

    @sign_apply_result.setter
    def sign_apply_result(self, value):
        if isinstance(value, SignApplyResult):
            self._sign_apply_result = value
        else:
            self._sign_apply_result = SignApplyResult.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceAcommunicationCreditphoneRoutehubApplyResponse, self).parse_response_content(response_content)
        if 'operation_type' in response:
            self.operation_type = response['operation_type']
        if 'order_no' in response:
            self.order_no = response['order_no']
        if 'sign_apply_result' in response:
            self.sign_apply_result = response['sign_apply_result']
