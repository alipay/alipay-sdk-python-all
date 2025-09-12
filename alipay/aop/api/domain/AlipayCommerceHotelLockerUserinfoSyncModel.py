#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceHotelLockerUserinfoSyncModel(object):

    def __init__(self):
        self._open_id = None
        self._org_group_code = None
        self._user_id = None
        self._user_relate_id = None
        self._user_relate_type = None

    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def org_group_code(self):
        return self._org_group_code

    @org_group_code.setter
    def org_group_code(self, value):
        self._org_group_code = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value
    @property
    def user_relate_id(self):
        return self._user_relate_id

    @user_relate_id.setter
    def user_relate_id(self, value):
        self._user_relate_id = value
    @property
    def user_relate_type(self):
        return self._user_relate_type

    @user_relate_type.setter
    def user_relate_type(self, value):
        self._user_relate_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.org_group_code:
            if hasattr(self.org_group_code, 'to_alipay_dict'):
                params['org_group_code'] = self.org_group_code.to_alipay_dict()
            else:
                params['org_group_code'] = self.org_group_code
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        if self.user_relate_id:
            if hasattr(self.user_relate_id, 'to_alipay_dict'):
                params['user_relate_id'] = self.user_relate_id.to_alipay_dict()
            else:
                params['user_relate_id'] = self.user_relate_id
        if self.user_relate_type:
            if hasattr(self.user_relate_type, 'to_alipay_dict'):
                params['user_relate_type'] = self.user_relate_type.to_alipay_dict()
            else:
                params['user_relate_type'] = self.user_relate_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceHotelLockerUserinfoSyncModel()
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'org_group_code' in d:
            o.org_group_code = d['org_group_code']
        if 'user_id' in d:
            o.user_id = d['user_id']
        if 'user_relate_id' in d:
            o.user_relate_id = d['user_relate_id']
        if 'user_relate_type' in d:
            o.user_relate_type = d['user_relate_type']
        return o


