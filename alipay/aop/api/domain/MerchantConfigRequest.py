#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MerchantConfigRequest(object):

    def __init__(self):
        self._banner_app_id = None
        self._banner_image_url = None
        self._banner_page = None
        self._banner_web_url = None
        self._jump_app_id = None
        self._jump_page = None
        self._jump_web_url = None
        self._merchant_contact = None
        self._merchant_id = None
        self._merchant_logo = None
        self._merchant_name = None

    @property
    def banner_app_id(self):
        return self._banner_app_id

    @banner_app_id.setter
    def banner_app_id(self, value):
        self._banner_app_id = value
    @property
    def banner_image_url(self):
        return self._banner_image_url

    @banner_image_url.setter
    def banner_image_url(self, value):
        self._banner_image_url = value
    @property
    def banner_page(self):
        return self._banner_page

    @banner_page.setter
    def banner_page(self, value):
        self._banner_page = value
    @property
    def banner_web_url(self):
        return self._banner_web_url

    @banner_web_url.setter
    def banner_web_url(self, value):
        self._banner_web_url = value
    @property
    def jump_app_id(self):
        return self._jump_app_id

    @jump_app_id.setter
    def jump_app_id(self, value):
        self._jump_app_id = value
    @property
    def jump_page(self):
        return self._jump_page

    @jump_page.setter
    def jump_page(self, value):
        self._jump_page = value
    @property
    def jump_web_url(self):
        return self._jump_web_url

    @jump_web_url.setter
    def jump_web_url(self, value):
        self._jump_web_url = value
    @property
    def merchant_contact(self):
        return self._merchant_contact

    @merchant_contact.setter
    def merchant_contact(self, value):
        self._merchant_contact = value
    @property
    def merchant_id(self):
        return self._merchant_id

    @merchant_id.setter
    def merchant_id(self, value):
        self._merchant_id = value
    @property
    def merchant_logo(self):
        return self._merchant_logo

    @merchant_logo.setter
    def merchant_logo(self, value):
        self._merchant_logo = value
    @property
    def merchant_name(self):
        return self._merchant_name

    @merchant_name.setter
    def merchant_name(self, value):
        self._merchant_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.banner_app_id:
            if hasattr(self.banner_app_id, 'to_alipay_dict'):
                params['banner_app_id'] = self.banner_app_id.to_alipay_dict()
            else:
                params['banner_app_id'] = self.banner_app_id
        if self.banner_image_url:
            if hasattr(self.banner_image_url, 'to_alipay_dict'):
                params['banner_image_url'] = self.banner_image_url.to_alipay_dict()
            else:
                params['banner_image_url'] = self.banner_image_url
        if self.banner_page:
            if hasattr(self.banner_page, 'to_alipay_dict'):
                params['banner_page'] = self.banner_page.to_alipay_dict()
            else:
                params['banner_page'] = self.banner_page
        if self.banner_web_url:
            if hasattr(self.banner_web_url, 'to_alipay_dict'):
                params['banner_web_url'] = self.banner_web_url.to_alipay_dict()
            else:
                params['banner_web_url'] = self.banner_web_url
        if self.jump_app_id:
            if hasattr(self.jump_app_id, 'to_alipay_dict'):
                params['jump_app_id'] = self.jump_app_id.to_alipay_dict()
            else:
                params['jump_app_id'] = self.jump_app_id
        if self.jump_page:
            if hasattr(self.jump_page, 'to_alipay_dict'):
                params['jump_page'] = self.jump_page.to_alipay_dict()
            else:
                params['jump_page'] = self.jump_page
        if self.jump_web_url:
            if hasattr(self.jump_web_url, 'to_alipay_dict'):
                params['jump_web_url'] = self.jump_web_url.to_alipay_dict()
            else:
                params['jump_web_url'] = self.jump_web_url
        if self.merchant_contact:
            if hasattr(self.merchant_contact, 'to_alipay_dict'):
                params['merchant_contact'] = self.merchant_contact.to_alipay_dict()
            else:
                params['merchant_contact'] = self.merchant_contact
        if self.merchant_id:
            if hasattr(self.merchant_id, 'to_alipay_dict'):
                params['merchant_id'] = self.merchant_id.to_alipay_dict()
            else:
                params['merchant_id'] = self.merchant_id
        if self.merchant_logo:
            if hasattr(self.merchant_logo, 'to_alipay_dict'):
                params['merchant_logo'] = self.merchant_logo.to_alipay_dict()
            else:
                params['merchant_logo'] = self.merchant_logo
        if self.merchant_name:
            if hasattr(self.merchant_name, 'to_alipay_dict'):
                params['merchant_name'] = self.merchant_name.to_alipay_dict()
            else:
                params['merchant_name'] = self.merchant_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MerchantConfigRequest()
        if 'banner_app_id' in d:
            o.banner_app_id = d['banner_app_id']
        if 'banner_image_url' in d:
            o.banner_image_url = d['banner_image_url']
        if 'banner_page' in d:
            o.banner_page = d['banner_page']
        if 'banner_web_url' in d:
            o.banner_web_url = d['banner_web_url']
        if 'jump_app_id' in d:
            o.jump_app_id = d['jump_app_id']
        if 'jump_page' in d:
            o.jump_page = d['jump_page']
        if 'jump_web_url' in d:
            o.jump_web_url = d['jump_web_url']
        if 'merchant_contact' in d:
            o.merchant_contact = d['merchant_contact']
        if 'merchant_id' in d:
            o.merchant_id = d['merchant_id']
        if 'merchant_logo' in d:
            o.merchant_logo = d['merchant_logo']
        if 'merchant_name' in d:
            o.merchant_name = d['merchant_name']
        return o


