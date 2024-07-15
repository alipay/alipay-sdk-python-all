#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.AlipaySolutionRecord import AlipaySolutionRecord


class AlipayMerchantSolutionRecordQueryModel(object):

    def __init__(self):
        self._record_data = None
        self._solution_code = None

    @property
    def record_data(self):
        return self._record_data

    @record_data.setter
    def record_data(self, value):
        if isinstance(value, list):
            self._record_data = list()
            for i in value:
                if isinstance(i, AlipaySolutionRecord):
                    self._record_data.append(i)
                else:
                    self._record_data.append(AlipaySolutionRecord.from_alipay_dict(i))
    @property
    def solution_code(self):
        return self._solution_code

    @solution_code.setter
    def solution_code(self, value):
        self._solution_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.record_data:
            if isinstance(self.record_data, list):
                for i in range(0, len(self.record_data)):
                    element = self.record_data[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.record_data[i] = element.to_alipay_dict()
            if hasattr(self.record_data, 'to_alipay_dict'):
                params['record_data'] = self.record_data.to_alipay_dict()
            else:
                params['record_data'] = self.record_data
        if self.solution_code:
            if hasattr(self.solution_code, 'to_alipay_dict'):
                params['solution_code'] = self.solution_code.to_alipay_dict()
            else:
                params['solution_code'] = self.solution_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayMerchantSolutionRecordQueryModel()
        if 'record_data' in d:
            o.record_data = d['record_data']
        if 'solution_code' in d:
            o.solution_code = d['solution_code']
        return o


