#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MybankCreditLoanapplyTaxOpenSendModel(object):

    def __init__(self):
        self._business_type = None
        self._data_object = None

    @property
    def business_type(self):
        return self._business_type

    @business_type.setter
    def business_type(self, value):
        self._business_type = value
    @property
    def data_object(self):
        return self._data_object

    @data_object.setter
    def data_object(self, value):
        self._data_object = value


    def to_alipay_dict(self):
        params = dict()
        if self.business_type:
            if hasattr(self.business_type, 'to_alipay_dict'):
                params['business_type'] = self.business_type.to_alipay_dict()
            else:
                params['business_type'] = self.business_type
        if self.data_object:
            if hasattr(self.data_object, 'to_alipay_dict'):
                params['data_object'] = self.data_object.to_alipay_dict()
            else:
                params['data_object'] = self.data_object
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MybankCreditLoanapplyTaxOpenSendModel()
        if 'business_type' in d:
            o.business_type = d['business_type']
        if 'data_object' in d:
            o.data_object = d['data_object']
        return o


