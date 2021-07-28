#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SignInfo(object):

    def __init__(self):
        self._back_url = None
        self._ext_info = None
        self._inst_id = None
        self._sign_product_id = None
        self._signer_name = None
        self._solution_code = None

    @property
    def back_url(self):
        return self._back_url

    @back_url.setter
    def back_url(self, value):
        self._back_url = value
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value
    @property
    def inst_id(self):
        return self._inst_id

    @inst_id.setter
    def inst_id(self, value):
        self._inst_id = value
    @property
    def sign_product_id(self):
        return self._sign_product_id

    @sign_product_id.setter
    def sign_product_id(self, value):
        self._sign_product_id = value
    @property
    def signer_name(self):
        return self._signer_name

    @signer_name.setter
    def signer_name(self, value):
        self._signer_name = value
    @property
    def solution_code(self):
        return self._solution_code

    @solution_code.setter
    def solution_code(self, value):
        self._solution_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.back_url:
            if hasattr(self.back_url, 'to_alipay_dict'):
                params['back_url'] = self.back_url.to_alipay_dict()
            else:
                params['back_url'] = self.back_url
        if self.ext_info:
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        if self.inst_id:
            if hasattr(self.inst_id, 'to_alipay_dict'):
                params['inst_id'] = self.inst_id.to_alipay_dict()
            else:
                params['inst_id'] = self.inst_id
        if self.sign_product_id:
            if hasattr(self.sign_product_id, 'to_alipay_dict'):
                params['sign_product_id'] = self.sign_product_id.to_alipay_dict()
            else:
                params['sign_product_id'] = self.sign_product_id
        if self.signer_name:
            if hasattr(self.signer_name, 'to_alipay_dict'):
                params['signer_name'] = self.signer_name.to_alipay_dict()
            else:
                params['signer_name'] = self.signer_name
        if self.solution_code:
            if hasattr(self.solution_code, 'to_alipay_dict'):
                params['solution_code'] = self.solution_code.to_alipay_dict()
            else:
                params['solution_code'] = self.solution_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SignInfo()
        if 'back_url' in d:
            o.back_url = d['back_url']
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'inst_id' in d:
            o.inst_id = d['inst_id']
        if 'sign_product_id' in d:
            o.sign_product_id = d['sign_product_id']
        if 'signer_name' in d:
            o.signer_name = d['signer_name']
        if 'solution_code' in d:
            o.solution_code = d['solution_code']
        return o


