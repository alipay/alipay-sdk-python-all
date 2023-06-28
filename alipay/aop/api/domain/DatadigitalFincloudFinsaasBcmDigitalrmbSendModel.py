#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class DatadigitalFincloudFinsaasBcmDigitalrmbSendModel(object):

    def __init__(self):
        self._phone_num_encrypt = None
        self._sms_code = None
        self._web_page_url = None

    @property
    def phone_num_encrypt(self):
        return self._phone_num_encrypt

    @phone_num_encrypt.setter
    def phone_num_encrypt(self, value):
        self._phone_num_encrypt = value
    @property
    def sms_code(self):
        return self._sms_code

    @sms_code.setter
    def sms_code(self, value):
        self._sms_code = value
    @property
    def web_page_url(self):
        return self._web_page_url

    @web_page_url.setter
    def web_page_url(self, value):
        self._web_page_url = value


    def to_alipay_dict(self):
        params = dict()
        if self.phone_num_encrypt:
            if hasattr(self.phone_num_encrypt, 'to_alipay_dict'):
                params['phone_num_encrypt'] = self.phone_num_encrypt.to_alipay_dict()
            else:
                params['phone_num_encrypt'] = self.phone_num_encrypt
        if self.sms_code:
            if hasattr(self.sms_code, 'to_alipay_dict'):
                params['sms_code'] = self.sms_code.to_alipay_dict()
            else:
                params['sms_code'] = self.sms_code
        if self.web_page_url:
            if hasattr(self.web_page_url, 'to_alipay_dict'):
                params['web_page_url'] = self.web_page_url.to_alipay_dict()
            else:
                params['web_page_url'] = self.web_page_url
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DatadigitalFincloudFinsaasBcmDigitalrmbSendModel()
        if 'phone_num_encrypt' in d:
            o.phone_num_encrypt = d['phone_num_encrypt']
        if 'sms_code' in d:
            o.sms_code = d['sms_code']
        if 'web_page_url' in d:
            o.web_page_url = d['web_page_url']
        return o


