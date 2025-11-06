#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ReconciliationMerchantInfo import ReconciliationMerchantInfo


class AlipayMerchantComplainReconciliationCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMerchantComplainReconciliationCreateResponse, self).__init__()
        self._merchant_credit_no = None
        self._merchant_infos = None

    @property
    def merchant_credit_no(self):
        return self._merchant_credit_no

    @merchant_credit_no.setter
    def merchant_credit_no(self, value):
        self._merchant_credit_no = value
    @property
    def merchant_infos(self):
        return self._merchant_infos

    @merchant_infos.setter
    def merchant_infos(self, value):
        if isinstance(value, list):
            self._merchant_infos = list()
            for i in value:
                if isinstance(i, ReconciliationMerchantInfo):
                    self._merchant_infos.append(i)
                else:
                    self._merchant_infos.append(ReconciliationMerchantInfo.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayMerchantComplainReconciliationCreateResponse, self).parse_response_content(response_content)
        if 'merchant_credit_no' in response:
            self.merchant_credit_no = response['merchant_credit_no']
        if 'merchant_infos' in response:
            self.merchant_infos = response['merchant_infos']
