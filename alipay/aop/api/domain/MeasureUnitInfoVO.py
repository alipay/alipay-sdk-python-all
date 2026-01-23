#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.MeasureUnitVO import MeasureUnitVO


class MeasureUnitInfoVO(object):

    def __init__(self):
        self._module_id = None
        self._units = None

    @property
    def module_id(self):
        return self._module_id

    @module_id.setter
    def module_id(self, value):
        self._module_id = value
    @property
    def units(self):
        return self._units

    @units.setter
    def units(self, value):
        if isinstance(value, list):
            self._units = list()
            for i in value:
                if isinstance(i, MeasureUnitVO):
                    self._units.append(i)
                else:
                    self._units.append(MeasureUnitVO.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.module_id:
            if hasattr(self.module_id, 'to_alipay_dict'):
                params['module_id'] = self.module_id.to_alipay_dict()
            else:
                params['module_id'] = self.module_id
        if self.units:
            if isinstance(self.units, list):
                for i in range(0, len(self.units)):
                    element = self.units[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.units[i] = element.to_alipay_dict()
            if hasattr(self.units, 'to_alipay_dict'):
                params['units'] = self.units.to_alipay_dict()
            else:
                params['units'] = self.units
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MeasureUnitInfoVO()
        if 'module_id' in d:
            o.module_id = d['module_id']
        if 'units' in d:
            o.units = d['units']
        return o


