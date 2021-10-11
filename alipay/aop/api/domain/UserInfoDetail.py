#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class UserInfoDetail(object):

    def __init__(self):
        self._ip_id = None
        self._ip_role_id = None
        self._out_member_id = None
        self._user_info_id = None
        self._user_info_type = None
        self._user_name = None

    @property
    def ip_id(self):
        return self._ip_id

    @ip_id.setter
    def ip_id(self, value):
        self._ip_id = value
    @property
    def ip_role_id(self):
        return self._ip_role_id

    @ip_role_id.setter
    def ip_role_id(self, value):
        self._ip_role_id = value
    @property
    def out_member_id(self):
        return self._out_member_id

    @out_member_id.setter
    def out_member_id(self, value):
        self._out_member_id = value
    @property
    def user_info_id(self):
        return self._user_info_id

    @user_info_id.setter
    def user_info_id(self, value):
        self._user_info_id = value
    @property
    def user_info_type(self):
        return self._user_info_type

    @user_info_type.setter
    def user_info_type(self, value):
        self._user_info_type = value
    @property
    def user_name(self):
        return self._user_name

    @user_name.setter
    def user_name(self, value):
        self._user_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.ip_id:
            if hasattr(self.ip_id, 'to_alipay_dict'):
                params['ip_id'] = self.ip_id.to_alipay_dict()
            else:
                params['ip_id'] = self.ip_id
        if self.ip_role_id:
            if hasattr(self.ip_role_id, 'to_alipay_dict'):
                params['ip_role_id'] = self.ip_role_id.to_alipay_dict()
            else:
                params['ip_role_id'] = self.ip_role_id
        if self.out_member_id:
            if hasattr(self.out_member_id, 'to_alipay_dict'):
                params['out_member_id'] = self.out_member_id.to_alipay_dict()
            else:
                params['out_member_id'] = self.out_member_id
        if self.user_info_id:
            if hasattr(self.user_info_id, 'to_alipay_dict'):
                params['user_info_id'] = self.user_info_id.to_alipay_dict()
            else:
                params['user_info_id'] = self.user_info_id
        if self.user_info_type:
            if hasattr(self.user_info_type, 'to_alipay_dict'):
                params['user_info_type'] = self.user_info_type.to_alipay_dict()
            else:
                params['user_info_type'] = self.user_info_type
        if self.user_name:
            if hasattr(self.user_name, 'to_alipay_dict'):
                params['user_name'] = self.user_name.to_alipay_dict()
            else:
                params['user_name'] = self.user_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = UserInfoDetail()
        if 'ip_id' in d:
            o.ip_id = d['ip_id']
        if 'ip_role_id' in d:
            o.ip_role_id = d['ip_role_id']
        if 'out_member_id' in d:
            o.out_member_id = d['out_member_id']
        if 'user_info_id' in d:
            o.user_info_id = d['user_info_id']
        if 'user_info_type' in d:
            o.user_info_type = d['user_info_type']
        if 'user_name' in d:
            o.user_name = d['user_name']
        return o


