#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MedicalNationalPayAuthInfo(object):

    def __init__(self):
        self._auth_no = None
        self._auth_stas = None
        self._auth_time = None
        self._auth_url = None
        self._medical_card_id = None
        self._medical_card_inst_id = None
        self._openapi_app_id = None
        self._pay_auth_no = None
        self._req_biz_no = None

    @property
    def auth_no(self):
        return self._auth_no

    @auth_no.setter
    def auth_no(self, value):
        self._auth_no = value
    @property
    def auth_stas(self):
        return self._auth_stas

    @auth_stas.setter
    def auth_stas(self, value):
        self._auth_stas = value
    @property
    def auth_time(self):
        return self._auth_time

    @auth_time.setter
    def auth_time(self, value):
        self._auth_time = value
    @property
    def auth_url(self):
        return self._auth_url

    @auth_url.setter
    def auth_url(self, value):
        self._auth_url = value
    @property
    def medical_card_id(self):
        return self._medical_card_id

    @medical_card_id.setter
    def medical_card_id(self, value):
        self._medical_card_id = value
    @property
    def medical_card_inst_id(self):
        return self._medical_card_inst_id

    @medical_card_inst_id.setter
    def medical_card_inst_id(self, value):
        self._medical_card_inst_id = value
    @property
    def openapi_app_id(self):
        return self._openapi_app_id

    @openapi_app_id.setter
    def openapi_app_id(self, value):
        self._openapi_app_id = value
    @property
    def pay_auth_no(self):
        return self._pay_auth_no

    @pay_auth_no.setter
    def pay_auth_no(self, value):
        self._pay_auth_no = value
    @property
    def req_biz_no(self):
        return self._req_biz_no

    @req_biz_no.setter
    def req_biz_no(self, value):
        self._req_biz_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.auth_no:
            if hasattr(self.auth_no, 'to_alipay_dict'):
                params['auth_no'] = self.auth_no.to_alipay_dict()
            else:
                params['auth_no'] = self.auth_no
        if self.auth_stas:
            if hasattr(self.auth_stas, 'to_alipay_dict'):
                params['auth_stas'] = self.auth_stas.to_alipay_dict()
            else:
                params['auth_stas'] = self.auth_stas
        if self.auth_time:
            if hasattr(self.auth_time, 'to_alipay_dict'):
                params['auth_time'] = self.auth_time.to_alipay_dict()
            else:
                params['auth_time'] = self.auth_time
        if self.auth_url:
            if hasattr(self.auth_url, 'to_alipay_dict'):
                params['auth_url'] = self.auth_url.to_alipay_dict()
            else:
                params['auth_url'] = self.auth_url
        if self.medical_card_id:
            if hasattr(self.medical_card_id, 'to_alipay_dict'):
                params['medical_card_id'] = self.medical_card_id.to_alipay_dict()
            else:
                params['medical_card_id'] = self.medical_card_id
        if self.medical_card_inst_id:
            if hasattr(self.medical_card_inst_id, 'to_alipay_dict'):
                params['medical_card_inst_id'] = self.medical_card_inst_id.to_alipay_dict()
            else:
                params['medical_card_inst_id'] = self.medical_card_inst_id
        if self.openapi_app_id:
            if hasattr(self.openapi_app_id, 'to_alipay_dict'):
                params['openapi_app_id'] = self.openapi_app_id.to_alipay_dict()
            else:
                params['openapi_app_id'] = self.openapi_app_id
        if self.pay_auth_no:
            if hasattr(self.pay_auth_no, 'to_alipay_dict'):
                params['pay_auth_no'] = self.pay_auth_no.to_alipay_dict()
            else:
                params['pay_auth_no'] = self.pay_auth_no
        if self.req_biz_no:
            if hasattr(self.req_biz_no, 'to_alipay_dict'):
                params['req_biz_no'] = self.req_biz_no.to_alipay_dict()
            else:
                params['req_biz_no'] = self.req_biz_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MedicalNationalPayAuthInfo()
        if 'auth_no' in d:
            o.auth_no = d['auth_no']
        if 'auth_stas' in d:
            o.auth_stas = d['auth_stas']
        if 'auth_time' in d:
            o.auth_time = d['auth_time']
        if 'auth_url' in d:
            o.auth_url = d['auth_url']
        if 'medical_card_id' in d:
            o.medical_card_id = d['medical_card_id']
        if 'medical_card_inst_id' in d:
            o.medical_card_inst_id = d['medical_card_inst_id']
        if 'openapi_app_id' in d:
            o.openapi_app_id = d['openapi_app_id']
        if 'pay_auth_no' in d:
            o.pay_auth_no = d['pay_auth_no']
        if 'req_biz_no' in d:
            o.req_biz_no = d['req_biz_no']
        return o


