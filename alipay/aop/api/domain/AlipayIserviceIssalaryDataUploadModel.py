#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.SalaryDataDetail import SalaryDataDetail


class AlipayIserviceIssalaryDataUploadModel(object):

    def __init__(self):
        self._data_day = None
        self._salary_data = None

    @property
    def data_day(self):
        return self._data_day

    @data_day.setter
    def data_day(self, value):
        self._data_day = value
    @property
    def salary_data(self):
        return self._salary_data

    @salary_data.setter
    def salary_data(self, value):
        if isinstance(value, list):
            self._salary_data = list()
            for i in value:
                if isinstance(i, SalaryDataDetail):
                    self._salary_data.append(i)
                else:
                    self._salary_data.append(SalaryDataDetail.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.data_day:
            if hasattr(self.data_day, 'to_alipay_dict'):
                params['data_day'] = self.data_day.to_alipay_dict()
            else:
                params['data_day'] = self.data_day
        if self.salary_data:
            if isinstance(self.salary_data, list):
                for i in range(0, len(self.salary_data)):
                    element = self.salary_data[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.salary_data[i] = element.to_alipay_dict()
            if hasattr(self.salary_data, 'to_alipay_dict'):
                params['salary_data'] = self.salary_data.to_alipay_dict()
            else:
                params['salary_data'] = self.salary_data
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayIserviceIssalaryDataUploadModel()
        if 'data_day' in d:
            o.data_day = d['data_day']
        if 'salary_data' in d:
            o.salary_data = d['salary_data']
        return o


