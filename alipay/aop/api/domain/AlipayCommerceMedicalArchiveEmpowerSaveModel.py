#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.KnxAuthDetail import KnxAuthDetail


class AlipayCommerceMedicalArchiveEmpowerSaveModel(object):

    def __init__(self):
        self._access_token = None
        self._auth_action = None
        self._auth_code = None
        self._auth_status = None
        self._data_source = None
        self._knx_auth_datail = None
        self._member_id = None
        self._open_id = None
        self._user_id = None

    @property
    def access_token(self):
        return self._access_token

    @access_token.setter
    def access_token(self, value):
        self._access_token = value
    @property
    def auth_action(self):
        return self._auth_action

    @auth_action.setter
    def auth_action(self, value):
        self._auth_action = value
    @property
    def auth_code(self):
        return self._auth_code

    @auth_code.setter
    def auth_code(self, value):
        self._auth_code = value
    @property
    def auth_status(self):
        return self._auth_status

    @auth_status.setter
    def auth_status(self, value):
        self._auth_status = value
    @property
    def data_source(self):
        return self._data_source

    @data_source.setter
    def data_source(self, value):
        self._data_source = value
    @property
    def knx_auth_datail(self):
        return self._knx_auth_datail

    @knx_auth_datail.setter
    def knx_auth_datail(self, value):
        if isinstance(value, KnxAuthDetail):
            self._knx_auth_datail = value
        else:
            self._knx_auth_datail = KnxAuthDetail.from_alipay_dict(value)
    @property
    def member_id(self):
        return self._member_id

    @member_id.setter
    def member_id(self, value):
        self._member_id = value
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


    def to_alipay_dict(self):
        params = dict()
        if self.access_token:
            if hasattr(self.access_token, 'to_alipay_dict'):
                params['access_token'] = self.access_token.to_alipay_dict()
            else:
                params['access_token'] = self.access_token
        if self.auth_action:
            if hasattr(self.auth_action, 'to_alipay_dict'):
                params['auth_action'] = self.auth_action.to_alipay_dict()
            else:
                params['auth_action'] = self.auth_action
        if self.auth_code:
            if hasattr(self.auth_code, 'to_alipay_dict'):
                params['auth_code'] = self.auth_code.to_alipay_dict()
            else:
                params['auth_code'] = self.auth_code
        if self.auth_status:
            if hasattr(self.auth_status, 'to_alipay_dict'):
                params['auth_status'] = self.auth_status.to_alipay_dict()
            else:
                params['auth_status'] = self.auth_status
        if self.data_source:
            if hasattr(self.data_source, 'to_alipay_dict'):
                params['data_source'] = self.data_source.to_alipay_dict()
            else:
                params['data_source'] = self.data_source
        if self.knx_auth_datail:
            if hasattr(self.knx_auth_datail, 'to_alipay_dict'):
                params['knx_auth_datail'] = self.knx_auth_datail.to_alipay_dict()
            else:
                params['knx_auth_datail'] = self.knx_auth_datail
        if self.member_id:
            if hasattr(self.member_id, 'to_alipay_dict'):
                params['member_id'] = self.member_id.to_alipay_dict()
            else:
                params['member_id'] = self.member_id
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
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMedicalArchiveEmpowerSaveModel()
        if 'access_token' in d:
            o.access_token = d['access_token']
        if 'auth_action' in d:
            o.auth_action = d['auth_action']
        if 'auth_code' in d:
            o.auth_code = d['auth_code']
        if 'auth_status' in d:
            o.auth_status = d['auth_status']
        if 'data_source' in d:
            o.data_source = d['data_source']
        if 'knx_auth_datail' in d:
            o.knx_auth_datail = d['knx_auth_datail']
        if 'member_id' in d:
            o.member_id = d['member_id']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


