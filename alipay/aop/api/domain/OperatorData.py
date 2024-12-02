#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class OperatorData(object):

    def __init__(self):
        self._avatar = None
        self._operator_id = None
        self._operator_name = None
        self._operator_open_id = None

    @property
    def avatar(self):
        return self._avatar

    @avatar.setter
    def avatar(self, value):
        self._avatar = value
    @property
    def operator_id(self):
        return self._operator_id

    @operator_id.setter
    def operator_id(self, value):
        self._operator_id = value
    @property
    def operator_name(self):
        return self._operator_name

    @operator_name.setter
    def operator_name(self, value):
        self._operator_name = value
    @property
    def operator_open_id(self):
        return self._operator_open_id

    @operator_open_id.setter
    def operator_open_id(self, value):
        self._operator_open_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.avatar:
            if hasattr(self.avatar, 'to_alipay_dict'):
                params['avatar'] = self.avatar.to_alipay_dict()
            else:
                params['avatar'] = self.avatar
        if self.operator_id:
            if hasattr(self.operator_id, 'to_alipay_dict'):
                params['operator_id'] = self.operator_id.to_alipay_dict()
            else:
                params['operator_id'] = self.operator_id
        if self.operator_name:
            if hasattr(self.operator_name, 'to_alipay_dict'):
                params['operator_name'] = self.operator_name.to_alipay_dict()
            else:
                params['operator_name'] = self.operator_name
        if self.operator_open_id:
            if hasattr(self.operator_open_id, 'to_alipay_dict'):
                params['operator_open_id'] = self.operator_open_id.to_alipay_dict()
            else:
                params['operator_open_id'] = self.operator_open_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = OperatorData()
        if 'avatar' in d:
            o.avatar = d['avatar']
        if 'operator_id' in d:
            o.operator_id = d['operator_id']
        if 'operator_name' in d:
            o.operator_name = d['operator_name']
        if 'operator_open_id' in d:
            o.operator_open_id = d['operator_open_id']
        return o


