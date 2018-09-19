#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AntMerchantExpandIndirectZftConsultResponse(AlipayResponse):

    def __init__(self):
        super(AntMerchantExpandIndirectZftConsultResponse, self).__init__()
        self._account_audit = None
        self._order_id = None
        self._risk_audit = None

    @property
    def account_audit(self):
        return self._account_audit

    @account_audit.setter
    def account_audit(self, value):
        self._account_audit = value
    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        self._order_id = value
    @property
    def risk_audit(self):
        return self._risk_audit

    @risk_audit.setter
    def risk_audit(self, value):
        self._risk_audit = value

    def parse_response_content(self, response_content):
        response = super(AntMerchantExpandIndirectZftConsultResponse, self).parse_response_content(response_content)
        if 'account_audit' in response:
            self.account_audit = response['account_audit']
        if 'order_id' in response:
            self.order_id = response['order_id']
        if 'risk_audit' in response:
            self.risk_audit = response['risk_audit']
