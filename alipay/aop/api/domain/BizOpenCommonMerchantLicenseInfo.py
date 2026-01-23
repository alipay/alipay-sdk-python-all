#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class BizOpenCommonMerchantLicenseInfo(object):

    def __init__(self):
        self._business_scope = None
        self._cert_no = None
        self._effective_date = None
        self._license_name = None
        self._license_pics = None
        self._reg_capital = None
        self._type = None

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
        self._cert_no = value
    @property
    def effective_date(self):
        return self._effective_date

    @effective_date.setter
    def effective_date(self, value):
        self._effective_date = value
    @property
    def license_name(self):
        return self._license_name

    @license_name.setter
    def license_name(self, value):
        self._license_name = value
    @property
    def license_pics(self):
        return self._license_pics

    @license_pics.setter
    def license_pics(self, value):
        if isinstance(value, list):
            self._license_pics = list()
            for i in value:
                self._license_pics.append(i)
    @property
    def reg_capital(self):
        return self._reg_capital

    @reg_capital.setter
    def reg_capital(self, value):
        self._reg_capital = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value


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
        if self.effective_date:
            if hasattr(self.effective_date, 'to_alipay_dict'):
                params['effective_date'] = self.effective_date.to_alipay_dict()
            else:
                params['effective_date'] = self.effective_date
        if self.license_name:
            if hasattr(self.license_name, 'to_alipay_dict'):
                params['license_name'] = self.license_name.to_alipay_dict()
            else:
                params['license_name'] = self.license_name
        if self.license_pics:
            if isinstance(self.license_pics, list):
                for i in range(0, len(self.license_pics)):
                    element = self.license_pics[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.license_pics[i] = element.to_alipay_dict()
            if hasattr(self.license_pics, 'to_alipay_dict'):
                params['license_pics'] = self.license_pics.to_alipay_dict()
            else:
                params['license_pics'] = self.license_pics
        if self.reg_capital:
            if hasattr(self.reg_capital, 'to_alipay_dict'):
                params['reg_capital'] = self.reg_capital.to_alipay_dict()
            else:
                params['reg_capital'] = self.reg_capital
        if self.type:
            if hasattr(self.type, 'to_alipay_dict'):
                params['type'] = self.type.to_alipay_dict()
            else:
                params['type'] = self.type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = BizOpenCommonMerchantLicenseInfo()
        if 'business_scope' in d:
            o.business_scope = d['business_scope']
        if 'cert_no' in d:
            o.cert_no = d['cert_no']
        if 'effective_date' in d:
            o.effective_date = d['effective_date']
        if 'license_name' in d:
            o.license_name = d['license_name']
        if 'license_pics' in d:
            o.license_pics = d['license_pics']
        if 'reg_capital' in d:
            o.reg_capital = d['reg_capital']
        if 'type' in d:
            o.type = d['type']
        return o


