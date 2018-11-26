#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SubCloudUserInfo(object):

    def __init__(self):
        self._sub_user_id = None
        self._sub_user_name = None
        self._sub_user_show_name = None
        self._user_id = None
        self._user_name = None

    @property
    def sub_user_id(self):
        return self._sub_user_id

    @sub_user_id.setter
    def sub_user_id(self, value):
        self._sub_user_id = value
    @property
    def sub_user_name(self):
        return self._sub_user_name

    @sub_user_name.setter
    def sub_user_name(self, value):
        self._sub_user_name = value
    @property
    def sub_user_show_name(self):
        return self._sub_user_show_name

    @sub_user_show_name.setter
    def sub_user_show_name(self, value):
        self._sub_user_show_name = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value
    @property
    def user_name(self):
        return self._user_name

    @user_name.setter
    def user_name(self, value):
        self._user_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.sub_user_id:
            if hasattr(self.sub_user_id, 'to_alipay_dict'):
                params['sub_user_id'] = self.sub_user_id.to_alipay_dict()
            else:
                params['sub_user_id'] = self.sub_user_id
        if self.sub_user_name:
            if hasattr(self.sub_user_name, 'to_alipay_dict'):
                params['sub_user_name'] = self.sub_user_name.to_alipay_dict()
            else:
                params['sub_user_name'] = self.sub_user_name
        if self.sub_user_show_name:
            if hasattr(self.sub_user_show_name, 'to_alipay_dict'):
                params['sub_user_show_name'] = self.sub_user_show_name.to_alipay_dict()
            else:
                params['sub_user_show_name'] = self.sub_user_show_name
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
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
        o = SubCloudUserInfo()
        if 'sub_user_id' in d:
            o.sub_user_id = d['sub_user_id']
        if 'sub_user_name' in d:
            o.sub_user_name = d['sub_user_name']
        if 'sub_user_show_name' in d:
            o.sub_user_show_name = d['sub_user_show_name']
        if 'user_id' in d:
            o.user_id = d['user_id']
        if 'user_name' in d:
            o.user_name = d['user_name']
        return o


