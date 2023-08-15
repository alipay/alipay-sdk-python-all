#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ProductUsageInfo import ProductUsageInfo


class WorkspaceResourceUsage(object):

    def __init__(self):
        self._end_time = None
        self._product_usage_infos = None
        self._start_time = None

    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, value):
        self._end_time = value
    @property
    def product_usage_infos(self):
        return self._product_usage_infos

    @product_usage_infos.setter
    def product_usage_infos(self, value):
        if isinstance(value, list):
            self._product_usage_infos = list()
            for i in value:
                if isinstance(i, ProductUsageInfo):
                    self._product_usage_infos.append(i)
                else:
                    self._product_usage_infos.append(ProductUsageInfo.from_alipay_dict(i))
    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, value):
        self._start_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.end_time:
            if hasattr(self.end_time, 'to_alipay_dict'):
                params['end_time'] = self.end_time.to_alipay_dict()
            else:
                params['end_time'] = self.end_time
        if self.product_usage_infos:
            if isinstance(self.product_usage_infos, list):
                for i in range(0, len(self.product_usage_infos)):
                    element = self.product_usage_infos[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.product_usage_infos[i] = element.to_alipay_dict()
            if hasattr(self.product_usage_infos, 'to_alipay_dict'):
                params['product_usage_infos'] = self.product_usage_infos.to_alipay_dict()
            else:
                params['product_usage_infos'] = self.product_usage_infos
        if self.start_time:
            if hasattr(self.start_time, 'to_alipay_dict'):
                params['start_time'] = self.start_time.to_alipay_dict()
            else:
                params['start_time'] = self.start_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = WorkspaceResourceUsage()
        if 'end_time' in d:
            o.end_time = d['end_time']
        if 'product_usage_infos' in d:
            o.product_usage_infos = d['product_usage_infos']
        if 'start_time' in d:
            o.start_time = d['start_time']
        return o


