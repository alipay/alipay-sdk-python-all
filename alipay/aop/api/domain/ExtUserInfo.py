#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ExtUserInfo(object):

    def __init__(self):
        self._cert_no = None
        self._cert_type = None
        self._fix_buyer = None
        self._min_age = None
        self._mobile = None
        self._name = None
        self._need_check_info = None

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
    def fix_buyer(self):
        return self._fix_buyer

    @fix_buyer.setter
    def fix_buyer(self, value):
        self._fix_buyer = value
    @property
    def min_age(self):
        return self._min_age

    @min_age.setter
    def min_age(self, value):
        self._min_age = value
    @property
    def mobile(self):
        return self._mobile

    @mobile.setter
    def mobile(self, value):
        self._mobile = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def need_check_info(self):
        return self._need_check_info

    @need_check_info.setter
    def need_check_info(self, value):
        self._need_check_info = value


    def to_alipay_dict(self):
        params = dict()
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
        if self.fix_buyer:
            if hasattr(self.fix_buyer, 'to_alipay_dict'):
                params['fix_buyer'] = self.fix_buyer.to_alipay_dict()
            else:
                params['fix_buyer'] = self.fix_buyer
        if self.min_age:
            if hasattr(self.min_age, 'to_alipay_dict'):
                params['min_age'] = self.min_age.to_alipay_dict()
            else:
                params['min_age'] = self.min_age
        if self.mobile:
            if hasattr(self.mobile, 'to_alipay_dict'):
                params['mobile'] = self.mobile.to_alipay_dict()
            else:
                params['mobile'] = self.mobile
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.need_check_info:
            if hasattr(self.need_check_info, 'to_alipay_dict'):
                params['need_check_info'] = self.need_check_info.to_alipay_dict()
            else:
                params['need_check_info'] = self.need_check_info
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ExtUserInfo()
        if 'cert_no' in d:
            o.cert_no = d['cert_no']
        if 'cert_type' in d:
            o.cert_type = d['cert_type']
        if 'fix_buyer' in d:
            o.fix_buyer = d['fix_buyer']
        if 'min_age' in d:
            o.min_age = d['min_age']
        if 'mobile' in d:
            o.mobile = d['mobile']
        if 'name' in d:
            o.name = d['name']
        if 'need_check_info' in d:
            o.need_check_info = d['need_check_info']
        return o


