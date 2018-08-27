#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ProdMarkRelationVO(object):

    def __init__(self):
        self._mark_code = None
        self._mark_type = None
        self._prod_code = None
        self._prod_version = None

    @property
    def mark_code(self):
        return self._mark_code

    @mark_code.setter
    def mark_code(self, value):
        self._mark_code = value
    @property
    def mark_type(self):
        return self._mark_type

    @mark_type.setter
    def mark_type(self, value):
        self._mark_type = value
    @property
    def prod_code(self):
        return self._prod_code

    @prod_code.setter
    def prod_code(self, value):
        self._prod_code = value
    @property
    def prod_version(self):
        return self._prod_version

    @prod_version.setter
    def prod_version(self, value):
        self._prod_version = value


    def to_alipay_dict(self):
        params = dict()
        if self.mark_code:
            if hasattr(self.mark_code, 'to_alipay_dict'):
                params['mark_code'] = self.mark_code.to_alipay_dict()
            else:
                params['mark_code'] = self.mark_code
        if self.mark_type:
            if hasattr(self.mark_type, 'to_alipay_dict'):
                params['mark_type'] = self.mark_type.to_alipay_dict()
            else:
                params['mark_type'] = self.mark_type
        if self.prod_code:
            if hasattr(self.prod_code, 'to_alipay_dict'):
                params['prod_code'] = self.prod_code.to_alipay_dict()
            else:
                params['prod_code'] = self.prod_code
        if self.prod_version:
            if hasattr(self.prod_version, 'to_alipay_dict'):
                params['prod_version'] = self.prod_version.to_alipay_dict()
            else:
                params['prod_version'] = self.prod_version
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ProdMarkRelationVO()
        if 'mark_code' in d:
            o.mark_code = d['mark_code']
        if 'mark_type' in d:
            o.mark_type = d['mark_type']
        if 'prod_code' in d:
            o.prod_code = d['prod_code']
        if 'prod_version' in d:
            o.prod_version = d['prod_version']
        return o


