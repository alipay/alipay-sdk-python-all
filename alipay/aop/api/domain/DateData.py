#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.IndicatorData import IndicatorData


class DateData(object):

    def __init__(self):
        self._date = None
        self._indicator_data_list = None

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, value):
        self._date = value
    @property
    def indicator_data_list(self):
        return self._indicator_data_list

    @indicator_data_list.setter
    def indicator_data_list(self, value):
        if isinstance(value, list):
            self._indicator_data_list = list()
            for i in value:
                if isinstance(i, IndicatorData):
                    self._indicator_data_list.append(i)
                else:
                    self._indicator_data_list.append(IndicatorData.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.date:
            if hasattr(self.date, 'to_alipay_dict'):
                params['date'] = self.date.to_alipay_dict()
            else:
                params['date'] = self.date
        if self.indicator_data_list:
            if isinstance(self.indicator_data_list, list):
                for i in range(0, len(self.indicator_data_list)):
                    element = self.indicator_data_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.indicator_data_list[i] = element.to_alipay_dict()
            if hasattr(self.indicator_data_list, 'to_alipay_dict'):
                params['indicator_data_list'] = self.indicator_data_list.to_alipay_dict()
            else:
                params['indicator_data_list'] = self.indicator_data_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DateData()
        if 'date' in d:
            o.date = d['date']
        if 'indicator_data_list' in d:
            o.indicator_data_list = d['indicator_data_list']
        return o


