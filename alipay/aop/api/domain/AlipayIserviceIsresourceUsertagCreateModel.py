#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayIserviceIsresourceUsertagCreateModel(object):

    def __init__(self):
        self._dt = None
        self._tag_level = None
        self._tag_level_value = None
        self._user_id = None
        self._value = None

    @property
    def dt(self):
        return self._dt

    @dt.setter
    def dt(self, value):
        self._dt = value
    @property
    def tag_level(self):
        return self._tag_level

    @tag_level.setter
    def tag_level(self, value):
        self._tag_level = value
    @property
    def tag_level_value(self):
        return self._tag_level_value

    @tag_level_value.setter
    def tag_level_value(self, value):
        self._tag_level_value = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value
    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value


    def to_alipay_dict(self):
        params = dict()
        if self.dt:
            if hasattr(self.dt, 'to_alipay_dict'):
                params['dt'] = self.dt.to_alipay_dict()
            else:
                params['dt'] = self.dt
        if self.tag_level:
            if hasattr(self.tag_level, 'to_alipay_dict'):
                params['tag_level'] = self.tag_level.to_alipay_dict()
            else:
                params['tag_level'] = self.tag_level
        if self.tag_level_value:
            if hasattr(self.tag_level_value, 'to_alipay_dict'):
                params['tag_level_value'] = self.tag_level_value.to_alipay_dict()
            else:
                params['tag_level_value'] = self.tag_level_value
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        if self.value:
            if hasattr(self.value, 'to_alipay_dict'):
                params['value'] = self.value.to_alipay_dict()
            else:
                params['value'] = self.value
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayIserviceIsresourceUsertagCreateModel()
        if 'dt' in d:
            o.dt = d['dt']
        if 'tag_level' in d:
            o.tag_level = d['tag_level']
        if 'tag_level_value' in d:
            o.tag_level_value = d['tag_level_value']
        if 'user_id' in d:
            o.user_id = d['user_id']
        if 'value' in d:
            o.value = d['value']
        return o


