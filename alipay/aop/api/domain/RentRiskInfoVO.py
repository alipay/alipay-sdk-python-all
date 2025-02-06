#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.RiskItemVO import RiskItemVO


class RentRiskInfoVO(object):

    def __init__(self):
        self._risk_item_list = None
        self._risk_type = None

    @property
    def risk_item_list(self):
        return self._risk_item_list

    @risk_item_list.setter
    def risk_item_list(self, value):
        if isinstance(value, list):
            self._risk_item_list = list()
            for i in value:
                if isinstance(i, RiskItemVO):
                    self._risk_item_list.append(i)
                else:
                    self._risk_item_list.append(RiskItemVO.from_alipay_dict(i))
    @property
    def risk_type(self):
        return self._risk_type

    @risk_type.setter
    def risk_type(self, value):
        self._risk_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.risk_item_list:
            if isinstance(self.risk_item_list, list):
                for i in range(0, len(self.risk_item_list)):
                    element = self.risk_item_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.risk_item_list[i] = element.to_alipay_dict()
            if hasattr(self.risk_item_list, 'to_alipay_dict'):
                params['risk_item_list'] = self.risk_item_list.to_alipay_dict()
            else:
                params['risk_item_list'] = self.risk_item_list
        if self.risk_type:
            if hasattr(self.risk_type, 'to_alipay_dict'):
                params['risk_type'] = self.risk_type.to_alipay_dict()
            else:
                params['risk_type'] = self.risk_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RentRiskInfoVO()
        if 'risk_item_list' in d:
            o.risk_item_list = d['risk_item_list']
        if 'risk_type' in d:
            o.risk_type = d['risk_type']
        return o


