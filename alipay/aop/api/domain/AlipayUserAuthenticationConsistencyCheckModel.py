#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayUserAuthenticationConsistencyCheckModel(object):

    def __init__(self):
        self._biz_from = None
        self._cert_type = None
        self._check_by_license = None
        self._encrypt_code = None
        self._ent_name = None
        self._open_id = None
        self._user_id = None
        self._user_type = None

    @property
    def biz_from(self):
        return self._biz_from

    @biz_from.setter
    def biz_from(self, value):
        self._biz_from = value
    @property
    def cert_type(self):
        return self._cert_type

    @cert_type.setter
    def cert_type(self, value):
        self._cert_type = value
    @property
    def check_by_license(self):
        return self._check_by_license

    @check_by_license.setter
    def check_by_license(self, value):
        self._check_by_license = value
    @property
    def encrypt_code(self):
        return self._encrypt_code

    @encrypt_code.setter
    def encrypt_code(self, value):
        self._encrypt_code = value
    @property
    def ent_name(self):
        return self._ent_name

    @ent_name.setter
    def ent_name(self, value):
        self._ent_name = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value
    @property
    def user_type(self):
        return self._user_type

    @user_type.setter
    def user_type(self, value):
        self._user_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_from:
            if hasattr(self.biz_from, 'to_alipay_dict'):
                params['biz_from'] = self.biz_from.to_alipay_dict()
            else:
                params['biz_from'] = self.biz_from
        if self.cert_type:
            if hasattr(self.cert_type, 'to_alipay_dict'):
                params['cert_type'] = self.cert_type.to_alipay_dict()
            else:
                params['cert_type'] = self.cert_type
        if self.check_by_license:
            if hasattr(self.check_by_license, 'to_alipay_dict'):
                params['check_by_license'] = self.check_by_license.to_alipay_dict()
            else:
                params['check_by_license'] = self.check_by_license
        if self.encrypt_code:
            if hasattr(self.encrypt_code, 'to_alipay_dict'):
                params['encrypt_code'] = self.encrypt_code.to_alipay_dict()
            else:
                params['encrypt_code'] = self.encrypt_code
        if self.ent_name:
            if hasattr(self.ent_name, 'to_alipay_dict'):
                params['ent_name'] = self.ent_name.to_alipay_dict()
            else:
                params['ent_name'] = self.ent_name
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        if self.user_type:
            if hasattr(self.user_type, 'to_alipay_dict'):
                params['user_type'] = self.user_type.to_alipay_dict()
            else:
                params['user_type'] = self.user_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayUserAuthenticationConsistencyCheckModel()
        if 'biz_from' in d:
            o.biz_from = d['biz_from']
        if 'cert_type' in d:
            o.cert_type = d['cert_type']
        if 'check_by_license' in d:
            o.check_by_license = d['check_by_license']
        if 'encrypt_code' in d:
            o.encrypt_code = d['encrypt_code']
        if 'ent_name' in d:
            o.ent_name = d['ent_name']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'user_id' in d:
            o.user_id = d['user_id']
        if 'user_type' in d:
            o.user_type = d['user_type']
        return o


