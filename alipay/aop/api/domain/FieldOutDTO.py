#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.PropertyOutDTO import PropertyOutDTO


class FieldOutDTO(object):

    def __init__(self):
        self._code = None
        self._props = None

    @property
    def code(self):
        return self._code

    @code.setter
    def code(self, value):
        self._code = value
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
        if self.code:
            if hasattr(self.code, 'to_alipay_dict'):
                params['code'] = self.code.to_alipay_dict()
            else:
                params['code'] = self.code
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
        o = FieldOutDTO()
        if 'code' in d:
            o.code = d['code']
        if 'props' in d:
            o.props = d['props']
        return o


