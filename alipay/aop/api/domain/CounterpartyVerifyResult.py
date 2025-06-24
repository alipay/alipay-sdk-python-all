#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.CounterpartyInfo import CounterpartyInfo


class CounterpartyVerifyResult(object):

    def __init__(self):
        self._ent_list = None
        self._is_match_risk_list = None

    @property
    def ent_list(self):
        return self._ent_list

    @ent_list.setter
    def ent_list(self, value):
        if isinstance(value, list):
            self._ent_list = list()
            for i in value:
                if isinstance(i, CounterpartyInfo):
                    self._ent_list.append(i)
                else:
                    self._ent_list.append(CounterpartyInfo.from_alipay_dict(i))
    @property
    def is_match_risk_list(self):
        return self._is_match_risk_list

    @is_match_risk_list.setter
    def is_match_risk_list(self, value):
        self._is_match_risk_list = value


    def to_alipay_dict(self):
        params = dict()
        if self.ent_list:
            if isinstance(self.ent_list, list):
                for i in range(0, len(self.ent_list)):
                    element = self.ent_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.ent_list[i] = element.to_alipay_dict()
            if hasattr(self.ent_list, 'to_alipay_dict'):
                params['ent_list'] = self.ent_list.to_alipay_dict()
            else:
                params['ent_list'] = self.ent_list
        if self.is_match_risk_list:
            if hasattr(self.is_match_risk_list, 'to_alipay_dict'):
                params['is_match_risk_list'] = self.is_match_risk_list.to_alipay_dict()
            else:
                params['is_match_risk_list'] = self.is_match_risk_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CounterpartyVerifyResult()
        if 'ent_list' in d:
            o.ent_list = d['ent_list']
        if 'is_match_risk_list' in d:
            o.is_match_risk_list = d['is_match_risk_list']
        return o


