#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.MBudgetInfo import MBudgetInfo
from alipay.aop.api.domain.MPromoConstraint import MPromoConstraint
from alipay.aop.api.domain.MEquityInfo import MEquityInfo
from alipay.aop.api.domain.MExtInfo import MExtInfo


class MPromoInfo(object):

    def __init__(self):
        self._budget = None
        self._constraint = None
        self._equity_info = None
        self._ext_info = None
        self._out_promo_id = None

    @property
    def budget(self):
        return self._budget

    @budget.setter
    def budget(self, value):
        if isinstance(value, MBudgetInfo):
            self._budget = value
        else:
            self._budget = MBudgetInfo.from_alipay_dict(value)
    @property
    def constraint(self):
        return self._constraint

    @constraint.setter
    def constraint(self, value):
        if isinstance(value, MPromoConstraint):
            self._constraint = value
        else:
            self._constraint = MPromoConstraint.from_alipay_dict(value)
    @property
    def equity_info(self):
        return self._equity_info

    @equity_info.setter
    def equity_info(self, value):
        if isinstance(value, MEquityInfo):
            self._equity_info = value
        else:
            self._equity_info = MEquityInfo.from_alipay_dict(value)
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        if isinstance(value, list):
            self._ext_info = list()
            for i in value:
                if isinstance(i, MExtInfo):
                    self._ext_info.append(i)
                else:
                    self._ext_info.append(MExtInfo.from_alipay_dict(i))
    @property
    def out_promo_id(self):
        return self._out_promo_id

    @out_promo_id.setter
    def out_promo_id(self, value):
        self._out_promo_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.budget:
            if hasattr(self.budget, 'to_alipay_dict'):
                params['budget'] = self.budget.to_alipay_dict()
            else:
                params['budget'] = self.budget
        if self.constraint:
            if hasattr(self.constraint, 'to_alipay_dict'):
                params['constraint'] = self.constraint.to_alipay_dict()
            else:
                params['constraint'] = self.constraint
        if self.equity_info:
            if hasattr(self.equity_info, 'to_alipay_dict'):
                params['equity_info'] = self.equity_info.to_alipay_dict()
            else:
                params['equity_info'] = self.equity_info
        if self.ext_info:
            if isinstance(self.ext_info, list):
                for i in range(0, len(self.ext_info)):
                    element = self.ext_info[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.ext_info[i] = element.to_alipay_dict()
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        if self.out_promo_id:
            if hasattr(self.out_promo_id, 'to_alipay_dict'):
                params['out_promo_id'] = self.out_promo_id.to_alipay_dict()
            else:
                params['out_promo_id'] = self.out_promo_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MPromoInfo()
        if 'budget' in d:
            o.budget = d['budget']
        if 'constraint' in d:
            o.constraint = d['constraint']
        if 'equity_info' in d:
            o.equity_info = d['equity_info']
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'out_promo_id' in d:
            o.out_promo_id = d['out_promo_id']
        return o


