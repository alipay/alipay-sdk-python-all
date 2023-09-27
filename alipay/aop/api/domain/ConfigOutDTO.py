#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.FieldOutDTO import FieldOutDTO
from alipay.aop.api.domain.PropertyOutDTO import PropertyOutDTO


class ConfigOutDTO(object):

    def __init__(self):
        self._fields = None
        self._model_code = None
        self._props = None

    @property
    def fields(self):
        return self._fields

    @fields.setter
    def fields(self, value):
        if isinstance(value, list):
            self._fields = list()
            for i in value:
                if isinstance(i, FieldOutDTO):
                    self._fields.append(i)
                else:
                    self._fields.append(FieldOutDTO.from_alipay_dict(i))
    @property
    def model_code(self):
        return self._model_code

    @model_code.setter
    def model_code(self, value):
        self._model_code = value
    @property
    def props(self):
        return self._props

    @props.setter
    def props(self, value):
        if isinstance(value, PropertyOutDTO):
            self._props = value
        else:
            self._props = PropertyOutDTO.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.fields:
            if isinstance(self.fields, list):
                for i in range(0, len(self.fields)):
                    element = self.fields[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.fields[i] = element.to_alipay_dict()
            if hasattr(self.fields, 'to_alipay_dict'):
                params['fields'] = self.fields.to_alipay_dict()
            else:
                params['fields'] = self.fields
        if self.model_code:
            if hasattr(self.model_code, 'to_alipay_dict'):
                params['model_code'] = self.model_code.to_alipay_dict()
            else:
                params['model_code'] = self.model_code
        if self.props:
            if hasattr(self.props, 'to_alipay_dict'):
                params['props'] = self.props.to_alipay_dict()
            else:
                params['props'] = self.props
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ConfigOutDTO()
        if 'fields' in d:
            o.fields = d['fields']
        if 'model_code' in d:
            o.model_code = d['model_code']
        if 'props' in d:
            o.props = d['props']
        return o


