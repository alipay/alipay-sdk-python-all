#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class BPaaSServiceInfo(object):

    def __init__(self):
        self._demo_link = None
        self._doc_link = None
        self._if_sign = None
        self._open_type = None
        self._service_code = None
        self._service_id = None
        self._service_name = None
        self._service_type = None
        self._service_version = None
        self._slogan = None

    @property
    def demo_link(self):
        return self._demo_link

    @demo_link.setter
    def demo_link(self, value):
        self._demo_link = value
    @property
    def doc_link(self):
        return self._doc_link

    @doc_link.setter
    def doc_link(self, value):
        self._doc_link = value
    @property
    def if_sign(self):
        return self._if_sign

    @if_sign.setter
    def if_sign(self, value):
        self._if_sign = value
    @property
    def open_type(self):
        return self._open_type

    @open_type.setter
    def open_type(self, value):
        self._open_type = value
    @property
    def service_code(self):
        return self._service_code

    @service_code.setter
    def service_code(self, value):
        self._service_code = value
    @property
    def service_id(self):
        return self._service_id

    @service_id.setter
    def service_id(self, value):
        self._service_id = value
    @property
    def service_name(self):
        return self._service_name

    @service_name.setter
    def service_name(self, value):
        self._service_name = value
    @property
    def service_type(self):
        return self._service_type

    @service_type.setter
    def service_type(self, value):
        self._service_type = value
    @property
    def service_version(self):
        return self._service_version

    @service_version.setter
    def service_version(self, value):
        self._service_version = value
    @property
    def slogan(self):
        return self._slogan

    @slogan.setter
    def slogan(self, value):
        self._slogan = value


    def to_alipay_dict(self):
        params = dict()
        if self.demo_link:
            if hasattr(self.demo_link, 'to_alipay_dict'):
                params['demo_link'] = self.demo_link.to_alipay_dict()
            else:
                params['demo_link'] = self.demo_link
        if self.doc_link:
            if hasattr(self.doc_link, 'to_alipay_dict'):
                params['doc_link'] = self.doc_link.to_alipay_dict()
            else:
                params['doc_link'] = self.doc_link
        if self.if_sign:
            if hasattr(self.if_sign, 'to_alipay_dict'):
                params['if_sign'] = self.if_sign.to_alipay_dict()
            else:
                params['if_sign'] = self.if_sign
        if self.open_type:
            if hasattr(self.open_type, 'to_alipay_dict'):
                params['open_type'] = self.open_type.to_alipay_dict()
            else:
                params['open_type'] = self.open_type
        if self.service_code:
            if hasattr(self.service_code, 'to_alipay_dict'):
                params['service_code'] = self.service_code.to_alipay_dict()
            else:
                params['service_code'] = self.service_code
        if self.service_id:
            if hasattr(self.service_id, 'to_alipay_dict'):
                params['service_id'] = self.service_id.to_alipay_dict()
            else:
                params['service_id'] = self.service_id
        if self.service_name:
            if hasattr(self.service_name, 'to_alipay_dict'):
                params['service_name'] = self.service_name.to_alipay_dict()
            else:
                params['service_name'] = self.service_name
        if self.service_type:
            if hasattr(self.service_type, 'to_alipay_dict'):
                params['service_type'] = self.service_type.to_alipay_dict()
            else:
                params['service_type'] = self.service_type
        if self.service_version:
            if hasattr(self.service_version, 'to_alipay_dict'):
                params['service_version'] = self.service_version.to_alipay_dict()
            else:
                params['service_version'] = self.service_version
        if self.slogan:
            if hasattr(self.slogan, 'to_alipay_dict'):
                params['slogan'] = self.slogan.to_alipay_dict()
            else:
                params['slogan'] = self.slogan
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = BPaaSServiceInfo()
        if 'demo_link' in d:
            o.demo_link = d['demo_link']
        if 'doc_link' in d:
            o.doc_link = d['doc_link']
        if 'if_sign' in d:
            o.if_sign = d['if_sign']
        if 'open_type' in d:
            o.open_type = d['open_type']
        if 'service_code' in d:
            o.service_code = d['service_code']
        if 'service_id' in d:
            o.service_id = d['service_id']
        if 'service_name' in d:
            o.service_name = d['service_name']
        if 'service_type' in d:
            o.service_type = d['service_type']
        if 'service_version' in d:
            o.service_version = d['service_version']
        if 'slogan' in d:
            o.slogan = d['slogan']
        return o


