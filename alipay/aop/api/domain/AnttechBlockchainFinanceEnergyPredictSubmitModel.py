#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.LoadInfoNode import LoadInfoNode


class AnttechBlockchainFinanceEnergyPredictSubmitModel(object):

    def __init__(self):
        self._data_type = None
        self._out_resource_id = None
        self._predict_date = None
        self._predict_load_list = None
        self._predict_timespan = None
        self._product_agreement_code = None

    @property
    def data_type(self):
        return self._data_type

    @data_type.setter
    def data_type(self, value):
        self._data_type = value
    @property
    def out_resource_id(self):
        return self._out_resource_id

    @out_resource_id.setter
    def out_resource_id(self, value):
        self._out_resource_id = value
    @property
    def predict_date(self):
        return self._predict_date

    @predict_date.setter
    def predict_date(self, value):
        self._predict_date = value
    @property
    def predict_load_list(self):
        return self._predict_load_list

    @predict_load_list.setter
    def predict_load_list(self, value):
        if isinstance(value, list):
            self._predict_load_list = list()
            for i in value:
                if isinstance(i, LoadInfoNode):
                    self._predict_load_list.append(i)
                else:
                    self._predict_load_list.append(LoadInfoNode.from_alipay_dict(i))
    @property
    def predict_timespan(self):
        return self._predict_timespan

    @predict_timespan.setter
    def predict_timespan(self, value):
        self._predict_timespan = value
    @property
    def product_agreement_code(self):
        return self._product_agreement_code

    @product_agreement_code.setter
    def product_agreement_code(self, value):
        self._product_agreement_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.data_type:
            if hasattr(self.data_type, 'to_alipay_dict'):
                params['data_type'] = self.data_type.to_alipay_dict()
            else:
                params['data_type'] = self.data_type
        if self.out_resource_id:
            if hasattr(self.out_resource_id, 'to_alipay_dict'):
                params['out_resource_id'] = self.out_resource_id.to_alipay_dict()
            else:
                params['out_resource_id'] = self.out_resource_id
        if self.predict_date:
            if hasattr(self.predict_date, 'to_alipay_dict'):
                params['predict_date'] = self.predict_date.to_alipay_dict()
            else:
                params['predict_date'] = self.predict_date
        if self.predict_load_list:
            if isinstance(self.predict_load_list, list):
                for i in range(0, len(self.predict_load_list)):
                    element = self.predict_load_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.predict_load_list[i] = element.to_alipay_dict()
            if hasattr(self.predict_load_list, 'to_alipay_dict'):
                params['predict_load_list'] = self.predict_load_list.to_alipay_dict()
            else:
                params['predict_load_list'] = self.predict_load_list
        if self.predict_timespan:
            if hasattr(self.predict_timespan, 'to_alipay_dict'):
                params['predict_timespan'] = self.predict_timespan.to_alipay_dict()
            else:
                params['predict_timespan'] = self.predict_timespan
        if self.product_agreement_code:
            if hasattr(self.product_agreement_code, 'to_alipay_dict'):
                params['product_agreement_code'] = self.product_agreement_code.to_alipay_dict()
            else:
                params['product_agreement_code'] = self.product_agreement_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AnttechBlockchainFinanceEnergyPredictSubmitModel()
        if 'data_type' in d:
            o.data_type = d['data_type']
        if 'out_resource_id' in d:
            o.out_resource_id = d['out_resource_id']
        if 'predict_date' in d:
            o.predict_date = d['predict_date']
        if 'predict_load_list' in d:
            o.predict_load_list = d['predict_load_list']
        if 'predict_timespan' in d:
            o.predict_timespan = d['predict_timespan']
        if 'product_agreement_code' in d:
            o.product_agreement_code = d['product_agreement_code']
        return o


