#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.CommonMerchantLicense import CommonMerchantLicense


class SettleInMerchantLicense(object):

    def __init__(self):
        self._common_merchant_licenses = None
        self._mcc_code = None
        self._name = None
        self._phone = None

    @property
    def common_merchant_licenses(self):
        return self._common_merchant_licenses

    @common_merchant_licenses.setter
    def common_merchant_licenses(self, value):
        if isinstance(value, list):
            self._common_merchant_licenses = list()
            for i in value:
                if isinstance(i, CommonMerchantLicense):
                    self._common_merchant_licenses.append(i)
                else:
                    self._common_merchant_licenses.append(CommonMerchantLicense.from_alipay_dict(i))
    @property
    def mcc_code(self):
        return self._mcc_code

    @mcc_code.setter
    def mcc_code(self, value):
        self._mcc_code = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, value):
        self._phone = value


    def to_alipay_dict(self):
        params = dict()
        if self.common_merchant_licenses:
            if isinstance(self.common_merchant_licenses, list):
                for i in range(0, len(self.common_merchant_licenses)):
                    element = self.common_merchant_licenses[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.common_merchant_licenses[i] = element.to_alipay_dict()
            if hasattr(self.common_merchant_licenses, 'to_alipay_dict'):
                params['common_merchant_licenses'] = self.common_merchant_licenses.to_alipay_dict()
            else:
                params['common_merchant_licenses'] = self.common_merchant_licenses
        if self.mcc_code:
            if hasattr(self.mcc_code, 'to_alipay_dict'):
                params['mcc_code'] = self.mcc_code.to_alipay_dict()
            else:
                params['mcc_code'] = self.mcc_code
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.phone:
            if hasattr(self.phone, 'to_alipay_dict'):
                params['phone'] = self.phone.to_alipay_dict()
            else:
                params['phone'] = self.phone
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SettleInMerchantLicense()
        if 'common_merchant_licenses' in d:
            o.common_merchant_licenses = d['common_merchant_licenses']
        if 'mcc_code' in d:
            o.mcc_code = d['mcc_code']
        if 'name' in d:
            o.name = d['name']
        if 'phone' in d:
            o.phone = d['phone']
        return o


