#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceEcAssetAuthorizeApplyModel(object):

    def __init__(self):
        self._account_id = None
        self._agreement_no = None
        self._asset_type = None
        self._auth_type = None
        self._ebe_alipay_logon_id = None
        self._ent_alipay_logon_id = None
        self._enterprise_id = None
        self._out_biz_no = None
        self._sign_terminal = None

    @property
    def account_id(self):
        return self._account_id

    @account_id.setter
    def account_id(self, value):
        self._account_id = value
    @property
    def agreement_no(self):
        return self._agreement_no

    @agreement_no.setter
    def agreement_no(self, value):
        self._agreement_no = value
    @property
    def asset_type(self):
        return self._asset_type

    @asset_type.setter
    def asset_type(self, value):
        self._asset_type = value
    @property
    def auth_type(self):
        return self._auth_type

    @auth_type.setter
    def auth_type(self, value):
        self._auth_type = value
    @property
    def ebe_alipay_logon_id(self):
        return self._ebe_alipay_logon_id

    @ebe_alipay_logon_id.setter
    def ebe_alipay_logon_id(self, value):
        self._ebe_alipay_logon_id = value
    @property
    def ent_alipay_logon_id(self):
        return self._ent_alipay_logon_id

    @ent_alipay_logon_id.setter
    def ent_alipay_logon_id(self, value):
        self._ent_alipay_logon_id = value
    @property
    def enterprise_id(self):
        return self._enterprise_id

    @enterprise_id.setter
    def enterprise_id(self, value):
        self._enterprise_id = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def sign_terminal(self):
        return self._sign_terminal

    @sign_terminal.setter
    def sign_terminal(self, value):
        self._sign_terminal = value


    def to_alipay_dict(self):
        params = dict()
        if self.account_id:
            if hasattr(self.account_id, 'to_alipay_dict'):
                params['account_id'] = self.account_id.to_alipay_dict()
            else:
                params['account_id'] = self.account_id
        if self.agreement_no:
            if hasattr(self.agreement_no, 'to_alipay_dict'):
                params['agreement_no'] = self.agreement_no.to_alipay_dict()
            else:
                params['agreement_no'] = self.agreement_no
        if self.asset_type:
            if hasattr(self.asset_type, 'to_alipay_dict'):
                params['asset_type'] = self.asset_type.to_alipay_dict()
            else:
                params['asset_type'] = self.asset_type
        if self.auth_type:
            if hasattr(self.auth_type, 'to_alipay_dict'):
                params['auth_type'] = self.auth_type.to_alipay_dict()
            else:
                params['auth_type'] = self.auth_type
        if self.ebe_alipay_logon_id:
            if hasattr(self.ebe_alipay_logon_id, 'to_alipay_dict'):
                params['ebe_alipay_logon_id'] = self.ebe_alipay_logon_id.to_alipay_dict()
            else:
                params['ebe_alipay_logon_id'] = self.ebe_alipay_logon_id
        if self.ent_alipay_logon_id:
            if hasattr(self.ent_alipay_logon_id, 'to_alipay_dict'):
                params['ent_alipay_logon_id'] = self.ent_alipay_logon_id.to_alipay_dict()
            else:
                params['ent_alipay_logon_id'] = self.ent_alipay_logon_id
        if self.enterprise_id:
            if hasattr(self.enterprise_id, 'to_alipay_dict'):
                params['enterprise_id'] = self.enterprise_id.to_alipay_dict()
            else:
                params['enterprise_id'] = self.enterprise_id
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.sign_terminal:
            if hasattr(self.sign_terminal, 'to_alipay_dict'):
                params['sign_terminal'] = self.sign_terminal.to_alipay_dict()
            else:
                params['sign_terminal'] = self.sign_terminal
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceEcAssetAuthorizeApplyModel()
        if 'account_id' in d:
            o.account_id = d['account_id']
        if 'agreement_no' in d:
            o.agreement_no = d['agreement_no']
        if 'asset_type' in d:
            o.asset_type = d['asset_type']
        if 'auth_type' in d:
            o.auth_type = d['auth_type']
        if 'ebe_alipay_logon_id' in d:
            o.ebe_alipay_logon_id = d['ebe_alipay_logon_id']
        if 'ent_alipay_logon_id' in d:
            o.ent_alipay_logon_id = d['ent_alipay_logon_id']
        if 'enterprise_id' in d:
            o.enterprise_id = d['enterprise_id']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'sign_terminal' in d:
            o.sign_terminal = d['sign_terminal']
        return o


