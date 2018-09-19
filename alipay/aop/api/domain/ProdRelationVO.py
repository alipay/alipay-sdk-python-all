#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ProdRelationVO(object):

    def __init__(self):
        self._num = None
        self._num_type = None
        self._prod_code = None
        self._prod_rel_code = None
        self._prod_rel_name = None
        self._prod_rel_type = None
        self._prod_rel_version = None
        self._prod_version = None
        self._sub_prod_rel_type = None

    @property
    def num(self):
        return self._num

    @num.setter
    def num(self, value):
        self._num = value
    @property
    def num_type(self):
        return self._num_type

    @num_type.setter
    def num_type(self, value):
        self._num_type = value
    @property
    def prod_code(self):
        return self._prod_code

    @prod_code.setter
    def prod_code(self, value):
        self._prod_code = value
    @property
    def prod_rel_code(self):
        return self._prod_rel_code

    @prod_rel_code.setter
    def prod_rel_code(self, value):
        self._prod_rel_code = value
    @property
    def prod_rel_name(self):
        return self._prod_rel_name

    @prod_rel_name.setter
    def prod_rel_name(self, value):
        self._prod_rel_name = value
    @property
    def prod_rel_type(self):
        return self._prod_rel_type

    @prod_rel_type.setter
    def prod_rel_type(self, value):
        self._prod_rel_type = value
    @property
    def prod_rel_version(self):
        return self._prod_rel_version

    @prod_rel_version.setter
    def prod_rel_version(self, value):
        self._prod_rel_version = value
    @property
    def prod_version(self):
        return self._prod_version

    @prod_version.setter
    def prod_version(self, value):
        self._prod_version = value
    @property
    def sub_prod_rel_type(self):
        return self._sub_prod_rel_type

    @sub_prod_rel_type.setter
    def sub_prod_rel_type(self, value):
        self._sub_prod_rel_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.num:
            if hasattr(self.num, 'to_alipay_dict'):
                params['num'] = self.num.to_alipay_dict()
            else:
                params['num'] = self.num
        if self.num_type:
            if hasattr(self.num_type, 'to_alipay_dict'):
                params['num_type'] = self.num_type.to_alipay_dict()
            else:
                params['num_type'] = self.num_type
        if self.prod_code:
            if hasattr(self.prod_code, 'to_alipay_dict'):
                params['prod_code'] = self.prod_code.to_alipay_dict()
            else:
                params['prod_code'] = self.prod_code
        if self.prod_rel_code:
            if hasattr(self.prod_rel_code, 'to_alipay_dict'):
                params['prod_rel_code'] = self.prod_rel_code.to_alipay_dict()
            else:
                params['prod_rel_code'] = self.prod_rel_code
        if self.prod_rel_name:
            if hasattr(self.prod_rel_name, 'to_alipay_dict'):
                params['prod_rel_name'] = self.prod_rel_name.to_alipay_dict()
            else:
                params['prod_rel_name'] = self.prod_rel_name
        if self.prod_rel_type:
            if hasattr(self.prod_rel_type, 'to_alipay_dict'):
                params['prod_rel_type'] = self.prod_rel_type.to_alipay_dict()
            else:
                params['prod_rel_type'] = self.prod_rel_type
        if self.prod_rel_version:
            if hasattr(self.prod_rel_version, 'to_alipay_dict'):
                params['prod_rel_version'] = self.prod_rel_version.to_alipay_dict()
            else:
                params['prod_rel_version'] = self.prod_rel_version
        if self.prod_version:
            if hasattr(self.prod_version, 'to_alipay_dict'):
                params['prod_version'] = self.prod_version.to_alipay_dict()
            else:
                params['prod_version'] = self.prod_version
        if self.sub_prod_rel_type:
            if hasattr(self.sub_prod_rel_type, 'to_alipay_dict'):
                params['sub_prod_rel_type'] = self.sub_prod_rel_type.to_alipay_dict()
            else:
                params['sub_prod_rel_type'] = self.sub_prod_rel_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ProdRelationVO()
        if 'num' in d:
            o.num = d['num']
        if 'num_type' in d:
            o.num_type = d['num_type']
        if 'prod_code' in d:
            o.prod_code = d['prod_code']
        if 'prod_rel_code' in d:
            o.prod_rel_code = d['prod_rel_code']
        if 'prod_rel_name' in d:
            o.prod_rel_name = d['prod_rel_name']
        if 'prod_rel_type' in d:
            o.prod_rel_type = d['prod_rel_type']
        if 'prod_rel_version' in d:
            o.prod_rel_version = d['prod_rel_version']
        if 'prod_version' in d:
            o.prod_version = d['prod_version']
        if 'sub_prod_rel_type' in d:
            o.sub_prod_rel_type = d['sub_prod_rel_type']
        return o


