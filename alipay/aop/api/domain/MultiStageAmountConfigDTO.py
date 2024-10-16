#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MultiStageAmountConfigDTO(object):

    def __init__(self):
        self._period_rent_amount = None
        self._period_unit = None
        self._period_unit_num = None

    @property
    def period_rent_amount(self):
        return self._period_rent_amount

    @period_rent_amount.setter
    def period_rent_amount(self, value):
        self._period_rent_amount = value
    @property
    def period_unit(self):
        return self._period_unit

    @period_unit.setter
    def period_unit(self, value):
        self._period_unit = value
    @property
    def period_unit_num(self):
        return self._period_unit_num

    @period_unit_num.setter
    def period_unit_num(self, value):
        self._period_unit_num = value


    def to_alipay_dict(self):
        params = dict()
        if self.period_rent_amount:
            if hasattr(self.period_rent_amount, 'to_alipay_dict'):
                params['period_rent_amount'] = self.period_rent_amount.to_alipay_dict()
            else:
                params['period_rent_amount'] = self.period_rent_amount
        if self.period_unit:
            if hasattr(self.period_unit, 'to_alipay_dict'):
                params['period_unit'] = self.period_unit.to_alipay_dict()
            else:
                params['period_unit'] = self.period_unit
        if self.period_unit_num:
            if hasattr(self.period_unit_num, 'to_alipay_dict'):
                params['period_unit_num'] = self.period_unit_num.to_alipay_dict()
            else:
                params['period_unit_num'] = self.period_unit_num
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MultiStageAmountConfigDTO()
        if 'period_rent_amount' in d:
            o.period_rent_amount = d['period_rent_amount']
        if 'period_unit' in d:
            o.period_unit = d['period_unit']
        if 'period_unit_num' in d:
            o.period_unit_num = d['period_unit_num']
        return o


