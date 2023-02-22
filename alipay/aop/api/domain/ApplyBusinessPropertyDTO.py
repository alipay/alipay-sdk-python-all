#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.BusinessContactDTO import BusinessContactDTO
from alipay.aop.api.domain.BusinessLicenseDTO import BusinessLicenseDTO
from alipay.aop.api.domain.BusinessSpecialLicenseDTO import BusinessSpecialLicenseDTO
from alipay.aop.api.domain.BusinessWebAppDTO import BusinessWebAppDTO


class ApplyBusinessPropertyDTO(object):

    def __init__(self):
        self._contacts = None
        self._extend = None
        self._license = None
        self._mcc_code = None
        self._mcc_type = None
        self._special_license = None
        self._web_apps = None

    @property
    def contacts(self):
        return self._contacts

    @contacts.setter
    def contacts(self, value):
        if isinstance(value, list):
            self._contacts = list()
            for i in value:
                if isinstance(i, BusinessContactDTO):
                    self._contacts.append(i)
                else:
                    self._contacts.append(BusinessContactDTO.from_alipay_dict(i))
    @property
    def extend(self):
        return self._extend

    @extend.setter
    def extend(self, value):
        self._extend = value
    @property
    def license(self):
        return self._license

    @license.setter
    def license(self, value):
        if isinstance(value, BusinessLicenseDTO):
            self._license = value
        else:
            self._license = BusinessLicenseDTO.from_alipay_dict(value)
    @property
    def mcc_code(self):
        return self._mcc_code

    @mcc_code.setter
    def mcc_code(self, value):
        self._mcc_code = value
    @property
    def mcc_type(self):
        return self._mcc_type

    @mcc_type.setter
    def mcc_type(self, value):
        self._mcc_type = value
    @property
    def special_license(self):
        return self._special_license

    @special_license.setter
    def special_license(self, value):
        if isinstance(value, list):
            self._special_license = list()
            for i in value:
                if isinstance(i, BusinessSpecialLicenseDTO):
                    self._special_license.append(i)
                else:
                    self._special_license.append(BusinessSpecialLicenseDTO.from_alipay_dict(i))
    @property
    def web_apps(self):
        return self._web_apps

    @web_apps.setter
    def web_apps(self, value):
        if isinstance(value, list):
            self._web_apps = list()
            for i in value:
                if isinstance(i, BusinessWebAppDTO):
                    self._web_apps.append(i)
                else:
                    self._web_apps.append(BusinessWebAppDTO.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.contacts:
            if isinstance(self.contacts, list):
                for i in range(0, len(self.contacts)):
                    element = self.contacts[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.contacts[i] = element.to_alipay_dict()
            if hasattr(self.contacts, 'to_alipay_dict'):
                params['contacts'] = self.contacts.to_alipay_dict()
            else:
                params['contacts'] = self.contacts
        if self.extend:
            if hasattr(self.extend, 'to_alipay_dict'):
                params['extend'] = self.extend.to_alipay_dict()
            else:
                params['extend'] = self.extend
        if self.license:
            if hasattr(self.license, 'to_alipay_dict'):
                params['license'] = self.license.to_alipay_dict()
            else:
                params['license'] = self.license
        if self.mcc_code:
            if hasattr(self.mcc_code, 'to_alipay_dict'):
                params['mcc_code'] = self.mcc_code.to_alipay_dict()
            else:
                params['mcc_code'] = self.mcc_code
        if self.mcc_type:
            if hasattr(self.mcc_type, 'to_alipay_dict'):
                params['mcc_type'] = self.mcc_type.to_alipay_dict()
            else:
                params['mcc_type'] = self.mcc_type
        if self.special_license:
            if isinstance(self.special_license, list):
                for i in range(0, len(self.special_license)):
                    element = self.special_license[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.special_license[i] = element.to_alipay_dict()
            if hasattr(self.special_license, 'to_alipay_dict'):
                params['special_license'] = self.special_license.to_alipay_dict()
            else:
                params['special_license'] = self.special_license
        if self.web_apps:
            if isinstance(self.web_apps, list):
                for i in range(0, len(self.web_apps)):
                    element = self.web_apps[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.web_apps[i] = element.to_alipay_dict()
            if hasattr(self.web_apps, 'to_alipay_dict'):
                params['web_apps'] = self.web_apps.to_alipay_dict()
            else:
                params['web_apps'] = self.web_apps
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ApplyBusinessPropertyDTO()
        if 'contacts' in d:
            o.contacts = d['contacts']
        if 'extend' in d:
            o.extend = d['extend']
        if 'license' in d:
            o.license = d['license']
        if 'mcc_code' in d:
            o.mcc_code = d['mcc_code']
        if 'mcc_type' in d:
            o.mcc_type = d['mcc_type']
        if 'special_license' in d:
            o.special_license = d['special_license']
        if 'web_apps' in d:
            o.web_apps = d['web_apps']
        return o


