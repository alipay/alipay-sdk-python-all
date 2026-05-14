#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RecyclingProxyRequest(object):

    def __init__(self):
        self._proxy_cert_no = None
        self._proxy_name = None
        self._proxy_phone = None

    @property
    def proxy_cert_no(self):
        return self._proxy_cert_no

    @proxy_cert_no.setter
    def proxy_cert_no(self, value):
        self._proxy_cert_no = value
    @property
    def proxy_name(self):
        return self._proxy_name

    @proxy_name.setter
    def proxy_name(self, value):
        self._proxy_name = value
    @property
    def proxy_phone(self):
        return self._proxy_phone

    @proxy_phone.setter
    def proxy_phone(self, value):
        self._proxy_phone = value


    def to_alipay_dict(self):
        params = dict()
        if self.proxy_cert_no:
            if hasattr(self.proxy_cert_no, 'to_alipay_dict'):
                params['proxy_cert_no'] = self.proxy_cert_no.to_alipay_dict()
            else:
                params['proxy_cert_no'] = self.proxy_cert_no
        if self.proxy_name:
            if hasattr(self.proxy_name, 'to_alipay_dict'):
                params['proxy_name'] = self.proxy_name.to_alipay_dict()
            else:
                params['proxy_name'] = self.proxy_name
        if self.proxy_phone:
            if hasattr(self.proxy_phone, 'to_alipay_dict'):
                params['proxy_phone'] = self.proxy_phone.to_alipay_dict()
            else:
                params['proxy_phone'] = self.proxy_phone
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RecyclingProxyRequest()
        if 'proxy_cert_no' in d:
            o.proxy_cert_no = d['proxy_cert_no']
        if 'proxy_name' in d:
            o.proxy_name = d['proxy_name']
        if 'proxy_phone' in d:
            o.proxy_phone = d['proxy_phone']
        return o


