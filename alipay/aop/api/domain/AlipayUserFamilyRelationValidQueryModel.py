#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayUserFamilyRelationValidQueryModel(object):

    def __init__(self):
        self._strict = None
        self._user_id = None

    @property
    def strict(self):
        return self._strict

    @strict.setter
    def strict(self, value):
        self._strict = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.strict:
            if hasattr(self.strict, 'to_alipay_dict'):
                params['strict'] = self.strict.to_alipay_dict()
            else:
                params['strict'] = self.strict
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
        o = AlipayUserFamilyRelationValidQueryModel()
        if 'strict' in d:
            o.strict = d['strict']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


