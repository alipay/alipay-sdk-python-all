#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayIserviceCcmCrmYxblacklistSyncModel(object):

    def __init__(self):
        self._ext_info = None
        self._invalid_time = None
        self._mobile = None
        self._take_time = None
        self._tenant_id = None
        self._user_name = None

    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value
    @property
    def invalid_time(self):
        return self._invalid_time

    @invalid_time.setter
    def invalid_time(self, value):
        self._invalid_time = value
    @property
    def mobile(self):
        return self._mobile

    @mobile.setter
    def mobile(self, value):
        self._mobile = value
    @property
    def take_time(self):
        return self._take_time

    @take_time.setter
    def take_time(self, value):
        self._take_time = value
    @property
    def tenant_id(self):
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, value):
        self._tenant_id = value
    @property
    def user_name(self):
        return self._user_name

    @user_name.setter
    def user_name(self, value):
        self._user_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.ext_info:
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        if self.invalid_time:
            if hasattr(self.invalid_time, 'to_alipay_dict'):
                params['invalid_time'] = self.invalid_time.to_alipay_dict()
            else:
                params['invalid_time'] = self.invalid_time
        if self.mobile:
            if hasattr(self.mobile, 'to_alipay_dict'):
                params['mobile'] = self.mobile.to_alipay_dict()
            else:
                params['mobile'] = self.mobile
        if self.take_time:
            if hasattr(self.take_time, 'to_alipay_dict'):
                params['take_time'] = self.take_time.to_alipay_dict()
            else:
                params['take_time'] = self.take_time
        if self.tenant_id:
            if hasattr(self.tenant_id, 'to_alipay_dict'):
                params['tenant_id'] = self.tenant_id.to_alipay_dict()
            else:
                params['tenant_id'] = self.tenant_id
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
        o = AlipayIserviceCcmCrmYxblacklistSyncModel()
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'invalid_time' in d:
            o.invalid_time = d['invalid_time']
        if 'mobile' in d:
            o.mobile = d['mobile']
        if 'take_time' in d:
            o.take_time = d['take_time']
        if 'tenant_id' in d:
            o.tenant_id = d['tenant_id']
        if 'user_name' in d:
            o.user_name = d['user_name']
        return o


