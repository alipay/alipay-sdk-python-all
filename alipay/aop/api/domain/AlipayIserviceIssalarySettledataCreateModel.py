#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.SettleDataDetail import SettleDataDetail


class AlipayIserviceIssalarySettledataCreateModel(object):

    def __init__(self):
        self._data_date = None
        self._settle_data = None

    @property
    def data_date(self):
        return self._data_date

    @data_date.setter
    def data_date(self, value):
        self._data_date = value
    @property
    def settle_data(self):
        return self._settle_data

    @settle_data.setter
    def settle_data(self, value):
        if isinstance(value, list):
            self._settle_data = list()
            for i in value:
                if isinstance(i, SettleDataDetail):
                    self._settle_data.append(i)
                else:
                    self._settle_data.append(SettleDataDetail.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.data_date:
            if hasattr(self.data_date, 'to_alipay_dict'):
                params['data_date'] = self.data_date.to_alipay_dict()
            else:
                params['data_date'] = self.data_date
        if self.settle_data:
            if isinstance(self.settle_data, list):
                for i in range(0, len(self.settle_data)):
                    element = self.settle_data[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.settle_data[i] = element.to_alipay_dict()
            if hasattr(self.settle_data, 'to_alipay_dict'):
                params['settle_data'] = self.settle_data.to_alipay_dict()
            else:
                params['settle_data'] = self.settle_data
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayIserviceIssalarySettledataCreateModel()
        if 'data_date' in d:
            o.data_date = d['data_date']
        if 'settle_data' in d:
            o.settle_data = d['settle_data']
        return o


