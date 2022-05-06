#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.AoiUser import AoiUser


class AlipayMerchantAuthCreateModel(object):

    def __init__(self):
        self._channel_code = None
        self._operator_id = None
        self._role = None
        self._scene_code = None
        self._user_list = None

    @property
    def channel_code(self):
        return self._channel_code

    @channel_code.setter
    def channel_code(self, value):
        self._channel_code = value
    @property
    def operator_id(self):
        return self._operator_id

    @operator_id.setter
    def operator_id(self, value):
        self._operator_id = value
    @property
    def role(self):
        return self._role

    @role.setter
    def role(self, value):
        self._role = value
    @property
    def scene_code(self):
        return self._scene_code

    @scene_code.setter
    def scene_code(self, value):
        self._scene_code = value
    @property
    def user_list(self):
        return self._user_list

    @user_list.setter
    def user_list(self, value):
        if isinstance(value, AoiUser):
            self._user_list = value
        else:
            self._user_list = AoiUser.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.channel_code:
            if hasattr(self.channel_code, 'to_alipay_dict'):
                params['channel_code'] = self.channel_code.to_alipay_dict()
            else:
                params['channel_code'] = self.channel_code
        if self.operator_id:
            if hasattr(self.operator_id, 'to_alipay_dict'):
                params['operator_id'] = self.operator_id.to_alipay_dict()
            else:
                params['operator_id'] = self.operator_id
        if self.role:
            if hasattr(self.role, 'to_alipay_dict'):
                params['role'] = self.role.to_alipay_dict()
            else:
                params['role'] = self.role
        if self.scene_code:
            if hasattr(self.scene_code, 'to_alipay_dict'):
                params['scene_code'] = self.scene_code.to_alipay_dict()
            else:
                params['scene_code'] = self.scene_code
        if self.user_list:
            if hasattr(self.user_list, 'to_alipay_dict'):
                params['user_list'] = self.user_list.to_alipay_dict()
            else:
                params['user_list'] = self.user_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayMerchantAuthCreateModel()
        if 'channel_code' in d:
            o.channel_code = d['channel_code']
        if 'operator_id' in d:
            o.operator_id = d['operator_id']
        if 'role' in d:
            o.role = d['role']
        if 'scene_code' in d:
            o.scene_code = d['scene_code']
        if 'user_list' in d:
            o.user_list = d['user_list']
        return o


