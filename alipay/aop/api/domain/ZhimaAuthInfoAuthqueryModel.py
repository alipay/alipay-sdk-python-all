#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ZhimaAuthInfoAuthqueryModel(object):

    def __init__(self):
        self._identity_param = None

    @property
    def identity_param(self):
        return self._identity_param

    @identity_param.setter
    def identity_param(self, value):
        self._identity_param = value


    def to_alipay_dict(self):
        params = dict()
        if self.identity_param:
            if hasattr(self.identity_param, 'to_alipay_dict'):
                params['identity_param'] = self.identity_param.to_alipay_dict()
            else:
                params['identity_param'] = self.identity_param
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ZhimaAuthInfoAuthqueryModel()
        if 'identity_param' in d:
            o.identity_param = d['identity_param']
        return o


