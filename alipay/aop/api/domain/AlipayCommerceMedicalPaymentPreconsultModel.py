#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceMedicalPaymentPreconsultModel(object):

    def __init__(self):
        self._drug_store_tag = None
        self._payment_city_code = None

    @property
    def drug_store_tag(self):
        return self._drug_store_tag

    @drug_store_tag.setter
    def drug_store_tag(self, value):
        self._drug_store_tag = value
    @property
    def payment_city_code(self):
        return self._payment_city_code

    @payment_city_code.setter
    def payment_city_code(self, value):
        self._payment_city_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.drug_store_tag:
            if hasattr(self.drug_store_tag, 'to_alipay_dict'):
                params['drug_store_tag'] = self.drug_store_tag.to_alipay_dict()
            else:
                params['drug_store_tag'] = self.drug_store_tag
        if self.payment_city_code:
            if hasattr(self.payment_city_code, 'to_alipay_dict'):
                params['payment_city_code'] = self.payment_city_code.to_alipay_dict()
            else:
                params['payment_city_code'] = self.payment_city_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMedicalPaymentPreconsultModel()
        if 'drug_store_tag' in d:
            o.drug_store_tag = d['drug_store_tag']
        if 'payment_city_code' in d:
            o.payment_city_code = d['payment_city_code']
        return o


