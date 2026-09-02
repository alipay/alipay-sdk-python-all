#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.EtcTollFeeTopThreeDTO import EtcTollFeeTopThreeDTO


class EtcTollFeeTollStatsDTO(object):

    def __init__(self):
        self._avg = None
        self._max = None
        self._median = None
        self._min = None
        self._top_three = None
        self._trip_fee = None

    @property
    def avg(self):
        return self._avg

    @avg.setter
    def avg(self, value):
        self._avg = value
    @property
    def max(self):
        return self._max

    @max.setter
    def max(self, value):
        self._max = value
    @property
    def median(self):
        return self._median

    @median.setter
    def median(self, value):
        self._median = value
    @property
    def min(self):
        return self._min

    @min.setter
    def min(self, value):
        self._min = value
    @property
    def top_three(self):
        return self._top_three

    @top_three.setter
    def top_three(self, value):
        if isinstance(value, list):
            self._top_three = list()
            for i in value:
                if isinstance(i, EtcTollFeeTopThreeDTO):
                    self._top_three.append(i)
                else:
                    self._top_three.append(EtcTollFeeTopThreeDTO.from_alipay_dict(i))
    @property
    def trip_fee(self):
        return self._trip_fee

    @trip_fee.setter
    def trip_fee(self, value):
        self._trip_fee = value


    def to_alipay_dict(self):
        params = dict()
        if self.avg:
            if hasattr(self.avg, 'to_alipay_dict'):
                params['avg'] = self.avg.to_alipay_dict()
            else:
                params['avg'] = self.avg
        if self.max:
            if hasattr(self.max, 'to_alipay_dict'):
                params['max'] = self.max.to_alipay_dict()
            else:
                params['max'] = self.max
        if self.median:
            if hasattr(self.median, 'to_alipay_dict'):
                params['median'] = self.median.to_alipay_dict()
            else:
                params['median'] = self.median
        if self.min:
            if hasattr(self.min, 'to_alipay_dict'):
                params['min'] = self.min.to_alipay_dict()
            else:
                params['min'] = self.min
        if self.top_three:
            if isinstance(self.top_three, list):
                for i in range(0, len(self.top_three)):
                    element = self.top_three[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.top_three[i] = element.to_alipay_dict()
            if hasattr(self.top_three, 'to_alipay_dict'):
                params['top_three'] = self.top_three.to_alipay_dict()
            else:
                params['top_three'] = self.top_three
        if self.trip_fee:
            if hasattr(self.trip_fee, 'to_alipay_dict'):
                params['trip_fee'] = self.trip_fee.to_alipay_dict()
            else:
                params['trip_fee'] = self.trip_fee
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = EtcTollFeeTollStatsDTO()
        if 'avg' in d:
            o.avg = d['avg']
        if 'max' in d:
            o.max = d['max']
        if 'median' in d:
            o.median = d['median']
        if 'min' in d:
            o.min = d['min']
        if 'top_three' in d:
            o.top_three = d['top_three']
        if 'trip_fee' in d:
            o.trip_fee = d['trip_fee']
        return o


