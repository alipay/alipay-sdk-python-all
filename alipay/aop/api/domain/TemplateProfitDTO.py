#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class TemplateProfitDTO(object):

    def __init__(self):
        self._profit_pre_desc = None
        self._profit_unit = None
        self._profit_value = None

    @property
    def profit_pre_desc(self):
        return self._profit_pre_desc

    @profit_pre_desc.setter
    def profit_pre_desc(self, value):
        self._profit_pre_desc = value
    @property
    def profit_unit(self):
        return self._profit_unit

    @profit_unit.setter
    def profit_unit(self, value):
        self._profit_unit = value
    @property
    def profit_value(self):
        return self._profit_value

    @profit_value.setter
    def profit_value(self, value):
        self._profit_value = value


    def to_alipay_dict(self):
        params = dict()
        if self.profit_pre_desc:
            if hasattr(self.profit_pre_desc, 'to_alipay_dict'):
                params['profit_pre_desc'] = self.profit_pre_desc.to_alipay_dict()
            else:
                params['profit_pre_desc'] = self.profit_pre_desc
        if self.profit_unit:
            if hasattr(self.profit_unit, 'to_alipay_dict'):
                params['profit_unit'] = self.profit_unit.to_alipay_dict()
            else:
                params['profit_unit'] = self.profit_unit
        if self.profit_value:
            if hasattr(self.profit_value, 'to_alipay_dict'):
                params['profit_value'] = self.profit_value.to_alipay_dict()
            else:
                params['profit_value'] = self.profit_value
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = TemplateProfitDTO()
        if 'profit_pre_desc' in d:
            o.profit_pre_desc = d['profit_pre_desc']
        if 'profit_unit' in d:
            o.profit_unit = d['profit_unit']
        if 'profit_value' in d:
            o.profit_value = d['profit_value']
        return o


