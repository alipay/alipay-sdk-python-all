#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayFinancialnetAuthSpaccountConsultModel(object):

    def __init__(self):
        self._biz_identity = None
        self._sign_product_id = None
        self._user_id = None

    @property
    def biz_identity(self):
        return self._biz_identity

    @biz_identity.setter
    def biz_identity(self, value):
        self._biz_identity = value
    @property
    def sign_product_id(self):
        return self._sign_product_id

    @sign_product_id.setter
    def sign_product_id(self, value):
        self._sign_product_id = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_identity:
            if hasattr(self.biz_identity, 'to_alipay_dict'):
                params['biz_identity'] = self.biz_identity.to_alipay_dict()
            else:
                params['biz_identity'] = self.biz_identity
        if self.sign_product_id:
            if hasattr(self.sign_product_id, 'to_alipay_dict'):
                params['sign_product_id'] = self.sign_product_id.to_alipay_dict()
            else:
                params['sign_product_id'] = self.sign_product_id
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
        o = AlipayFinancialnetAuthSpaccountConsultModel()
        if 'biz_identity' in d:
            o.biz_identity = d['biz_identity']
        if 'sign_product_id' in d:
            o.sign_product_id = d['sign_product_id']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


