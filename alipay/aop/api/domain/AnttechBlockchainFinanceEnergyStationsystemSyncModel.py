#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AnttechBlockchainFinanceEnergyStationsystemSyncModel(object):

    def __init__(self):
        self._data_list = None
        self._data_type = None
        self._product_agreement_code = None
        self._real_time = None
        self._report_time = None

    @property
    def data_list(self):
        return self._data_list

    @data_list.setter
    def data_list(self, value):
        self._data_list = value
    @property
    def data_type(self):
        return self._data_type

    @data_type.setter
    def data_type(self, value):
        self._data_type = value
    @property
    def product_agreement_code(self):
        return self._product_agreement_code

    @product_agreement_code.setter
    def product_agreement_code(self, value):
        self._product_agreement_code = value
    @property
    def real_time(self):
        return self._real_time

    @real_time.setter
    def real_time(self, value):
        self._real_time = value
    @property
    def report_time(self):
        return self._report_time

    @report_time.setter
    def report_time(self, value):
        self._report_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.data_list:
            if hasattr(self.data_list, 'to_alipay_dict'):
                params['data_list'] = self.data_list.to_alipay_dict()
            else:
                params['data_list'] = self.data_list
        if self.data_type:
            if hasattr(self.data_type, 'to_alipay_dict'):
                params['data_type'] = self.data_type.to_alipay_dict()
            else:
                params['data_type'] = self.data_type
        if self.product_agreement_code:
            if hasattr(self.product_agreement_code, 'to_alipay_dict'):
                params['product_agreement_code'] = self.product_agreement_code.to_alipay_dict()
            else:
                params['product_agreement_code'] = self.product_agreement_code
        if self.real_time:
            if hasattr(self.real_time, 'to_alipay_dict'):
                params['real_time'] = self.real_time.to_alipay_dict()
            else:
                params['real_time'] = self.real_time
        if self.report_time:
            if hasattr(self.report_time, 'to_alipay_dict'):
                params['report_time'] = self.report_time.to_alipay_dict()
            else:
                params['report_time'] = self.report_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AnttechBlockchainFinanceEnergyStationsystemSyncModel()
        if 'data_list' in d:
            o.data_list = d['data_list']
        if 'data_type' in d:
            o.data_type = d['data_type']
        if 'product_agreement_code' in d:
            o.product_agreement_code = d['product_agreement_code']
        if 'real_time' in d:
            o.real_time = d['real_time']
        if 'report_time' in d:
            o.report_time = d['report_time']
        return o


