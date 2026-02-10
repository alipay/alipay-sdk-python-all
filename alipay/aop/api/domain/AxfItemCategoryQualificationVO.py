#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AxfItemCategoryQualificationVO(object):

    def __init__(self):
        self._param_description = None
        self._qualification_name = None
        self._qualification_type = None

    @property
    def param_description(self):
        return self._param_description

    @param_description.setter
    def param_description(self, value):
        self._param_description = value
    @property
    def qualification_name(self):
        return self._qualification_name

    @qualification_name.setter
    def qualification_name(self, value):
        self._qualification_name = value
    @property
    def qualification_type(self):
        return self._qualification_type

    @qualification_type.setter
    def qualification_type(self, value):
        self._qualification_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.param_description:
            if hasattr(self.param_description, 'to_alipay_dict'):
                params['param_description'] = self.param_description.to_alipay_dict()
            else:
                params['param_description'] = self.param_description
        if self.qualification_name:
            if hasattr(self.qualification_name, 'to_alipay_dict'):
                params['qualification_name'] = self.qualification_name.to_alipay_dict()
            else:
                params['qualification_name'] = self.qualification_name
        if self.qualification_type:
            if hasattr(self.qualification_type, 'to_alipay_dict'):
                params['qualification_type'] = self.qualification_type.to_alipay_dict()
            else:
                params['qualification_type'] = self.qualification_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AxfItemCategoryQualificationVO()
        if 'param_description' in d:
            o.param_description = d['param_description']
        if 'qualification_name' in d:
            o.qualification_name = d['qualification_name']
        if 'qualification_type' in d:
            o.qualification_type = d['qualification_type']
        return o


