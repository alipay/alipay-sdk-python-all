#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceMedicalThirdcodeSyncModel(object):

    def __init__(self):
        self._auth_data_scope = None
        self._auth_data_valid_from = None
        self._open_id = None
        self._third_app_id = None
        self._third_auth_code = None
        self._user_id = None

    @property
    def auth_data_scope(self):
        return self._auth_data_scope

    @auth_data_scope.setter
    def auth_data_scope(self, value):
        self._auth_data_scope = value
    @property
    def auth_data_valid_from(self):
        return self._auth_data_valid_from

    @auth_data_valid_from.setter
    def auth_data_valid_from(self, value):
        self._auth_data_valid_from = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def third_app_id(self):
        return self._third_app_id

    @third_app_id.setter
    def third_app_id(self, value):
        self._third_app_id = value
    @property
    def third_auth_code(self):
        return self._third_auth_code

    @third_auth_code.setter
    def third_auth_code(self, value):
        self._third_auth_code = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.auth_data_scope:
            if hasattr(self.auth_data_scope, 'to_alipay_dict'):
                params['auth_data_scope'] = self.auth_data_scope.to_alipay_dict()
            else:
                params['auth_data_scope'] = self.auth_data_scope
        if self.auth_data_valid_from:
            if hasattr(self.auth_data_valid_from, 'to_alipay_dict'):
                params['auth_data_valid_from'] = self.auth_data_valid_from.to_alipay_dict()
            else:
                params['auth_data_valid_from'] = self.auth_data_valid_from
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.third_app_id:
            if hasattr(self.third_app_id, 'to_alipay_dict'):
                params['third_app_id'] = self.third_app_id.to_alipay_dict()
            else:
                params['third_app_id'] = self.third_app_id
        if self.third_auth_code:
            if hasattr(self.third_auth_code, 'to_alipay_dict'):
                params['third_auth_code'] = self.third_auth_code.to_alipay_dict()
            else:
                params['third_auth_code'] = self.third_auth_code
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
        o = AlipayCommerceMedicalThirdcodeSyncModel()
        if 'auth_data_scope' in d:
            o.auth_data_scope = d['auth_data_scope']
        if 'auth_data_valid_from' in d:
            o.auth_data_valid_from = d['auth_data_valid_from']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'third_app_id' in d:
            o.third_app_id = d['third_app_id']
        if 'third_auth_code' in d:
            o.third_auth_code = d['third_auth_code']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


