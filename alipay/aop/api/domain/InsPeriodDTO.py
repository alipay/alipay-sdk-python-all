#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class InsPeriodDTO(object):

    def __init__(self):
        self._option_tag = None
        self._period = None
        self._recommend = None
        self._unit = None

    @property
    def option_tag(self):
        return self._option_tag

    @option_tag.setter
    def option_tag(self, value):
        self._option_tag = value
    @property
    def period(self):
        return self._period

    @period.setter
    def period(self, value):
        self._period = value
    @property
    def recommend(self):
        return self._recommend

    @recommend.setter
    def recommend(self, value):
        self._recommend = value
    @property
    def unit(self):
        return self._unit

    @unit.setter
    def unit(self, value):
        self._unit = value


    def to_alipay_dict(self):
        params = dict()
        if self.option_tag:
            if hasattr(self.option_tag, 'to_alipay_dict'):
                params['option_tag'] = self.option_tag.to_alipay_dict()
            else:
                params['option_tag'] = self.option_tag
        if self.period:
            if hasattr(self.period, 'to_alipay_dict'):
                params['period'] = self.period.to_alipay_dict()
            else:
                params['period'] = self.period
        if self.recommend:
            if hasattr(self.recommend, 'to_alipay_dict'):
                params['recommend'] = self.recommend.to_alipay_dict()
            else:
                params['recommend'] = self.recommend
        if self.unit:
            if hasattr(self.unit, 'to_alipay_dict'):
                params['unit'] = self.unit.to_alipay_dict()
            else:
                params['unit'] = self.unit
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = InsPeriodDTO()
        if 'option_tag' in d:
            o.option_tag = d['option_tag']
        if 'period' in d:
            o.period = d['period']
        if 'recommend' in d:
            o.recommend = d['recommend']
        if 'unit' in d:
            o.unit = d['unit']
        return o


