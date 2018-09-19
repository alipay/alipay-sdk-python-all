#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ProdParams(object):

    def __init__(self):
        self._auth_biz_params = None

    @property
    def auth_biz_params(self):
        return self._auth_biz_params

    @auth_biz_params.setter
    def auth_biz_params(self, value):
        self._auth_biz_params = value


    def to_alipay_dict(self):
        params = dict()
        if self.auth_biz_params:
            if hasattr(self.auth_biz_params, 'to_alipay_dict'):
                params['auth_biz_params'] = self.auth_biz_params.to_alipay_dict()
            else:
                params['auth_biz_params'] = self.auth_biz_params
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ProdParams()
        if 'auth_biz_params' in d:
            o.auth_biz_params = d['auth_biz_params']
        return o


