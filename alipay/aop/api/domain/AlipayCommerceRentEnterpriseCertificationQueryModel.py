#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceRentEnterpriseCertificationQueryModel(object):

    def __init__(self):
        self._open_id = None
        self._partner_id = None
        self._partner_open_id = None
        self._unified_social_credit_code = None
        self._user_id = None

    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def partner_id(self):
        return self._partner_id

    @partner_id.setter
    def partner_id(self, value):
        self._partner_id = value
    @property
    def partner_open_id(self):
        return self._partner_open_id

    @partner_open_id.setter
    def partner_open_id(self, value):
        self._partner_open_id = value
    @property
    def unified_social_credit_code(self):
        return self._unified_social_credit_code

    @unified_social_credit_code.setter
    def unified_social_credit_code(self, value):
        self._unified_social_credit_code = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.partner_id:
            if hasattr(self.partner_id, 'to_alipay_dict'):
                params['partner_id'] = self.partner_id.to_alipay_dict()
            else:
                params['partner_id'] = self.partner_id
        if self.partner_open_id:
            if hasattr(self.partner_open_id, 'to_alipay_dict'):
                params['partner_open_id'] = self.partner_open_id.to_alipay_dict()
            else:
                params['partner_open_id'] = self.partner_open_id
        if self.unified_social_credit_code:
            if hasattr(self.unified_social_credit_code, 'to_alipay_dict'):
                params['unified_social_credit_code'] = self.unified_social_credit_code.to_alipay_dict()
            else:
                params['unified_social_credit_code'] = self.unified_social_credit_code
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
        o = AlipayCommerceRentEnterpriseCertificationQueryModel()
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'partner_id' in d:
            o.partner_id = d['partner_id']
        if 'partner_open_id' in d:
            o.partner_open_id = d['partner_open_id']
        if 'unified_social_credit_code' in d:
            o.unified_social_credit_code = d['unified_social_credit_code']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


