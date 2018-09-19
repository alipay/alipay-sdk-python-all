#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ContactPersonInfo import ContactPersonInfo


class BaseInfo(object):

    def __init__(self):
        self._alipay_fuwu_name = None
        self._app_name = None
        self._contact_info = None
        self._logo_pic = None
        self._mcc_code = None
        self._short_name = None
        self._special_license_pic = None
        self._usage_scenario = None
        self._web_address = None
        self._web_auth_pic = None
        self._weixin_public_name = None

    @property
    def alipay_fuwu_name(self):
        return self._alipay_fuwu_name

    @alipay_fuwu_name.setter
    def alipay_fuwu_name(self, value):
        self._alipay_fuwu_name = value
    @property
    def app_name(self):
        return self._app_name

    @app_name.setter
    def app_name(self, value):
        self._app_name = value
    @property
    def contact_info(self):
        return self._contact_info

    @contact_info.setter
    def contact_info(self, value):
        if isinstance(value, list):
            self._contact_info = list()
            for i in value:
                if isinstance(i, ContactPersonInfo):
                    self._contact_info.append(i)
                else:
                    self._contact_info.append(ContactPersonInfo.from_alipay_dict(i))
    @property
    def logo_pic(self):
        return self._logo_pic

    @logo_pic.setter
    def logo_pic(self, value):
        self._logo_pic = value
    @property
    def mcc_code(self):
        return self._mcc_code

    @mcc_code.setter
    def mcc_code(self, value):
        self._mcc_code = value
    @property
    def short_name(self):
        return self._short_name

    @short_name.setter
    def short_name(self, value):
        self._short_name = value
    @property
    def special_license_pic(self):
        return self._special_license_pic

    @special_license_pic.setter
    def special_license_pic(self, value):
        if isinstance(value, list):
            self._special_license_pic = list()
            for i in value:
                self._special_license_pic.append(i)
    @property
    def usage_scenario(self):
        return self._usage_scenario

    @usage_scenario.setter
    def usage_scenario(self, value):
        self._usage_scenario = value
    @property
    def web_address(self):
        return self._web_address

    @web_address.setter
    def web_address(self, value):
        if isinstance(value, list):
            self._web_address = list()
            for i in value:
                self._web_address.append(i)
    @property
    def web_auth_pic(self):
        return self._web_auth_pic

    @web_auth_pic.setter
    def web_auth_pic(self, value):
        self._web_auth_pic = value
    @property
    def weixin_public_name(self):
        return self._weixin_public_name

    @weixin_public_name.setter
    def weixin_public_name(self, value):
        self._weixin_public_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.alipay_fuwu_name:
            if hasattr(self.alipay_fuwu_name, 'to_alipay_dict'):
                params['alipay_fuwu_name'] = self.alipay_fuwu_name.to_alipay_dict()
            else:
                params['alipay_fuwu_name'] = self.alipay_fuwu_name
        if self.app_name:
            if hasattr(self.app_name, 'to_alipay_dict'):
                params['app_name'] = self.app_name.to_alipay_dict()
            else:
                params['app_name'] = self.app_name
        if self.contact_info:
            if isinstance(self.contact_info, list):
                for i in range(0, len(self.contact_info)):
                    element = self.contact_info[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.contact_info[i] = element.to_alipay_dict()
            if hasattr(self.contact_info, 'to_alipay_dict'):
                params['contact_info'] = self.contact_info.to_alipay_dict()
            else:
                params['contact_info'] = self.contact_info
        if self.logo_pic:
            if hasattr(self.logo_pic, 'to_alipay_dict'):
                params['logo_pic'] = self.logo_pic.to_alipay_dict()
            else:
                params['logo_pic'] = self.logo_pic
        if self.mcc_code:
            if hasattr(self.mcc_code, 'to_alipay_dict'):
                params['mcc_code'] = self.mcc_code.to_alipay_dict()
            else:
                params['mcc_code'] = self.mcc_code
        if self.short_name:
            if hasattr(self.short_name, 'to_alipay_dict'):
                params['short_name'] = self.short_name.to_alipay_dict()
            else:
                params['short_name'] = self.short_name
        if self.special_license_pic:
            if isinstance(self.special_license_pic, list):
                for i in range(0, len(self.special_license_pic)):
                    element = self.special_license_pic[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.special_license_pic[i] = element.to_alipay_dict()
            if hasattr(self.special_license_pic, 'to_alipay_dict'):
                params['special_license_pic'] = self.special_license_pic.to_alipay_dict()
            else:
                params['special_license_pic'] = self.special_license_pic
        if self.usage_scenario:
            if hasattr(self.usage_scenario, 'to_alipay_dict'):
                params['usage_scenario'] = self.usage_scenario.to_alipay_dict()
            else:
                params['usage_scenario'] = self.usage_scenario
        if self.web_address:
            if isinstance(self.web_address, list):
                for i in range(0, len(self.web_address)):
                    element = self.web_address[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.web_address[i] = element.to_alipay_dict()
            if hasattr(self.web_address, 'to_alipay_dict'):
                params['web_address'] = self.web_address.to_alipay_dict()
            else:
                params['web_address'] = self.web_address
        if self.web_auth_pic:
            if hasattr(self.web_auth_pic, 'to_alipay_dict'):
                params['web_auth_pic'] = self.web_auth_pic.to_alipay_dict()
            else:
                params['web_auth_pic'] = self.web_auth_pic
        if self.weixin_public_name:
            if hasattr(self.weixin_public_name, 'to_alipay_dict'):
                params['weixin_public_name'] = self.weixin_public_name.to_alipay_dict()
            else:
                params['weixin_public_name'] = self.weixin_public_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = BaseInfo()
        if 'alipay_fuwu_name' in d:
            o.alipay_fuwu_name = d['alipay_fuwu_name']
        if 'app_name' in d:
            o.app_name = d['app_name']
        if 'contact_info' in d:
            o.contact_info = d['contact_info']
        if 'logo_pic' in d:
            o.logo_pic = d['logo_pic']
        if 'mcc_code' in d:
            o.mcc_code = d['mcc_code']
        if 'short_name' in d:
            o.short_name = d['short_name']
        if 'special_license_pic' in d:
            o.special_license_pic = d['special_license_pic']
        if 'usage_scenario' in d:
            o.usage_scenario = d['usage_scenario']
        if 'web_address' in d:
            o.web_address = d['web_address']
        if 'web_auth_pic' in d:
            o.web_auth_pic = d['web_auth_pic']
        if 'weixin_public_name' in d:
            o.weixin_public_name = d['weixin_public_name']
        return o


