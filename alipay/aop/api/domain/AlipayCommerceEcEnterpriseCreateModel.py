#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceEcEnterpriseCreateModel(object):

    def __init__(self):
        self._biz_scene = None
        self._create_fund_account = None
        self._create_iot_group = None
        self._enterprise_alias = None
        self._enterprise_name = None
        self._identity = None
        self._identity_name = None
        self._identity_open_id = None
        self._identity_type = None
        self._out_biz_no = None
        self._sign_return_url = None
        self._sign_terminal = None

    @property
    def biz_scene(self):
        return self._biz_scene

    @biz_scene.setter
    def biz_scene(self, value):
        self._biz_scene = value
    @property
    def create_fund_account(self):
        return self._create_fund_account

    @create_fund_account.setter
    def create_fund_account(self, value):
        self._create_fund_account = value
    @property
    def create_iot_group(self):
        return self._create_iot_group

    @create_iot_group.setter
    def create_iot_group(self, value):
        self._create_iot_group = value
    @property
    def enterprise_alias(self):
        return self._enterprise_alias

    @enterprise_alias.setter
    def enterprise_alias(self, value):
        self._enterprise_alias = value
    @property
    def enterprise_name(self):
        return self._enterprise_name

    @enterprise_name.setter
    def enterprise_name(self, value):
        self._enterprise_name = value
    @property
    def identity(self):
        return self._identity

    @identity.setter
    def identity(self, value):
        self._identity = value
    @property
    def identity_name(self):
        return self._identity_name

    @identity_name.setter
    def identity_name(self, value):
        self._identity_name = value
    @property
    def identity_open_id(self):
        return self._identity_open_id

    @identity_open_id.setter
    def identity_open_id(self, value):
        self._identity_open_id = value
    @property
    def identity_type(self):
        return self._identity_type

    @identity_type.setter
    def identity_type(self, value):
        self._identity_type = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def sign_return_url(self):
        return self._sign_return_url

    @sign_return_url.setter
    def sign_return_url(self, value):
        self._sign_return_url = value
    @property
    def sign_terminal(self):
        return self._sign_terminal

    @sign_terminal.setter
    def sign_terminal(self, value):
        self._sign_terminal = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_scene:
            if hasattr(self.biz_scene, 'to_alipay_dict'):
                params['biz_scene'] = self.biz_scene.to_alipay_dict()
            else:
                params['biz_scene'] = self.biz_scene
        if self.create_fund_account:
            if hasattr(self.create_fund_account, 'to_alipay_dict'):
                params['create_fund_account'] = self.create_fund_account.to_alipay_dict()
            else:
                params['create_fund_account'] = self.create_fund_account
        if self.create_iot_group:
            if hasattr(self.create_iot_group, 'to_alipay_dict'):
                params['create_iot_group'] = self.create_iot_group.to_alipay_dict()
            else:
                params['create_iot_group'] = self.create_iot_group
        if self.enterprise_alias:
            if hasattr(self.enterprise_alias, 'to_alipay_dict'):
                params['enterprise_alias'] = self.enterprise_alias.to_alipay_dict()
            else:
                params['enterprise_alias'] = self.enterprise_alias
        if self.enterprise_name:
            if hasattr(self.enterprise_name, 'to_alipay_dict'):
                params['enterprise_name'] = self.enterprise_name.to_alipay_dict()
            else:
                params['enterprise_name'] = self.enterprise_name
        if self.identity:
            if hasattr(self.identity, 'to_alipay_dict'):
                params['identity'] = self.identity.to_alipay_dict()
            else:
                params['identity'] = self.identity
        if self.identity_name:
            if hasattr(self.identity_name, 'to_alipay_dict'):
                params['identity_name'] = self.identity_name.to_alipay_dict()
            else:
                params['identity_name'] = self.identity_name
        if self.identity_open_id:
            if hasattr(self.identity_open_id, 'to_alipay_dict'):
                params['identity_open_id'] = self.identity_open_id.to_alipay_dict()
            else:
                params['identity_open_id'] = self.identity_open_id
        if self.identity_type:
            if hasattr(self.identity_type, 'to_alipay_dict'):
                params['identity_type'] = self.identity_type.to_alipay_dict()
            else:
                params['identity_type'] = self.identity_type
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.sign_return_url:
            if hasattr(self.sign_return_url, 'to_alipay_dict'):
                params['sign_return_url'] = self.sign_return_url.to_alipay_dict()
            else:
                params['sign_return_url'] = self.sign_return_url
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
        o = AlipayCommerceEcEnterpriseCreateModel()
        if 'biz_scene' in d:
            o.biz_scene = d['biz_scene']
        if 'create_fund_account' in d:
            o.create_fund_account = d['create_fund_account']
        if 'create_iot_group' in d:
            o.create_iot_group = d['create_iot_group']
        if 'enterprise_alias' in d:
            o.enterprise_alias = d['enterprise_alias']
        if 'enterprise_name' in d:
            o.enterprise_name = d['enterprise_name']
        if 'identity' in d:
            o.identity = d['identity']
        if 'identity_name' in d:
            o.identity_name = d['identity_name']
        if 'identity_open_id' in d:
            o.identity_open_id = d['identity_open_id']
        if 'identity_type' in d:
            o.identity_type = d['identity_type']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'sign_return_url' in d:
            o.sign_return_url = d['sign_return_url']
        if 'sign_terminal' in d:
            o.sign_terminal = d['sign_terminal']
        return o


