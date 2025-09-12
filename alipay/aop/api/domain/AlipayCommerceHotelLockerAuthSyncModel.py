#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceHotelLockerAuthSyncModel(object):

    def __init__(self):
        self._auth_id = None
        self._device_id = None
        self._device_isv_code = None
        self._device_sn = None
        self._effective = None
        self._end_time = None
        self._operators_code = None
        self._org_group_code = None
        self._start_time = None
        self._user_relate_id = None
        self._user_relate_type = None

    @property
    def auth_id(self):
        return self._auth_id

    @auth_id.setter
    def auth_id(self, value):
        self._auth_id = value
    @property
    def device_id(self):
        return self._device_id

    @device_id.setter
    def device_id(self, value):
        self._device_id = value
    @property
    def device_isv_code(self):
        return self._device_isv_code

    @device_isv_code.setter
    def device_isv_code(self, value):
        self._device_isv_code = value
    @property
    def device_sn(self):
        return self._device_sn

    @device_sn.setter
    def device_sn(self, value):
        self._device_sn = value
    @property
    def effective(self):
        return self._effective

    @effective.setter
    def effective(self, value):
        self._effective = value
    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, value):
        self._end_time = value
    @property
    def operators_code(self):
        return self._operators_code

    @operators_code.setter
    def operators_code(self, value):
        self._operators_code = value
    @property
    def org_group_code(self):
        return self._org_group_code

    @org_group_code.setter
    def org_group_code(self, value):
        self._org_group_code = value
    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, value):
        self._start_time = value
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
        if self.auth_id:
            if hasattr(self.auth_id, 'to_alipay_dict'):
                params['auth_id'] = self.auth_id.to_alipay_dict()
            else:
                params['auth_id'] = self.auth_id
        if self.device_id:
            if hasattr(self.device_id, 'to_alipay_dict'):
                params['device_id'] = self.device_id.to_alipay_dict()
            else:
                params['device_id'] = self.device_id
        if self.device_isv_code:
            if hasattr(self.device_isv_code, 'to_alipay_dict'):
                params['device_isv_code'] = self.device_isv_code.to_alipay_dict()
            else:
                params['device_isv_code'] = self.device_isv_code
        if self.device_sn:
            if hasattr(self.device_sn, 'to_alipay_dict'):
                params['device_sn'] = self.device_sn.to_alipay_dict()
            else:
                params['device_sn'] = self.device_sn
        if self.effective:
            if hasattr(self.effective, 'to_alipay_dict'):
                params['effective'] = self.effective.to_alipay_dict()
            else:
                params['effective'] = self.effective
        if self.end_time:
            if hasattr(self.end_time, 'to_alipay_dict'):
                params['end_time'] = self.end_time.to_alipay_dict()
            else:
                params['end_time'] = self.end_time
        if self.operators_code:
            if hasattr(self.operators_code, 'to_alipay_dict'):
                params['operators_code'] = self.operators_code.to_alipay_dict()
            else:
                params['operators_code'] = self.operators_code
        if self.org_group_code:
            if hasattr(self.org_group_code, 'to_alipay_dict'):
                params['org_group_code'] = self.org_group_code.to_alipay_dict()
            else:
                params['org_group_code'] = self.org_group_code
        if self.start_time:
            if hasattr(self.start_time, 'to_alipay_dict'):
                params['start_time'] = self.start_time.to_alipay_dict()
            else:
                params['start_time'] = self.start_time
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
        o = AlipayCommerceHotelLockerAuthSyncModel()
        if 'auth_id' in d:
            o.auth_id = d['auth_id']
        if 'device_id' in d:
            o.device_id = d['device_id']
        if 'device_isv_code' in d:
            o.device_isv_code = d['device_isv_code']
        if 'device_sn' in d:
            o.device_sn = d['device_sn']
        if 'effective' in d:
            o.effective = d['effective']
        if 'end_time' in d:
            o.end_time = d['end_time']
        if 'operators_code' in d:
            o.operators_code = d['operators_code']
        if 'org_group_code' in d:
            o.org_group_code = d['org_group_code']
        if 'start_time' in d:
            o.start_time = d['start_time']
        if 'user_relate_id' in d:
            o.user_relate_id = d['user_relate_id']
        if 'user_relate_type' in d:
            o.user_relate_type = d['user_relate_type']
        return o


