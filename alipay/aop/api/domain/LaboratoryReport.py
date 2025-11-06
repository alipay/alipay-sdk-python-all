#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.LaboratoryResultInfo import LaboratoryResultInfo


class LaboratoryReport(object):

    def __init__(self):
        self._result_info_list = None

    @property
    def result_info_list(self):
        return self._result_info_list

    @result_info_list.setter
    def result_info_list(self, value):
        if isinstance(value, list):
            self._result_info_list = list()
            for i in value:
                if isinstance(i, LaboratoryResultInfo):
                    self._result_info_list.append(i)
                else:
                    self._result_info_list.append(LaboratoryResultInfo.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.result_info_list:
            if isinstance(self.result_info_list, list):
                for i in range(0, len(self.result_info_list)):
                    element = self.result_info_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.result_info_list[i] = element.to_alipay_dict()
            if hasattr(self.result_info_list, 'to_alipay_dict'):
                params['result_info_list'] = self.result_info_list.to_alipay_dict()
            else:
                params['result_info_list'] = self.result_info_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = LaboratoryReport()
        if 'result_info_list' in d:
            o.result_info_list = d['result_info_list']
        return o


