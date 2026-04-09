#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.BusinessLicenseInfo import BusinessLicenseInfo
from alipay.aop.api.domain.LifeServiceContactInfo import LifeServiceContactInfo
from alipay.aop.api.domain.SpecialLicenseInfo import SpecialLicenseInfo


class AlipayOpenSpInteopLifeserviceCreateModel(object):

    def __init__(self):
        self._business_license_info = None
        self._contact_info = None
        self._inteop_order_no = None
        self._mcc_code = None
        self._special_license_info = None

    @property
    def business_license_info(self):
        return self._business_license_info

    @business_license_info.setter
    def business_license_info(self, value):
        if isinstance(value, BusinessLicenseInfo):
            self._business_license_info = value
        else:
            self._business_license_info = BusinessLicenseInfo.from_alipay_dict(value)
    @property
    def contact_info(self):
        return self._contact_info

    @contact_info.setter
    def contact_info(self, value):
        if isinstance(value, LifeServiceContactInfo):
            self._contact_info = value
        else:
            self._contact_info = LifeServiceContactInfo.from_alipay_dict(value)
    @property
    def inteop_order_no(self):
        return self._inteop_order_no

    @inteop_order_no.setter
    def inteop_order_no(self, value):
        self._inteop_order_no = value
    @property
    def mcc_code(self):
        return self._mcc_code

    @mcc_code.setter
    def mcc_code(self, value):
        self._mcc_code = value
    @property
    def special_license_info(self):
        return self._special_license_info

    @special_license_info.setter
    def special_license_info(self, value):
        if isinstance(value, list):
            self._special_license_info = list()
            for i in value:
                if isinstance(i, SpecialLicenseInfo):
                    self._special_license_info.append(i)
                else:
                    self._special_license_info.append(SpecialLicenseInfo.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.business_license_info:
            if hasattr(self.business_license_info, 'to_alipay_dict'):
                params['business_license_info'] = self.business_license_info.to_alipay_dict()
            else:
                params['business_license_info'] = self.business_license_info
        if self.contact_info:
            if hasattr(self.contact_info, 'to_alipay_dict'):
                params['contact_info'] = self.contact_info.to_alipay_dict()
            else:
                params['contact_info'] = self.contact_info
        if self.inteop_order_no:
            if hasattr(self.inteop_order_no, 'to_alipay_dict'):
                params['inteop_order_no'] = self.inteop_order_no.to_alipay_dict()
            else:
                params['inteop_order_no'] = self.inteop_order_no
        if self.mcc_code:
            if hasattr(self.mcc_code, 'to_alipay_dict'):
                params['mcc_code'] = self.mcc_code.to_alipay_dict()
            else:
                params['mcc_code'] = self.mcc_code
        if self.special_license_info:
            if isinstance(self.special_license_info, list):
                for i in range(0, len(self.special_license_info)):
                    element = self.special_license_info[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.special_license_info[i] = element.to_alipay_dict()
            if hasattr(self.special_license_info, 'to_alipay_dict'):
                params['special_license_info'] = self.special_license_info.to_alipay_dict()
            else:
                params['special_license_info'] = self.special_license_info
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenSpInteopLifeserviceCreateModel()
        if 'business_license_info' in d:
            o.business_license_info = d['business_license_info']
        if 'contact_info' in d:
            o.contact_info = d['contact_info']
        if 'inteop_order_no' in d:
            o.inteop_order_no = d['inteop_order_no']
        if 'mcc_code' in d:
            o.mcc_code = d['mcc_code']
        if 'special_license_info' in d:
            o.special_license_info = d['special_license_info']
        return o


