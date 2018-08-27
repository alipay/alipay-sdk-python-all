#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipaySecurityRiskReconfirmRiskidentifyCertifyModel(object):

    def __init__(self):
        self._account = None
        self._app_code = None
        self._company = None
        self._extend_param = None
        self._scene_code = None
        self._tenant_id_list = None
        self._um_id = None
        self._um_id_token = None
        self._user_id = None

    @property
    def account(self):
        return self._account

    @account.setter
    def account(self, value):
        self._account = value
    @property
    def app_code(self):
        return self._app_code

    @app_code.setter
    def app_code(self, value):
        self._app_code = value
    @property
    def company(self):
        return self._company

    @company.setter
    def company(self, value):
        self._company = value
    @property
    def extend_param(self):
        return self._extend_param

    @extend_param.setter
    def extend_param(self, value):
        self._extend_param = value
    @property
    def scene_code(self):
        return self._scene_code

    @scene_code.setter
    def scene_code(self, value):
        self._scene_code = value
    @property
    def tenant_id_list(self):
        return self._tenant_id_list

    @tenant_id_list.setter
    def tenant_id_list(self, value):
        self._tenant_id_list = value
    @property
    def um_id(self):
        return self._um_id

    @um_id.setter
    def um_id(self, value):
        self._um_id = value
    @property
    def um_id_token(self):
        return self._um_id_token

    @um_id_token.setter
    def um_id_token(self, value):
        self._um_id_token = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.account:
            if hasattr(self.account, 'to_alipay_dict'):
                params['account'] = self.account.to_alipay_dict()
            else:
                params['account'] = self.account
        if self.app_code:
            if hasattr(self.app_code, 'to_alipay_dict'):
                params['app_code'] = self.app_code.to_alipay_dict()
            else:
                params['app_code'] = self.app_code
        if self.company:
            if hasattr(self.company, 'to_alipay_dict'):
                params['company'] = self.company.to_alipay_dict()
            else:
                params['company'] = self.company
        if self.extend_param:
            if hasattr(self.extend_param, 'to_alipay_dict'):
                params['extend_param'] = self.extend_param.to_alipay_dict()
            else:
                params['extend_param'] = self.extend_param
        if self.scene_code:
            if hasattr(self.scene_code, 'to_alipay_dict'):
                params['scene_code'] = self.scene_code.to_alipay_dict()
            else:
                params['scene_code'] = self.scene_code
        if self.tenant_id_list:
            if hasattr(self.tenant_id_list, 'to_alipay_dict'):
                params['tenant_id_list'] = self.tenant_id_list.to_alipay_dict()
            else:
                params['tenant_id_list'] = self.tenant_id_list
        if self.um_id:
            if hasattr(self.um_id, 'to_alipay_dict'):
                params['um_id'] = self.um_id.to_alipay_dict()
            else:
                params['um_id'] = self.um_id
        if self.um_id_token:
            if hasattr(self.um_id_token, 'to_alipay_dict'):
                params['um_id_token'] = self.um_id_token.to_alipay_dict()
            else:
                params['um_id_token'] = self.um_id_token
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
        o = AlipaySecurityRiskReconfirmRiskidentifyCertifyModel()
        if 'account' in d:
            o.account = d['account']
        if 'app_code' in d:
            o.app_code = d['app_code']
        if 'company' in d:
            o.company = d['company']
        if 'extend_param' in d:
            o.extend_param = d['extend_param']
        if 'scene_code' in d:
            o.scene_code = d['scene_code']
        if 'tenant_id_list' in d:
            o.tenant_id_list = d['tenant_id_list']
        if 'um_id' in d:
            o.um_id = d['um_id']
        if 'um_id_token' in d:
            o.um_id_token = d['um_id_token']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


