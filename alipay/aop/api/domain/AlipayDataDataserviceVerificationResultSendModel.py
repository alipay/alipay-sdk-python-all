#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.DxVerifyResultItem import DxVerifyResultItem


class AlipayDataDataserviceVerificationResultSendModel(object):

    def __init__(self):
        self._record_id = None
        self._result_items = None

    @property
    def record_id(self):
        return self._record_id

    @record_id.setter
    def record_id(self, value):
        self._record_id = value
    @property
    def result_items(self):
        return self._result_items

    @result_items.setter
    def result_items(self, value):
        if isinstance(value, list):
            self._result_items = list()
            for i in value:
                if isinstance(i, DxVerifyResultItem):
                    self._result_items.append(i)
                else:
                    self._result_items.append(DxVerifyResultItem.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.record_id:
            if hasattr(self.record_id, 'to_alipay_dict'):
                params['record_id'] = self.record_id.to_alipay_dict()
            else:
                params['record_id'] = self.record_id
        if self.result_items:
            if isinstance(self.result_items, list):
                for i in range(0, len(self.result_items)):
                    element = self.result_items[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.result_items[i] = element.to_alipay_dict()
            if hasattr(self.result_items, 'to_alipay_dict'):
                params['result_items'] = self.result_items.to_alipay_dict()
            else:
                params['result_items'] = self.result_items
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayDataDataserviceVerificationResultSendModel()
        if 'record_id' in d:
            o.record_id = d['record_id']
        if 'result_items' in d:
            o.result_items = d['result_items']
        return o


