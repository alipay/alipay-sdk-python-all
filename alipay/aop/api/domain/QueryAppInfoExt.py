#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class QueryAppInfoExt(object):

    def __init__(self):
        self._app_name = None
        self._app_number = None
        self._application_type = None
        self._callback_url = None
        self._charset_type = None
        self._dev_id = None
        self._gateway_url = None
        self._package_code_set = None
        self._pid = None
        self._signature_type = None
        self._status = None
        self._use_encrypt = None

    @property
    def app_name(self):
        return self._app_name

    @app_name.setter
    def app_name(self, value):
        self._app_name = value
    @property
    def app_number(self):
        return self._app_number

    @app_number.setter
    def app_number(self, value):
        self._app_number = value
    @property
    def application_type(self):
        return self._application_type

    @application_type.setter
    def application_type(self, value):
        self._application_type = value
    @property
    def callback_url(self):
        return self._callback_url

    @callback_url.setter
    def callback_url(self, value):
        self._callback_url = value
    @property
    def charset_type(self):
        return self._charset_type

    @charset_type.setter
    def charset_type(self, value):
        self._charset_type = value
    @property
    def dev_id(self):
        return self._dev_id

    @dev_id.setter
    def dev_id(self, value):
        self._dev_id = value
    @property
    def gateway_url(self):
        return self._gateway_url

    @gateway_url.setter
    def gateway_url(self, value):
        self._gateway_url = value
    @property
    def package_code_set(self):
        return self._package_code_set

    @package_code_set.setter
    def package_code_set(self, value):
        if isinstance(value, list):
            self._package_code_set = list()
            for i in value:
                self._package_code_set.append(i)
    @property
    def pid(self):
        return self._pid

    @pid.setter
    def pid(self, value):
        self._pid = value
    @property
    def signature_type(self):
        return self._signature_type

    @signature_type.setter
    def signature_type(self, value):
        self._signature_type = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def use_encrypt(self):
        return self._use_encrypt

    @use_encrypt.setter
    def use_encrypt(self, value):
        self._use_encrypt = value


    def to_alipay_dict(self):
        params = dict()
        if self.app_name:
            if hasattr(self.app_name, 'to_alipay_dict'):
                params['app_name'] = self.app_name.to_alipay_dict()
            else:
                params['app_name'] = self.app_name
        if self.app_number:
            if hasattr(self.app_number, 'to_alipay_dict'):
                params['app_number'] = self.app_number.to_alipay_dict()
            else:
                params['app_number'] = self.app_number
        if self.application_type:
            if hasattr(self.application_type, 'to_alipay_dict'):
                params['application_type'] = self.application_type.to_alipay_dict()
            else:
                params['application_type'] = self.application_type
        if self.callback_url:
            if hasattr(self.callback_url, 'to_alipay_dict'):
                params['callback_url'] = self.callback_url.to_alipay_dict()
            else:
                params['callback_url'] = self.callback_url
        if self.charset_type:
            if hasattr(self.charset_type, 'to_alipay_dict'):
                params['charset_type'] = self.charset_type.to_alipay_dict()
            else:
                params['charset_type'] = self.charset_type
        if self.dev_id:
            if hasattr(self.dev_id, 'to_alipay_dict'):
                params['dev_id'] = self.dev_id.to_alipay_dict()
            else:
                params['dev_id'] = self.dev_id
        if self.gateway_url:
            if hasattr(self.gateway_url, 'to_alipay_dict'):
                params['gateway_url'] = self.gateway_url.to_alipay_dict()
            else:
                params['gateway_url'] = self.gateway_url
        if self.package_code_set:
            if isinstance(self.package_code_set, list):
                for i in range(0, len(self.package_code_set)):
                    element = self.package_code_set[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.package_code_set[i] = element.to_alipay_dict()
            if hasattr(self.package_code_set, 'to_alipay_dict'):
                params['package_code_set'] = self.package_code_set.to_alipay_dict()
            else:
                params['package_code_set'] = self.package_code_set
        if self.pid:
            if hasattr(self.pid, 'to_alipay_dict'):
                params['pid'] = self.pid.to_alipay_dict()
            else:
                params['pid'] = self.pid
        if self.signature_type:
            if hasattr(self.signature_type, 'to_alipay_dict'):
                params['signature_type'] = self.signature_type.to_alipay_dict()
            else:
                params['signature_type'] = self.signature_type
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.use_encrypt:
            if hasattr(self.use_encrypt, 'to_alipay_dict'):
                params['use_encrypt'] = self.use_encrypt.to_alipay_dict()
            else:
                params['use_encrypt'] = self.use_encrypt
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = QueryAppInfoExt()
        if 'app_name' in d:
            o.app_name = d['app_name']
        if 'app_number' in d:
            o.app_number = d['app_number']
        if 'application_type' in d:
            o.application_type = d['application_type']
        if 'callback_url' in d:
            o.callback_url = d['callback_url']
        if 'charset_type' in d:
            o.charset_type = d['charset_type']
        if 'dev_id' in d:
            o.dev_id = d['dev_id']
        if 'gateway_url' in d:
            o.gateway_url = d['gateway_url']
        if 'package_code_set' in d:
            o.package_code_set = d['package_code_set']
        if 'pid' in d:
            o.pid = d['pid']
        if 'signature_type' in d:
            o.signature_type = d['signature_type']
        if 'status' in d:
            o.status = d['status']
        if 'use_encrypt' in d:
            o.use_encrypt = d['use_encrypt']
        return o


