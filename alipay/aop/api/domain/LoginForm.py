#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class LoginForm(object):

    def __init__(self):
        self._captcha = None
        self._id_card_no = None
        self._name = None
        self._phone_no = None
        self._query_password = None
        self._service_password = None
        self._sms_code = None
        self._sms_code_jldx = None

    @property
    def captcha(self):
        return self._captcha

    @captcha.setter
    def captcha(self, value):
        self._captcha = value
    @property
    def id_card_no(self):
        return self._id_card_no

    @id_card_no.setter
    def id_card_no(self, value):
        self._id_card_no = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def phone_no(self):
        return self._phone_no

    @phone_no.setter
    def phone_no(self, value):
        self._phone_no = value
    @property
    def query_password(self):
        return self._query_password

    @query_password.setter
    def query_password(self, value):
        self._query_password = value
    @property
    def service_password(self):
        return self._service_password

    @service_password.setter
    def service_password(self, value):
        self._service_password = value
    @property
    def sms_code(self):
        return self._sms_code

    @sms_code.setter
    def sms_code(self, value):
        self._sms_code = value
    @property
    def sms_code_jldx(self):
        return self._sms_code_jldx

    @sms_code_jldx.setter
    def sms_code_jldx(self, value):
        self._sms_code_jldx = value


    def to_alipay_dict(self):
        params = dict()
        if self.captcha:
            if hasattr(self.captcha, 'to_alipay_dict'):
                params['captcha'] = self.captcha.to_alipay_dict()
            else:
                params['captcha'] = self.captcha
        if self.id_card_no:
            if hasattr(self.id_card_no, 'to_alipay_dict'):
                params['id_card_no'] = self.id_card_no.to_alipay_dict()
            else:
                params['id_card_no'] = self.id_card_no
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.phone_no:
            if hasattr(self.phone_no, 'to_alipay_dict'):
                params['phone_no'] = self.phone_no.to_alipay_dict()
            else:
                params['phone_no'] = self.phone_no
        if self.query_password:
            if hasattr(self.query_password, 'to_alipay_dict'):
                params['query_password'] = self.query_password.to_alipay_dict()
            else:
                params['query_password'] = self.query_password
        if self.service_password:
            if hasattr(self.service_password, 'to_alipay_dict'):
                params['service_password'] = self.service_password.to_alipay_dict()
            else:
                params['service_password'] = self.service_password
        if self.sms_code:
            if hasattr(self.sms_code, 'to_alipay_dict'):
                params['sms_code'] = self.sms_code.to_alipay_dict()
            else:
                params['sms_code'] = self.sms_code
        if self.sms_code_jldx:
            if hasattr(self.sms_code_jldx, 'to_alipay_dict'):
                params['sms_code_jldx'] = self.sms_code_jldx.to_alipay_dict()
            else:
                params['sms_code_jldx'] = self.sms_code_jldx
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = LoginForm()
        if 'captcha' in d:
            o.captcha = d['captcha']
        if 'id_card_no' in d:
            o.id_card_no = d['id_card_no']
        if 'name' in d:
            o.name = d['name']
        if 'phone_no' in d:
            o.phone_no = d['phone_no']
        if 'query_password' in d:
            o.query_password = d['query_password']
        if 'service_password' in d:
            o.service_password = d['service_password']
        if 'sms_code' in d:
            o.sms_code = d['sms_code']
        if 'sms_code_jldx' in d:
            o.sms_code_jldx = d['sms_code_jldx']
        return o


