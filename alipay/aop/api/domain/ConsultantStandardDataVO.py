#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ReferenceDataItem import ReferenceDataItem
from alipay.aop.api.domain.ReferenceDataItem import ReferenceDataItem
from alipay.aop.api.domain.ReferenceDataItem import ReferenceDataItem


class ConsultantStandardDataVO(object):

    def __init__(self):
        self._percentile_data = None
        self._special_data = None
        self._thresholds = None

    @property
    def percentile_data(self):
        return self._percentile_data

    @percentile_data.setter
    def percentile_data(self, value):
        if isinstance(value, list):
            self._percentile_data = list()
            for i in value:
                if isinstance(i, ReferenceDataItem):
                    self._percentile_data.append(i)
                else:
                    self._percentile_data.append(ReferenceDataItem.from_alipay_dict(i))
    @property
    def special_data(self):
        return self._special_data

    @special_data.setter
    def special_data(self, value):
        if isinstance(value, list):
            self._special_data = list()
            for i in value:
                if isinstance(i, ReferenceDataItem):
                    self._special_data.append(i)
                else:
                    self._special_data.append(ReferenceDataItem.from_alipay_dict(i))
    @property
    def thresholds(self):
        return self._thresholds

    @thresholds.setter
    def thresholds(self, value):
        if isinstance(value, list):
            self._thresholds = list()
            for i in value:
                if isinstance(i, ReferenceDataItem):
                    self._thresholds.append(i)
                else:
                    self._thresholds.append(ReferenceDataItem.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.percentile_data:
            if isinstance(self.percentile_data, list):
                for i in range(0, len(self.percentile_data)):
                    element = self.percentile_data[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.percentile_data[i] = element.to_alipay_dict()
            if hasattr(self.percentile_data, 'to_alipay_dict'):
                params['percentile_data'] = self.percentile_data.to_alipay_dict()
            else:
                params['percentile_data'] = self.percentile_data
        if self.special_data:
            if isinstance(self.special_data, list):
                for i in range(0, len(self.special_data)):
                    element = self.special_data[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.special_data[i] = element.to_alipay_dict()
            if hasattr(self.special_data, 'to_alipay_dict'):
                params['special_data'] = self.special_data.to_alipay_dict()
            else:
                params['special_data'] = self.special_data
        if self.thresholds:
            if isinstance(self.thresholds, list):
                for i in range(0, len(self.thresholds)):
                    element = self.thresholds[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.thresholds[i] = element.to_alipay_dict()
            if hasattr(self.thresholds, 'to_alipay_dict'):
                params['thresholds'] = self.thresholds.to_alipay_dict()
            else:
                params['thresholds'] = self.thresholds
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ConsultantStandardDataVO()
        if 'percentile_data' in d:
            o.percentile_data = d['percentile_data']
        if 'special_data' in d:
            o.special_data = d['special_data']
        if 'thresholds' in d:
            o.thresholds = d['thresholds']
        return o


