#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.FengdieActivitySchemaModel import FengdieActivitySchemaModel


class FengdieActivityComponentModel(object):

    def __init__(self):
        self._component_data = None
        self._name = None

    @property
    def component_data(self):
        return self._component_data

    @component_data.setter
    def component_data(self, value):
        if isinstance(value, list):
            self._component_data = list()
            for i in value:
                if isinstance(i, FengdieActivitySchemaModel):
                    self._component_data.append(i)
                else:
                    self._component_data.append(FengdieActivitySchemaModel.from_alipay_dict(i))
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value


    def to_alipay_dict(self):
        params = dict()
        if self.component_data:
            if isinstance(self.component_data, list):
                for i in range(0, len(self.component_data)):
                    element = self.component_data[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.component_data[i] = element.to_alipay_dict()
            if hasattr(self.component_data, 'to_alipay_dict'):
                params['component_data'] = self.component_data.to_alipay_dict()
            else:
                params['component_data'] = self.component_data
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = FengdieActivityComponentModel()
        if 'component_data' in d:
            o.component_data = d['component_data']
        if 'name' in d:
            o.name = d['name']
        return o


