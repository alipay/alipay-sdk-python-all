#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.SubRentRiskItem import SubRentRiskItem
from alipay.aop.api.domain.SubRentRiskItem import SubRentRiskItem
from alipay.aop.api.domain.SubRentRiskItem import SubRentRiskItem


class SubRentRiskResult(object):

    def __init__(self):
        self._base_performance_risk = None
        self._multi_rent_risk = None
        self._overdue_risk = None

    @property
    def base_performance_risk(self):
        return self._base_performance_risk

    @base_performance_risk.setter
    def base_performance_risk(self, value):
        if isinstance(value, SubRentRiskItem):
            self._base_performance_risk = value
        else:
            self._base_performance_risk = SubRentRiskItem.from_alipay_dict(value)
    @property
    def multi_rent_risk(self):
        return self._multi_rent_risk

    @multi_rent_risk.setter
    def multi_rent_risk(self, value):
        if isinstance(value, SubRentRiskItem):
            self._multi_rent_risk = value
        else:
            self._multi_rent_risk = SubRentRiskItem.from_alipay_dict(value)
    @property
    def overdue_risk(self):
        return self._overdue_risk

    @overdue_risk.setter
    def overdue_risk(self, value):
        if isinstance(value, SubRentRiskItem):
            self._overdue_risk = value
        else:
            self._overdue_risk = SubRentRiskItem.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.base_performance_risk:
            if hasattr(self.base_performance_risk, 'to_alipay_dict'):
                params['base_performance_risk'] = self.base_performance_risk.to_alipay_dict()
            else:
                params['base_performance_risk'] = self.base_performance_risk
        if self.multi_rent_risk:
            if hasattr(self.multi_rent_risk, 'to_alipay_dict'):
                params['multi_rent_risk'] = self.multi_rent_risk.to_alipay_dict()
            else:
                params['multi_rent_risk'] = self.multi_rent_risk
        if self.overdue_risk:
            if hasattr(self.overdue_risk, 'to_alipay_dict'):
                params['overdue_risk'] = self.overdue_risk.to_alipay_dict()
            else:
                params['overdue_risk'] = self.overdue_risk
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SubRentRiskResult()
        if 'base_performance_risk' in d:
            o.base_performance_risk = d['base_performance_risk']
        if 'multi_rent_risk' in d:
            o.multi_rent_risk = d['multi_rent_risk']
        if 'overdue_risk' in d:
            o.overdue_risk = d['overdue_risk']
        return o


