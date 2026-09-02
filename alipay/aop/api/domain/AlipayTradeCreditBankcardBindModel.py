#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayTradeCreditBankcardBindModel(object):

    def __init__(self):
        self._agreement_no = None
        self._biz_type = None
        self._cert_no = None
        self._cert_type = None
        self._need_check = None
        self._out_bind_no = None
        self._real_name = None
        self._redirect_url = None
        self._redirection_data = None

    @property
    def agreement_no(self):
        return self._agreement_no

    @agreement_no.setter
    def agreement_no(self, value):
        self._agreement_no = value
    @property
    def biz_type(self):
        return self._biz_type

    @biz_type.setter
    def biz_type(self, value):
        self._biz_type = value
    @property
    def cert_no(self):
        return self._cert_no

    @cert_no.setter
    def cert_no(self, value):
        self._cert_no = value
    @property
    def cert_type(self):
        return self._cert_type

    @cert_type.setter
    def cert_type(self, value):
        self._cert_type = value
    @property
    def need_check(self):
        return self._need_check

    @need_check.setter
    def need_check(self, value):
        self._need_check = value
    @property
    def out_bind_no(self):
        return self._out_bind_no

    @out_bind_no.setter
    def out_bind_no(self, value):
        self._out_bind_no = value
    @property
    def real_name(self):
        return self._real_name

    @real_name.setter
    def real_name(self, value):
        self._real_name = value
    @property
    def redirect_url(self):
        return self._redirect_url

    @redirect_url.setter
    def redirect_url(self, value):
        self._redirect_url = value
    @property
    def redirection_data(self):
        return self._redirection_data

    @redirection_data.setter
    def redirection_data(self, value):
        self._redirection_data = value


    def to_alipay_dict(self):
        params = dict()
        if self.agreement_no:
            if hasattr(self.agreement_no, 'to_alipay_dict'):
                params['agreement_no'] = self.agreement_no.to_alipay_dict()
            else:
                params['agreement_no'] = self.agreement_no
        if self.biz_type:
            if hasattr(self.biz_type, 'to_alipay_dict'):
                params['biz_type'] = self.biz_type.to_alipay_dict()
            else:
                params['biz_type'] = self.biz_type
        if self.cert_no:
            if hasattr(self.cert_no, 'to_alipay_dict'):
                params['cert_no'] = self.cert_no.to_alipay_dict()
            else:
                params['cert_no'] = self.cert_no
        if self.cert_type:
            if hasattr(self.cert_type, 'to_alipay_dict'):
                params['cert_type'] = self.cert_type.to_alipay_dict()
            else:
                params['cert_type'] = self.cert_type
        if self.need_check:
            if hasattr(self.need_check, 'to_alipay_dict'):
                params['need_check'] = self.need_check.to_alipay_dict()
            else:
                params['need_check'] = self.need_check
        if self.out_bind_no:
            if hasattr(self.out_bind_no, 'to_alipay_dict'):
                params['out_bind_no'] = self.out_bind_no.to_alipay_dict()
            else:
                params['out_bind_no'] = self.out_bind_no
        if self.real_name:
            if hasattr(self.real_name, 'to_alipay_dict'):
                params['real_name'] = self.real_name.to_alipay_dict()
            else:
                params['real_name'] = self.real_name
        if self.redirect_url:
            if hasattr(self.redirect_url, 'to_alipay_dict'):
                params['redirect_url'] = self.redirect_url.to_alipay_dict()
            else:
                params['redirect_url'] = self.redirect_url
        if self.redirection_data:
            if hasattr(self.redirection_data, 'to_alipay_dict'):
                params['redirection_data'] = self.redirection_data.to_alipay_dict()
            else:
                params['redirection_data'] = self.redirection_data
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayTradeCreditBankcardBindModel()
        if 'agreement_no' in d:
            o.agreement_no = d['agreement_no']
        if 'biz_type' in d:
            o.biz_type = d['biz_type']
        if 'cert_no' in d:
            o.cert_no = d['cert_no']
        if 'cert_type' in d:
            o.cert_type = d['cert_type']
        if 'need_check' in d:
            o.need_check = d['need_check']
        if 'out_bind_no' in d:
            o.out_bind_no = d['out_bind_no']
        if 'real_name' in d:
            o.real_name = d['real_name']
        if 'redirect_url' in d:
            o.redirect_url = d['redirect_url']
        if 'redirection_data' in d:
            o.redirection_data = d['redirection_data']
        return o


