#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RecommendBankInfo(object):

    def __init__(self):
        self._android_package_name = None
        self._android_schema = None
        self._bank_code = None
        self._bank_icon_url = None
        self._bank_name = None
        self._enable = None
        self._ios_schema = None
        self._memo = None

    @property
    def android_package_name(self):
        return self._android_package_name

    @android_package_name.setter
    def android_package_name(self, value):
        self._android_package_name = value
    @property
    def android_schema(self):
        return self._android_schema

    @android_schema.setter
    def android_schema(self, value):
        self._android_schema = value
    @property
    def bank_code(self):
        return self._bank_code

    @bank_code.setter
    def bank_code(self, value):
        self._bank_code = value
    @property
    def bank_icon_url(self):
        return self._bank_icon_url

    @bank_icon_url.setter
    def bank_icon_url(self, value):
        self._bank_icon_url = value
    @property
    def bank_name(self):
        return self._bank_name

    @bank_name.setter
    def bank_name(self, value):
        self._bank_name = value
    @property
    def enable(self):
        return self._enable

    @enable.setter
    def enable(self, value):
        self._enable = value
    @property
    def ios_schema(self):
        return self._ios_schema

    @ios_schema.setter
    def ios_schema(self, value):
        self._ios_schema = value
    @property
    def memo(self):
        return self._memo

    @memo.setter
    def memo(self, value):
        self._memo = value


    def to_alipay_dict(self):
        params = dict()
        if self.android_package_name:
            if hasattr(self.android_package_name, 'to_alipay_dict'):
                params['android_package_name'] = self.android_package_name.to_alipay_dict()
            else:
                params['android_package_name'] = self.android_package_name
        if self.android_schema:
            if hasattr(self.android_schema, 'to_alipay_dict'):
                params['android_schema'] = self.android_schema.to_alipay_dict()
            else:
                params['android_schema'] = self.android_schema
        if self.bank_code:
            if hasattr(self.bank_code, 'to_alipay_dict'):
                params['bank_code'] = self.bank_code.to_alipay_dict()
            else:
                params['bank_code'] = self.bank_code
        if self.bank_icon_url:
            if hasattr(self.bank_icon_url, 'to_alipay_dict'):
                params['bank_icon_url'] = self.bank_icon_url.to_alipay_dict()
            else:
                params['bank_icon_url'] = self.bank_icon_url
        if self.bank_name:
            if hasattr(self.bank_name, 'to_alipay_dict'):
                params['bank_name'] = self.bank_name.to_alipay_dict()
            else:
                params['bank_name'] = self.bank_name
        if self.enable:
            if hasattr(self.enable, 'to_alipay_dict'):
                params['enable'] = self.enable.to_alipay_dict()
            else:
                params['enable'] = self.enable
        if self.ios_schema:
            if hasattr(self.ios_schema, 'to_alipay_dict'):
                params['ios_schema'] = self.ios_schema.to_alipay_dict()
            else:
                params['ios_schema'] = self.ios_schema
        if self.memo:
            if hasattr(self.memo, 'to_alipay_dict'):
                params['memo'] = self.memo.to_alipay_dict()
            else:
                params['memo'] = self.memo
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RecommendBankInfo()
        if 'android_package_name' in d:
            o.android_package_name = d['android_package_name']
        if 'android_schema' in d:
            o.android_schema = d['android_schema']
        if 'bank_code' in d:
            o.bank_code = d['bank_code']
        if 'bank_icon_url' in d:
            o.bank_icon_url = d['bank_icon_url']
        if 'bank_name' in d:
            o.bank_name = d['bank_name']
        if 'enable' in d:
            o.enable = d['enable']
        if 'ios_schema' in d:
            o.ios_schema = d['ios_schema']
        if 'memo' in d:
            o.memo = d['memo']
        return o


