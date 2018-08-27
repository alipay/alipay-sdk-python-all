#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayInsSceneProductSignConfirmModel(object):

    def __init__(self):
        self._prod_code = None
        self._user_id = None

    @property
    def prod_code(self):
        return self._prod_code

    @prod_code.setter
    def prod_code(self, value):
        self._prod_code = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.prod_code:
            if hasattr(self.prod_code, 'to_alipay_dict'):
                params['prod_code'] = self.prod_code.to_alipay_dict()
            else:
                params['prod_code'] = self.prod_code
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayInsSceneProductSignConfirmModel()
        if 'prod_code' in d:
            o.prod_code = d['prod_code']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


