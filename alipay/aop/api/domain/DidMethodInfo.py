#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class DidMethodInfo(object):

    def __init__(self):
        self._sign_src = None
        self._signature = None
        self._vm = None

    @property
    def sign_src(self):
        return self._sign_src

    @sign_src.setter
    def sign_src(self, value):
        self._sign_src = value
    @property
    def signature(self):
        return self._signature

    @signature.setter
    def signature(self, value):
        self._signature = value
    @property
    def vm(self):
        return self._vm

    @vm.setter
    def vm(self, value):
        self._vm = value


    def to_alipay_dict(self):
        params = dict()
        if self.sign_src:
            if hasattr(self.sign_src, 'to_alipay_dict'):
                params['sign_src'] = self.sign_src.to_alipay_dict()
            else:
                params['sign_src'] = self.sign_src
        if self.signature:
            if hasattr(self.signature, 'to_alipay_dict'):
                params['signature'] = self.signature.to_alipay_dict()
            else:
                params['signature'] = self.signature
        if self.vm:
            if hasattr(self.vm, 'to_alipay_dict'):
                params['vm'] = self.vm.to_alipay_dict()
            else:
                params['vm'] = self.vm
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DidMethodInfo()
        if 'sign_src' in d:
            o.sign_src = d['sign_src']
        if 'signature' in d:
            o.signature = d['signature']
        if 'vm' in d:
            o.vm = d['vm']
        return o


