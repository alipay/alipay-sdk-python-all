#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.IotQueryDeviceInfo import IotQueryDeviceInfo


class AlipayMarketingShowwindowContentQueryModel(object):

    def __init__(self):
        self._device_info_list = None
        self._query_date = None
        self._source = None

    @property
    def device_info_list(self):
        return self._device_info_list

    @device_info_list.setter
    def device_info_list(self, value):
        if isinstance(value, list):
            self._device_info_list = list()
            for i in value:
                if isinstance(i, IotQueryDeviceInfo):
                    self._device_info_list.append(i)
                else:
                    self._device_info_list.append(IotQueryDeviceInfo.from_alipay_dict(i))
    @property
    def query_date(self):
        return self._query_date

    @query_date.setter
    def query_date(self, value):
        self._query_date = value
    @property
    def source(self):
        return self._source

    @source.setter
    def source(self, value):
        self._source = value


    def to_alipay_dict(self):
        params = dict()
        if self.device_info_list:
            if isinstance(self.device_info_list, list):
                for i in range(0, len(self.device_info_list)):
                    element = self.device_info_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.device_info_list[i] = element.to_alipay_dict()
            if hasattr(self.device_info_list, 'to_alipay_dict'):
                params['device_info_list'] = self.device_info_list.to_alipay_dict()
            else:
                params['device_info_list'] = self.device_info_list
        if self.query_date:
            if hasattr(self.query_date, 'to_alipay_dict'):
                params['query_date'] = self.query_date.to_alipay_dict()
            else:
                params['query_date'] = self.query_date
        if self.source:
            if hasattr(self.source, 'to_alipay_dict'):
                params['source'] = self.source.to_alipay_dict()
            else:
                params['source'] = self.source
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayMarketingShowwindowContentQueryModel()
        if 'device_info_list' in d:
            o.device_info_list = d['device_info_list']
        if 'query_date' in d:
            o.query_date = d['query_date']
        if 'source' in d:
            o.source = d['source']
        return o


