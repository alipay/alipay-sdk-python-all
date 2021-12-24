#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceSportsFacepayskinReceiveModel(object):

    def __init__(self):
        self._client_version = None
        self._expire_date = None
        self._skin_id = None
        self._user_id = None

    @property
    def client_version(self):
        return self._client_version

    @client_version.setter
    def client_version(self, value):
        self._client_version = value
    @property
    def expire_date(self):
        return self._expire_date

    @expire_date.setter
    def expire_date(self, value):
        self._expire_date = value
    @property
    def skin_id(self):
        return self._skin_id

    @skin_id.setter
    def skin_id(self, value):
        self._skin_id = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.client_version:
            if hasattr(self.client_version, 'to_alipay_dict'):
                params['client_version'] = self.client_version.to_alipay_dict()
            else:
                params['client_version'] = self.client_version
        if self.expire_date:
            if hasattr(self.expire_date, 'to_alipay_dict'):
                params['expire_date'] = self.expire_date.to_alipay_dict()
            else:
                params['expire_date'] = self.expire_date
        if self.skin_id:
            if hasattr(self.skin_id, 'to_alipay_dict'):
                params['skin_id'] = self.skin_id.to_alipay_dict()
            else:
                params['skin_id'] = self.skin_id
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
        o = AlipayCommerceSportsFacepayskinReceiveModel()
        if 'client_version' in d:
            o.client_version = d['client_version']
        if 'expire_date' in d:
            o.expire_date = d['expire_date']
        if 'skin_id' in d:
            o.skin_id = d['skin_id']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


