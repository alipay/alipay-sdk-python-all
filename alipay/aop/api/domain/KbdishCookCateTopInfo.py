#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class KbdishCookCateTopInfo(object):

    def __init__(self):
        self._catetory_id = None
        self._cook_id = None
        self._create_user = None
        self._oper_type = None
        self._update_user = None

    @property
    def catetory_id(self):
        return self._catetory_id

    @catetory_id.setter
    def catetory_id(self, value):
        self._catetory_id = value
    @property
    def cook_id(self):
        return self._cook_id

    @cook_id.setter
    def cook_id(self, value):
        self._cook_id = value
    @property
    def create_user(self):
        return self._create_user

    @create_user.setter
    def create_user(self, value):
        self._create_user = value
    @property
    def oper_type(self):
        return self._oper_type

    @oper_type.setter
    def oper_type(self, value):
        self._oper_type = value
    @property
    def update_user(self):
        return self._update_user

    @update_user.setter
    def update_user(self, value):
        self._update_user = value


    def to_alipay_dict(self):
        params = dict()
        if self.catetory_id:
            if hasattr(self.catetory_id, 'to_alipay_dict'):
                params['catetory_id'] = self.catetory_id.to_alipay_dict()
            else:
                params['catetory_id'] = self.catetory_id
        if self.cook_id:
            if hasattr(self.cook_id, 'to_alipay_dict'):
                params['cook_id'] = self.cook_id.to_alipay_dict()
            else:
                params['cook_id'] = self.cook_id
        if self.create_user:
            if hasattr(self.create_user, 'to_alipay_dict'):
                params['create_user'] = self.create_user.to_alipay_dict()
            else:
                params['create_user'] = self.create_user
        if self.oper_type:
            if hasattr(self.oper_type, 'to_alipay_dict'):
                params['oper_type'] = self.oper_type.to_alipay_dict()
            else:
                params['oper_type'] = self.oper_type
        if self.update_user:
            if hasattr(self.update_user, 'to_alipay_dict'):
                params['update_user'] = self.update_user.to_alipay_dict()
            else:
                params['update_user'] = self.update_user
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KbdishCookCateTopInfo()
        if 'catetory_id' in d:
            o.catetory_id = d['catetory_id']
        if 'cook_id' in d:
            o.cook_id = d['cook_id']
        if 'create_user' in d:
            o.create_user = d['create_user']
        if 'oper_type' in d:
            o.oper_type = d['oper_type']
        if 'update_user' in d:
            o.update_user = d['update_user']
        return o


