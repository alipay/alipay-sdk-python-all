#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.FvPairList import FvPairList


class AlipayBossFncGfmdmRecordsBatchqueryModel(object):

    def __init__(self):
        self._conditions = None
        self._dicode = None

    @property
    def conditions(self):
        return self._conditions

    @conditions.setter
    def conditions(self, value):
        if isinstance(value, list):
            self._conditions = list()
            for i in value:
                if isinstance(i, FvPairList):
                    self._conditions.append(i)
                else:
                    self._conditions.append(FvPairList.from_alipay_dict(i))
    @property
    def dicode(self):
        return self._dicode

    @dicode.setter
    def dicode(self, value):
        self._dicode = value


    def to_alipay_dict(self):
        params = dict()
        if self.conditions:
            if isinstance(self.conditions, list):
                for i in range(0, len(self.conditions)):
                    element = self.conditions[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.conditions[i] = element.to_alipay_dict()
            if hasattr(self.conditions, 'to_alipay_dict'):
                params['conditions'] = self.conditions.to_alipay_dict()
            else:
                params['conditions'] = self.conditions
        if self.dicode:
            if hasattr(self.dicode, 'to_alipay_dict'):
                params['dicode'] = self.dicode.to_alipay_dict()
            else:
                params['dicode'] = self.dicode
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayBossFncGfmdmRecordsBatchqueryModel()
        if 'conditions' in d:
            o.conditions = d['conditions']
        if 'dicode' in d:
            o.dicode = d['dicode']
        return o


