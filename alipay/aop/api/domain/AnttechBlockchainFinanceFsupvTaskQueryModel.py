#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AnttechBlockchainFinanceFsupvTaskQueryModel(object):

    def __init__(self):
        self._fund_supv_product_code = None
        self._supervised_id_number = None
        self._supervisor_id_number = None

    @property
    def fund_supv_product_code(self):
        return self._fund_supv_product_code

    @fund_supv_product_code.setter
    def fund_supv_product_code(self, value):
        self._fund_supv_product_code = value
    @property
    def supervised_id_number(self):
        return self._supervised_id_number

    @supervised_id_number.setter
    def supervised_id_number(self, value):
        self._supervised_id_number = value
    @property
    def supervisor_id_number(self):
        return self._supervisor_id_number

    @supervisor_id_number.setter
    def supervisor_id_number(self, value):
        self._supervisor_id_number = value


    def to_alipay_dict(self):
        params = dict()
        if self.fund_supv_product_code:
            if hasattr(self.fund_supv_product_code, 'to_alipay_dict'):
                params['fund_supv_product_code'] = self.fund_supv_product_code.to_alipay_dict()
            else:
                params['fund_supv_product_code'] = self.fund_supv_product_code
        if self.supervised_id_number:
            if hasattr(self.supervised_id_number, 'to_alipay_dict'):
                params['supervised_id_number'] = self.supervised_id_number.to_alipay_dict()
            else:
                params['supervised_id_number'] = self.supervised_id_number
        if self.supervisor_id_number:
            if hasattr(self.supervisor_id_number, 'to_alipay_dict'):
                params['supervisor_id_number'] = self.supervisor_id_number.to_alipay_dict()
            else:
                params['supervisor_id_number'] = self.supervisor_id_number
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AnttechBlockchainFinanceFsupvTaskQueryModel()
        if 'fund_supv_product_code' in d:
            o.fund_supv_product_code = d['fund_supv_product_code']
        if 'supervised_id_number' in d:
            o.supervised_id_number = d['supervised_id_number']
        if 'supervisor_id_number' in d:
            o.supervisor_id_number = d['supervisor_id_number']
        return o


