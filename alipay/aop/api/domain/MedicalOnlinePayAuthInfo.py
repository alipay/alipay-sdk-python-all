#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MedicalOnlinePayAuthInfo(object):

    def __init__(self):
        self._auth_no = None
        self._auth_stas = None
        self._auth_time = None
        self._auth_url = None
        self._chnl_sign_data = None
        self._oc_token = None
        self._org_sign_data = None
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
    def chnl_sign_data(self):
        return self._chnl_sign_data

    @chnl_sign_data.setter
    def chnl_sign_data(self, value):
        self._chnl_sign_data = value
    @property
    def oc_token(self):
        return self._oc_token

    @oc_token.setter
    def oc_token(self, value):
        self._oc_token = value
    @property
    def org_sign_data(self):
        return self._org_sign_data

    @org_sign_data.setter
    def org_sign_data(self, value):
        self._org_sign_data = value
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
        if self.chnl_sign_data:
            if hasattr(self.chnl_sign_data, 'to_alipay_dict'):
                params['chnl_sign_data'] = self.chnl_sign_data.to_alipay_dict()
            else:
                params['chnl_sign_data'] = self.chnl_sign_data
        if self.oc_token:
            if hasattr(self.oc_token, 'to_alipay_dict'):
                params['oc_token'] = self.oc_token.to_alipay_dict()
            else:
                params['oc_token'] = self.oc_token
        if self.org_sign_data:
            if hasattr(self.org_sign_data, 'to_alipay_dict'):
                params['org_sign_data'] = self.org_sign_data.to_alipay_dict()
            else:
                params['org_sign_data'] = self.org_sign_data
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
        o = MedicalOnlinePayAuthInfo()
        if 'auth_no' in d:
            o.auth_no = d['auth_no']
        if 'auth_stas' in d:
            o.auth_stas = d['auth_stas']
        if 'auth_time' in d:
            o.auth_time = d['auth_time']
        if 'auth_url' in d:
            o.auth_url = d['auth_url']
        if 'chnl_sign_data' in d:
            o.chnl_sign_data = d['chnl_sign_data']
        if 'oc_token' in d:
            o.oc_token = d['oc_token']
        if 'org_sign_data' in d:
            o.org_sign_data = d['org_sign_data']
        if 'req_biz_no' in d:
            o.req_biz_no = d['req_biz_no']
        return o


