#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.StockVerifyRecord import StockVerifyRecord


class AntfortuneStockVerifyReportSyncModel(object):

    def __init__(self):
        self._record_list = None
        self._rule_id = None

    @property
    def record_list(self):
        return self._record_list

    @record_list.setter
    def record_list(self, value):
        if isinstance(value, list):
            self._record_list = list()
            for i in value:
                if isinstance(i, StockVerifyRecord):
                    self._record_list.append(i)
                else:
                    self._record_list.append(StockVerifyRecord.from_alipay_dict(i))
    @property
    def rule_id(self):
        return self._rule_id

    @rule_id.setter
    def rule_id(self, value):
        self._rule_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.record_list:
            if isinstance(self.record_list, list):
                for i in range(0, len(self.record_list)):
                    element = self.record_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.record_list[i] = element.to_alipay_dict()
            if hasattr(self.record_list, 'to_alipay_dict'):
                params['record_list'] = self.record_list.to_alipay_dict()
            else:
                params['record_list'] = self.record_list
        if self.rule_id:
            if hasattr(self.rule_id, 'to_alipay_dict'):
                params['rule_id'] = self.rule_id.to_alipay_dict()
            else:
                params['rule_id'] = self.rule_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AntfortuneStockVerifyReportSyncModel()
        if 'record_list' in d:
            o.record_list = d['record_list']
        if 'rule_id' in d:
            o.rule_id = d['rule_id']
        return o


