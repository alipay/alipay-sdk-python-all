#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.CreditpaySubquota import CreditpaySubquota


class MybankCreditSupplychainCreditpayAmountQueryResponse(AlipayResponse):

    def __init__(self):
        super(MybankCreditSupplychainCreditpayAmountQueryResponse, self).__init__()
        self._admit = None
        self._available_amt = None
        self._buyer_scene_id = None
        self._creditpay_sub_quotas = None
        self._signed = None
        self._total_amt = None
        self._trace_id = None

    @property
    def admit(self):
        return self._admit

    @admit.setter
    def admit(self, value):
        self._admit = value
    @property
    def available_amt(self):
        return self._available_amt

    @available_amt.setter
    def available_amt(self, value):
        self._available_amt = value
    @property
    def buyer_scene_id(self):
        return self._buyer_scene_id

    @buyer_scene_id.setter
    def buyer_scene_id(self, value):
        self._buyer_scene_id = value
    @property
    def creditpay_sub_quotas(self):
        return self._creditpay_sub_quotas

    @creditpay_sub_quotas.setter
    def creditpay_sub_quotas(self, value):
        if isinstance(value, list):
            self._creditpay_sub_quotas = list()
            for i in value:
                if isinstance(i, CreditpaySubquota):
                    self._creditpay_sub_quotas.append(i)
                else:
                    self._creditpay_sub_quotas.append(CreditpaySubquota.from_alipay_dict(i))
    @property
    def signed(self):
        return self._signed

    @signed.setter
    def signed(self, value):
        self._signed = value
    @property
    def total_amt(self):
        return self._total_amt

    @total_amt.setter
    def total_amt(self, value):
        self._total_amt = value
    @property
    def trace_id(self):
        return self._trace_id

    @trace_id.setter
    def trace_id(self, value):
        self._trace_id = value

    def parse_response_content(self, response_content):
        response = super(MybankCreditSupplychainCreditpayAmountQueryResponse, self).parse_response_content(response_content)
        if 'admit' in response:
            self.admit = response['admit']
        if 'available_amt' in response:
            self.available_amt = response['available_amt']
        if 'buyer_scene_id' in response:
            self.buyer_scene_id = response['buyer_scene_id']
        if 'creditpay_sub_quotas' in response:
            self.creditpay_sub_quotas = response['creditpay_sub_quotas']
        if 'signed' in response:
            self.signed = response['signed']
        if 'total_amt' in response:
            self.total_amt = response['total_amt']
        if 'trace_id' in response:
            self.trace_id = response['trace_id']
