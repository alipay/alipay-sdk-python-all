#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ProductBaseVO(object):

    def __init__(self):
        self._biz_status = None
        self._is_combinate = None
        self._prod_env = None
        self._prod_name = None
        self._prod_template_code = None
        self._prod_template_version = None
        self._prod_type = None
        self._prod_version = None
        self._status = None
        self._std_prod_code = None
        self._std_prod_version = None

    @property
    def biz_status(self):
        return self._biz_status

    @biz_status.setter
    def biz_status(self, value):
        self._biz_status = value
    @property
    def is_combinate(self):
        return self._is_combinate

    @is_combinate.setter
    def is_combinate(self, value):
        self._is_combinate = value
    @property
    def prod_env(self):
        return self._prod_env

    @prod_env.setter
    def prod_env(self, value):
        self._prod_env = value
    @property
    def prod_name(self):
        return self._prod_name

    @prod_name.setter
    def prod_name(self, value):
        self._prod_name = value
    @property
    def prod_template_code(self):
        return self._prod_template_code

    @prod_template_code.setter
    def prod_template_code(self, value):
        self._prod_template_code = value
    @property
    def prod_template_version(self):
        return self._prod_template_version

    @prod_template_version.setter
    def prod_template_version(self, value):
        self._prod_template_version = value
    @property
    def prod_type(self):
        return self._prod_type

    @prod_type.setter
    def prod_type(self, value):
        self._prod_type = value
    @property
    def prod_version(self):
        return self._prod_version

    @prod_version.setter
    def prod_version(self, value):
        self._prod_version = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def std_prod_code(self):
        return self._std_prod_code

    @std_prod_code.setter
    def std_prod_code(self, value):
        self._std_prod_code = value
    @property
    def std_prod_version(self):
        return self._std_prod_version

    @std_prod_version.setter
    def std_prod_version(self, value):
        self._std_prod_version = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_status:
            if hasattr(self.biz_status, 'to_alipay_dict'):
                params['biz_status'] = self.biz_status.to_alipay_dict()
            else:
                params['biz_status'] = self.biz_status
        if self.is_combinate:
            if hasattr(self.is_combinate, 'to_alipay_dict'):
                params['is_combinate'] = self.is_combinate.to_alipay_dict()
            else:
                params['is_combinate'] = self.is_combinate
        if self.prod_env:
            if hasattr(self.prod_env, 'to_alipay_dict'):
                params['prod_env'] = self.prod_env.to_alipay_dict()
            else:
                params['prod_env'] = self.prod_env
        if self.prod_name:
            if hasattr(self.prod_name, 'to_alipay_dict'):
                params['prod_name'] = self.prod_name.to_alipay_dict()
            else:
                params['prod_name'] = self.prod_name
        if self.prod_template_code:
            if hasattr(self.prod_template_code, 'to_alipay_dict'):
                params['prod_template_code'] = self.prod_template_code.to_alipay_dict()
            else:
                params['prod_template_code'] = self.prod_template_code
        if self.prod_template_version:
            if hasattr(self.prod_template_version, 'to_alipay_dict'):
                params['prod_template_version'] = self.prod_template_version.to_alipay_dict()
            else:
                params['prod_template_version'] = self.prod_template_version
        if self.prod_type:
            if hasattr(self.prod_type, 'to_alipay_dict'):
                params['prod_type'] = self.prod_type.to_alipay_dict()
            else:
                params['prod_type'] = self.prod_type
        if self.prod_version:
            if hasattr(self.prod_version, 'to_alipay_dict'):
                params['prod_version'] = self.prod_version.to_alipay_dict()
            else:
                params['prod_version'] = self.prod_version
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.std_prod_code:
            if hasattr(self.std_prod_code, 'to_alipay_dict'):
                params['std_prod_code'] = self.std_prod_code.to_alipay_dict()
            else:
                params['std_prod_code'] = self.std_prod_code
        if self.std_prod_version:
            if hasattr(self.std_prod_version, 'to_alipay_dict'):
                params['std_prod_version'] = self.std_prod_version.to_alipay_dict()
            else:
                params['std_prod_version'] = self.std_prod_version
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ProductBaseVO()
        if 'biz_status' in d:
            o.biz_status = d['biz_status']
        if 'is_combinate' in d:
            o.is_combinate = d['is_combinate']
        if 'prod_env' in d:
            o.prod_env = d['prod_env']
        if 'prod_name' in d:
            o.prod_name = d['prod_name']
        if 'prod_template_code' in d:
            o.prod_template_code = d['prod_template_code']
        if 'prod_template_version' in d:
            o.prod_template_version = d['prod_template_version']
        if 'prod_type' in d:
            o.prod_type = d['prod_type']
        if 'prod_version' in d:
            o.prod_version = d['prod_version']
        if 'status' in d:
            o.status = d['status']
        if 'std_prod_code' in d:
            o.std_prod_code = d['std_prod_code']
        if 'std_prod_version' in d:
            o.std_prod_version = d['std_prod_version']
        return o


