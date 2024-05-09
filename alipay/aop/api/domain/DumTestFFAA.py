#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class DumTestFFAA(object):

    def __init__(self):
        self._field_a = None
        self._open_id = None
        self._user_id = None

    @property
    def field_a(self):
        return self._field_a

    @field_a.setter
    def field_a(self, value):
        self._field_a = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.field_a:
            if hasattr(self.field_a, 'to_alipay_dict'):
                params['field_a'] = self.field_a.to_alipay_dict()
            else:
                params['field_a'] = self.field_a
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
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
        o = DumTestFFAA()
        if 'field_a' in d:
            o.field_a = d['field_a']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


