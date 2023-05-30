#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.DtBankRandomRangeInfo import DtBankRandomRangeInfo


class DtBankPreferenceRandomRule(object):

    def __init__(self):
        self._range_info_list = None

    @property
    def range_info_list(self):
        return self._range_info_list

    @range_info_list.setter
    def range_info_list(self, value):
        if isinstance(value, list):
            self._range_info_list = list()
            for i in value:
                if isinstance(i, DtBankRandomRangeInfo):
                    self._range_info_list.append(i)
                else:
                    self._range_info_list.append(DtBankRandomRangeInfo.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.range_info_list:
            if isinstance(self.range_info_list, list):
                for i in range(0, len(self.range_info_list)):
                    element = self.range_info_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.range_info_list[i] = element.to_alipay_dict()
            if hasattr(self.range_info_list, 'to_alipay_dict'):
                params['range_info_list'] = self.range_info_list.to_alipay_dict()
            else:
                params['range_info_list'] = self.range_info_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DtBankPreferenceRandomRule()
        if 'range_info_list' in d:
            o.range_info_list = d['range_info_list']
        return o


