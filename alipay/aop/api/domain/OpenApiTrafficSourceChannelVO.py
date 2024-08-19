#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class OpenApiTrafficSourceChannelVO(object):

    def __init__(self):
        self._first_source_type = None
        self._second_source_type = None

    @property
    def first_source_type(self):
        return self._first_source_type

    @first_source_type.setter
    def first_source_type(self, value):
        self._first_source_type = value
    @property
    def second_source_type(self):
        return self._second_source_type

    @second_source_type.setter
    def second_source_type(self, value):
        self._second_source_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.first_source_type:
            if hasattr(self.first_source_type, 'to_alipay_dict'):
                params['first_source_type'] = self.first_source_type.to_alipay_dict()
            else:
                params['first_source_type'] = self.first_source_type
        if self.second_source_type:
            if hasattr(self.second_source_type, 'to_alipay_dict'):
                params['second_source_type'] = self.second_source_type.to_alipay_dict()
            else:
                params['second_source_type'] = self.second_source_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = OpenApiTrafficSourceChannelVO()
        if 'first_source_type' in d:
            o.first_source_type = d['first_source_type']
        if 'second_source_type' in d:
            o.second_source_type = d['second_source_type']
        return o


