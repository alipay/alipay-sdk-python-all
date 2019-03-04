#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.LogisticsExternalCarrierInfo import LogisticsExternalCarrierInfo


class LogisticsExternalInfo(object):

    def __init__(self):
        self._carrier_info_list = None
        self._carrier_sub_count = None

    @property
    def carrier_info_list(self):
        return self._carrier_info_list

    @carrier_info_list.setter
    def carrier_info_list(self, value):
        if isinstance(value, list):
            self._carrier_info_list = list()
            for i in value:
                if isinstance(i, LogisticsExternalCarrierInfo):
                    self._carrier_info_list.append(i)
                else:
                    self._carrier_info_list.append(LogisticsExternalCarrierInfo.from_alipay_dict(i))
    @property
    def carrier_sub_count(self):
        return self._carrier_sub_count

    @carrier_sub_count.setter
    def carrier_sub_count(self, value):
        self._carrier_sub_count = value


    def to_alipay_dict(self):
        params = dict()
        if self.carrier_info_list:
            if isinstance(self.carrier_info_list, list):
                for i in range(0, len(self.carrier_info_list)):
                    element = self.carrier_info_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.carrier_info_list[i] = element.to_alipay_dict()
            if hasattr(self.carrier_info_list, 'to_alipay_dict'):
                params['carrier_info_list'] = self.carrier_info_list.to_alipay_dict()
            else:
                params['carrier_info_list'] = self.carrier_info_list
        if self.carrier_sub_count:
            if hasattr(self.carrier_sub_count, 'to_alipay_dict'):
                params['carrier_sub_count'] = self.carrier_sub_count.to_alipay_dict()
            else:
                params['carrier_sub_count'] = self.carrier_sub_count
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = LogisticsExternalInfo()
        if 'carrier_info_list' in d:
            o.carrier_info_list = d['carrier_info_list']
        if 'carrier_sub_count' in d:
            o.carrier_sub_count = d['carrier_sub_count']
        return o


