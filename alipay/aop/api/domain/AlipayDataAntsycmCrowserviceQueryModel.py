#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayDataAntsycmCrowserviceQueryModel(object):

    def __init__(self):
        self._business_code = None
        self._partner_id = None
        self._service_id = None
        self._service_type = None
        self._user_sign = None
        self._user_sign_type = None

    @property
    def business_code(self):
        return self._business_code

    @business_code.setter
    def business_code(self, value):
        self._business_code = value
    @property
    def partner_id(self):
        return self._partner_id

    @partner_id.setter
    def partner_id(self, value):
        self._partner_id = value
    @property
    def service_id(self):
        return self._service_id

    @service_id.setter
    def service_id(self, value):
        self._service_id = value
    @property
    def service_type(self):
        return self._service_type

    @service_type.setter
    def service_type(self, value):
        self._service_type = value
    @property
    def user_sign(self):
        return self._user_sign

    @user_sign.setter
    def user_sign(self, value):
        self._user_sign = value
    @property
    def user_sign_type(self):
        return self._user_sign_type

    @user_sign_type.setter
    def user_sign_type(self, value):
        self._user_sign_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.business_code:
            if hasattr(self.business_code, 'to_alipay_dict'):
                params['business_code'] = self.business_code.to_alipay_dict()
            else:
                params['business_code'] = self.business_code
        if self.partner_id:
            if hasattr(self.partner_id, 'to_alipay_dict'):
                params['partner_id'] = self.partner_id.to_alipay_dict()
            else:
                params['partner_id'] = self.partner_id
        if self.service_id:
            if hasattr(self.service_id, 'to_alipay_dict'):
                params['service_id'] = self.service_id.to_alipay_dict()
            else:
                params['service_id'] = self.service_id
        if self.service_type:
            if hasattr(self.service_type, 'to_alipay_dict'):
                params['service_type'] = self.service_type.to_alipay_dict()
            else:
                params['service_type'] = self.service_type
        if self.user_sign:
            if hasattr(self.user_sign, 'to_alipay_dict'):
                params['user_sign'] = self.user_sign.to_alipay_dict()
            else:
                params['user_sign'] = self.user_sign
        if self.user_sign_type:
            if hasattr(self.user_sign_type, 'to_alipay_dict'):
                params['user_sign_type'] = self.user_sign_type.to_alipay_dict()
            else:
                params['user_sign_type'] = self.user_sign_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayDataAntsycmCrowserviceQueryModel()
        if 'business_code' in d:
            o.business_code = d['business_code']
        if 'partner_id' in d:
            o.partner_id = d['partner_id']
        if 'service_id' in d:
            o.service_id = d['service_id']
        if 'service_type' in d:
            o.service_type = d['service_type']
        if 'user_sign' in d:
            o.user_sign = d['user_sign']
        if 'user_sign_type' in d:
            o.user_sign_type = d['user_sign_type']
        return o


