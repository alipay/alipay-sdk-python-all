#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class OpenApiWithholdPlanDetailPojo(object):

    def __init__(self):
        self._period_no = None
        self._to_repay_amount = None
        self._withhold_date = None

    @property
    def period_no(self):
        return self._period_no

    @period_no.setter
    def period_no(self, value):
        self._period_no = value
    @property
    def to_repay_amount(self):
        return self._to_repay_amount

    @to_repay_amount.setter
    def to_repay_amount(self, value):
        self._to_repay_amount = value
    @property
    def withhold_date(self):
        return self._withhold_date

    @withhold_date.setter
    def withhold_date(self, value):
        self._withhold_date = value


    def to_alipay_dict(self):
        params = dict()
        if self.period_no:
            if hasattr(self.period_no, 'to_alipay_dict'):
                params['period_no'] = self.period_no.to_alipay_dict()
            else:
                params['period_no'] = self.period_no
        if self.to_repay_amount:
            if hasattr(self.to_repay_amount, 'to_alipay_dict'):
                params['to_repay_amount'] = self.to_repay_amount.to_alipay_dict()
            else:
                params['to_repay_amount'] = self.to_repay_amount
        if self.withhold_date:
            if hasattr(self.withhold_date, 'to_alipay_dict'):
                params['withhold_date'] = self.withhold_date.to_alipay_dict()
            else:
                params['withhold_date'] = self.withhold_date
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = OpenApiWithholdPlanDetailPojo()
        if 'period_no' in d:
            o.period_no = d['period_no']
        if 'to_repay_amount' in d:
            o.to_repay_amount = d['to_repay_amount']
        if 'withhold_date' in d:
            o.withhold_date = d['withhold_date']
        return o


