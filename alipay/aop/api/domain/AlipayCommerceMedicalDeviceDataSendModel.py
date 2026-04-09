#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.DetailVO import DetailVO
from alipay.aop.api.domain.StatisticVO import StatisticVO


class AlipayCommerceMedicalDeviceDataSendModel(object):

    def __init__(self):
        self._details = None
        self._device_id = None
        self._device_vendor = None
        self._out_id = None
        self._statistics = None

    @property
    def details(self):
        return self._details

    @details.setter
    def details(self, value):
        if isinstance(value, list):
            self._details = list()
            for i in value:
                if isinstance(i, DetailVO):
                    self._details.append(i)
                else:
                    self._details.append(DetailVO.from_alipay_dict(i))
    @property
    def device_id(self):
        return self._device_id

    @device_id.setter
    def device_id(self, value):
        self._device_id = value
    @property
    def device_vendor(self):
        return self._device_vendor

    @device_vendor.setter
    def device_vendor(self, value):
        self._device_vendor = value
    @property
    def out_id(self):
        return self._out_id

    @out_id.setter
    def out_id(self, value):
        self._out_id = value
    @property
    def statistics(self):
        return self._statistics

    @statistics.setter
    def statistics(self, value):
        if isinstance(value, list):
            self._statistics = list()
            for i in value:
                if isinstance(i, StatisticVO):
                    self._statistics.append(i)
                else:
                    self._statistics.append(StatisticVO.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.details:
            if isinstance(self.details, list):
                for i in range(0, len(self.details)):
                    element = self.details[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.details[i] = element.to_alipay_dict()
            if hasattr(self.details, 'to_alipay_dict'):
                params['details'] = self.details.to_alipay_dict()
            else:
                params['details'] = self.details
        if self.device_id:
            if hasattr(self.device_id, 'to_alipay_dict'):
                params['device_id'] = self.device_id.to_alipay_dict()
            else:
                params['device_id'] = self.device_id
        if self.device_vendor:
            if hasattr(self.device_vendor, 'to_alipay_dict'):
                params['device_vendor'] = self.device_vendor.to_alipay_dict()
            else:
                params['device_vendor'] = self.device_vendor
        if self.out_id:
            if hasattr(self.out_id, 'to_alipay_dict'):
                params['out_id'] = self.out_id.to_alipay_dict()
            else:
                params['out_id'] = self.out_id
        if self.statistics:
            if isinstance(self.statistics, list):
                for i in range(0, len(self.statistics)):
                    element = self.statistics[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.statistics[i] = element.to_alipay_dict()
            if hasattr(self.statistics, 'to_alipay_dict'):
                params['statistics'] = self.statistics.to_alipay_dict()
            else:
                params['statistics'] = self.statistics
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMedicalDeviceDataSendModel()
        if 'details' in d:
            o.details = d['details']
        if 'device_id' in d:
            o.device_id = d['device_id']
        if 'device_vendor' in d:
            o.device_vendor = d['device_vendor']
        if 'out_id' in d:
            o.out_id = d['out_id']
        if 'statistics' in d:
            o.statistics = d['statistics']
        return o


