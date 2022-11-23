#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ActivityGoods import ActivityGoods


class AlipayBossCommMsgtoCeBindModel(object):

    def __init__(self):
        self._business_scope = None
        self._cert_no = None
        self._hascode = None
        self._mobile = None
        self._province_code = None
        self._user_name = None

    @property
    def business_scope(self):
        return self._business_scope

    @business_scope.setter
    def business_scope(self, value):
        self._business_scope = value
    @property
    def cert_no(self):
        return self._cert_no

    @cert_no.setter
    def cert_no(self, value):
        if isinstance(value, ActivityGoods):
            self._cert_no = value
        else:
            self._cert_no = ActivityGoods.from_alipay_dict(value)
    @property
    def hascode(self):
        return self._hascode

    @hascode.setter
    def hascode(self, value):
        self._hascode = value
    @property
    def mobile(self):
        return self._mobile

    @mobile.setter
    def mobile(self, value):
        self._mobile = value
    @property
    def province_code(self):
        return self._province_code

    @province_code.setter
    def province_code(self, value):
        self._province_code = value
    @property
    def user_name(self):
        return self._user_name

    @user_name.setter
    def user_name(self, value):
        if isinstance(value, list):
            self._user_name = list()
            for i in value:
                self._user_name.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.business_scope:
            if hasattr(self.business_scope, 'to_alipay_dict'):
                params['business_scope'] = self.business_scope.to_alipay_dict()
            else:
                params['business_scope'] = self.business_scope
        if self.cert_no:
            if hasattr(self.cert_no, 'to_alipay_dict'):
                params['cert_no'] = self.cert_no.to_alipay_dict()
            else:
                params['cert_no'] = self.cert_no
        if self.hascode:
            if hasattr(self.hascode, 'to_alipay_dict'):
                params['hascode'] = self.hascode.to_alipay_dict()
            else:
                params['hascode'] = self.hascode
        if self.mobile:
            if hasattr(self.mobile, 'to_alipay_dict'):
                params['mobile'] = self.mobile.to_alipay_dict()
            else:
                params['mobile'] = self.mobile
        if self.province_code:
            if hasattr(self.province_code, 'to_alipay_dict'):
                params['province_code'] = self.province_code.to_alipay_dict()
            else:
                params['province_code'] = self.province_code
        if self.user_name:
            if isinstance(self.user_name, list):
                for i in range(0, len(self.user_name)):
                    element = self.user_name[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.user_name[i] = element.to_alipay_dict()
            if hasattr(self.user_name, 'to_alipay_dict'):
                params['user_name'] = self.user_name.to_alipay_dict()
            else:
                params['user_name'] = self.user_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayBossCommMsgtoCeBindModel()
        if 'business_scope' in d:
            o.business_scope = d['business_scope']
        if 'cert_no' in d:
            o.cert_no = d['cert_no']
        if 'hascode' in d:
            o.hascode = d['hascode']
        if 'mobile' in d:
            o.mobile = d['mobile']
        if 'province_code' in d:
            o.province_code = d['province_code']
        if 'user_name' in d:
            o.user_name = d['user_name']
        return o


