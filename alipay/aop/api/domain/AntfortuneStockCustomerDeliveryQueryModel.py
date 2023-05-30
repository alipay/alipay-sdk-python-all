#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AntfortuneStockCustomerDeliveryQueryModel(object):

    def __init__(self):
        self._agreement_no = None
        self._position_code = None

    @property
    def agreement_no(self):
        return self._agreement_no

    @agreement_no.setter
    def agreement_no(self, value):
        self._agreement_no = value
    @property
    def position_code(self):
        return self._position_code

    @position_code.setter
    def position_code(self, value):
        if isinstance(value, list):
            self._position_code = list()
            for i in value:
                self._position_code.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.agreement_no:
            if hasattr(self.agreement_no, 'to_alipay_dict'):
                params['agreement_no'] = self.agreement_no.to_alipay_dict()
            else:
                params['agreement_no'] = self.agreement_no
        if self.position_code:
            if isinstance(self.position_code, list):
                for i in range(0, len(self.position_code)):
                    element = self.position_code[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.position_code[i] = element.to_alipay_dict()
            if hasattr(self.position_code, 'to_alipay_dict'):
                params['position_code'] = self.position_code.to_alipay_dict()
            else:
                params['position_code'] = self.position_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AntfortuneStockCustomerDeliveryQueryModel()
        if 'agreement_no' in d:
            o.agreement_no = d['agreement_no']
        if 'position_code' in d:
            o.position_code = d['position_code']
        return o


