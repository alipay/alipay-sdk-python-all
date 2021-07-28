#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class DiseaseDTO(object):

    def __init__(self):
        self._code = None
        self._disease_name = None

    @property
    def code(self):
        return self._code

    @code.setter
    def code(self, value):
        self._code = value
    @property
    def disease_name(self):
        return self._disease_name

    @disease_name.setter
    def disease_name(self, value):
        self._disease_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.code:
            if hasattr(self.code, 'to_alipay_dict'):
                params['code'] = self.code.to_alipay_dict()
            else:
                params['code'] = self.code
        if self.disease_name:
            if hasattr(self.disease_name, 'to_alipay_dict'):
                params['disease_name'] = self.disease_name.to_alipay_dict()
            else:
                params['disease_name'] = self.disease_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DiseaseDTO()
        if 'code' in d:
            o.code = d['code']
        if 'disease_name' in d:
            o.disease_name = d['disease_name']
        return o


