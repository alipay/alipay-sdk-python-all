#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ProdLORelationVO(object):

    def __init__(self):
        self._lo_code = None
        self._lo_type = None
        self._prod_code = None
        self._prod_version = None

    @property
    def lo_code(self):
        return self._lo_code

    @lo_code.setter
    def lo_code(self, value):
        self._lo_code = value
    @property
    def lo_type(self):
        return self._lo_type

    @lo_type.setter
    def lo_type(self, value):
        self._lo_type = value
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
        if self.lo_code:
            if hasattr(self.lo_code, 'to_alipay_dict'):
                params['lo_code'] = self.lo_code.to_alipay_dict()
            else:
                params['lo_code'] = self.lo_code
        if self.lo_type:
            if hasattr(self.lo_type, 'to_alipay_dict'):
                params['lo_type'] = self.lo_type.to_alipay_dict()
            else:
                params['lo_type'] = self.lo_type
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
        o = ProdLORelationVO()
        if 'lo_code' in d:
            o.lo_code = d['lo_code']
        if 'lo_type' in d:
            o.lo_type = d['lo_type']
        if 'prod_code' in d:
            o.prod_code = d['prod_code']
        if 'prod_version' in d:
            o.prod_version = d['prod_version']
        return o


