#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.Filter import Filter
from alipay.aop.api.domain.Material import Material


class AlipayOpenPublicMessageLabelSendModel(object):

    def __init__(self):
        self._filter = None
        self._material = None

    @property
    def filter(self):
        return self._filter

    @filter.setter
    def filter(self, value):
        if isinstance(value, Filter):
            self._filter = value
        else:
            self._filter = Filter.from_alipay_dict(value)
    @property
    def material(self):
        return self._material

    @material.setter
    def material(self, value):
        if isinstance(value, Material):
            self._material = value
        else:
            self._material = Material.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.filter:
            if hasattr(self.filter, 'to_alipay_dict'):
                params['filter'] = self.filter.to_alipay_dict()
            else:
                params['filter'] = self.filter
        if self.material:
            if hasattr(self.material, 'to_alipay_dict'):
                params['material'] = self.material.to_alipay_dict()
            else:
                params['material'] = self.material
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenPublicMessageLabelSendModel()
        if 'filter' in d:
            o.filter = d['filter']
        if 'material' in d:
            o.material = d['material']
        return o


