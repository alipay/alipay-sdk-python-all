#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class OpenIdValue(object):

    def __init__(self):
        self._open_id = None
        self._union_id = None
        self._user_id = None

    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def union_id(self):
        return self._union_id

    @union_id.setter
    def union_id(self, value):
        self._union_id = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.union_id:
            if hasattr(self.union_id, 'to_alipay_dict'):
                params['union_id'] = self.union_id.to_alipay_dict()
            else:
                params['union_id'] = self.union_id
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
        o = OpenIdValue()
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'union_id' in d:
            o.union_id = d['union_id']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


