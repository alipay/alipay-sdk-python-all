#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ZhimaAuthInfoAuthqueryModel(object):

    def __init__(self):
        self._auth_category = None
        self._identity_param = None
        self._identity_type = None

    @property
    def auth_category(self):
        return self._auth_category

    @auth_category.setter
    def auth_category(self, value):
        self._auth_category = value
    @property
    def identity_param(self):
        return self._identity_param

    @identity_param.setter
    def identity_param(self, value):
        self._identity_param = value
    @property
    def identity_type(self):
        return self._identity_type

    @identity_type.setter
    def identity_type(self, value):
        self._identity_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.auth_category:
            if hasattr(self.auth_category, 'to_alipay_dict'):
                params['auth_category'] = self.auth_category.to_alipay_dict()
            else:
                params['auth_category'] = self.auth_category
        if self.identity_param:
            if hasattr(self.identity_param, 'to_alipay_dict'):
                params['identity_param'] = self.identity_param.to_alipay_dict()
            else:
                params['identity_param'] = self.identity_param
        if self.identity_type:
            if hasattr(self.identity_type, 'to_alipay_dict'):
                params['identity_type'] = self.identity_type.to_alipay_dict()
            else:
                params['identity_type'] = self.identity_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ZhimaAuthInfoAuthqueryModel()
        if 'auth_category' in d:
            o.auth_category = d['auth_category']
        if 'identity_param' in d:
            o.identity_param = d['identity_param']
        if 'identity_type' in d:
            o.identity_type = d['identity_type']
        return o


