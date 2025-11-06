#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ReportResultInfo import ReportResultInfo


class HealthLaboratoryReport(object):

    def __init__(self):
        self._item_name = None
        self._result_info_list = None

    @property
    def item_name(self):
        return self._item_name

    @item_name.setter
    def item_name(self, value):
        self._item_name = value
    @property
    def result_info_list(self):
        return self._result_info_list

    @result_info_list.setter
    def result_info_list(self, value):
        if isinstance(value, list):
            self._result_info_list = list()
            for i in value:
                if isinstance(i, ReportResultInfo):
                    self._result_info_list.append(i)
                else:
                    self._result_info_list.append(ReportResultInfo.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.item_name:
            if hasattr(self.item_name, 'to_alipay_dict'):
                params['item_name'] = self.item_name.to_alipay_dict()
            else:
                params['item_name'] = self.item_name
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
        o = HealthLaboratoryReport()
        if 'item_name' in d:
            o.item_name = d['item_name']
        if 'result_info_list' in d:
            o.result_info_list = d['result_info_list']
        return o


