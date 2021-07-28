#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AnttechBlockchainDefinCustomerLoginConfirmModel(object):

    def __init__(self):
        self._action = None
        self._biz_product = None
        self._mode = None
        self._password = None
        self._user_name = None
        self._verify_code = None

    @property
    def action(self):
        return self._action

    @action.setter
    def action(self, value):
        self._action = value
    @property
    def biz_product(self):
        return self._biz_product

    @biz_product.setter
    def biz_product(self, value):
        self._biz_product = value
    @property
    def mode(self):
        return self._mode

    @mode.setter
    def mode(self, value):
        self._mode = value
    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        self._password = value
    @property
    def user_name(self):
        return self._user_name

    @user_name.setter
    def user_name(self, value):
        self._user_name = value
    @property
    def verify_code(self):
        return self._verify_code

    @verify_code.setter
    def verify_code(self, value):
        self._verify_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.action:
            if hasattr(self.action, 'to_alipay_dict'):
                params['action'] = self.action.to_alipay_dict()
            else:
                params['action'] = self.action
        if self.biz_product:
            if hasattr(self.biz_product, 'to_alipay_dict'):
                params['biz_product'] = self.biz_product.to_alipay_dict()
            else:
                params['biz_product'] = self.biz_product
        if self.mode:
            if hasattr(self.mode, 'to_alipay_dict'):
                params['mode'] = self.mode.to_alipay_dict()
            else:
                params['mode'] = self.mode
        if self.password:
            if hasattr(self.password, 'to_alipay_dict'):
                params['password'] = self.password.to_alipay_dict()
            else:
                params['password'] = self.password
        if self.user_name:
            if hasattr(self.user_name, 'to_alipay_dict'):
                params['user_name'] = self.user_name.to_alipay_dict()
            else:
                params['user_name'] = self.user_name
        if self.verify_code:
            if hasattr(self.verify_code, 'to_alipay_dict'):
                params['verify_code'] = self.verify_code.to_alipay_dict()
            else:
                params['verify_code'] = self.verify_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AnttechBlockchainDefinCustomerLoginConfirmModel()
        if 'action' in d:
            o.action = d['action']
        if 'biz_product' in d:
            o.biz_product = d['biz_product']
        if 'mode' in d:
            o.mode = d['mode']
        if 'password' in d:
            o.password = d['password']
        if 'user_name' in d:
            o.user_name = d['user_name']
        if 'verify_code' in d:
            o.verify_code = d['verify_code']
        return o


