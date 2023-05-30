#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RuntimeProtectConfig(object):

    def __init__(self):
        self._anti_debug = None
        self._anti_emulator = None
        self._anti_hook = None
        self._anti_inject = None
        self._anti_multi_app = None
        self._anti_root = None
        self._anti_signature = None

    @property
    def anti_debug(self):
        return self._anti_debug

    @anti_debug.setter
    def anti_debug(self, value):
        self._anti_debug = value
    @property
    def anti_emulator(self):
        return self._anti_emulator

    @anti_emulator.setter
    def anti_emulator(self, value):
        self._anti_emulator = value
    @property
    def anti_hook(self):
        return self._anti_hook

    @anti_hook.setter
    def anti_hook(self, value):
        self._anti_hook = value
    @property
    def anti_inject(self):
        return self._anti_inject

    @anti_inject.setter
    def anti_inject(self, value):
        self._anti_inject = value
    @property
    def anti_multi_app(self):
        return self._anti_multi_app

    @anti_multi_app.setter
    def anti_multi_app(self, value):
        self._anti_multi_app = value
    @property
    def anti_root(self):
        return self._anti_root

    @anti_root.setter
    def anti_root(self, value):
        self._anti_root = value
    @property
    def anti_signature(self):
        return self._anti_signature

    @anti_signature.setter
    def anti_signature(self, value):
        self._anti_signature = value


    def to_alipay_dict(self):
        params = dict()
        if self.anti_debug:
            if hasattr(self.anti_debug, 'to_alipay_dict'):
                params['anti_debug'] = self.anti_debug.to_alipay_dict()
            else:
                params['anti_debug'] = self.anti_debug
        if self.anti_emulator:
            if hasattr(self.anti_emulator, 'to_alipay_dict'):
                params['anti_emulator'] = self.anti_emulator.to_alipay_dict()
            else:
                params['anti_emulator'] = self.anti_emulator
        if self.anti_hook:
            if hasattr(self.anti_hook, 'to_alipay_dict'):
                params['anti_hook'] = self.anti_hook.to_alipay_dict()
            else:
                params['anti_hook'] = self.anti_hook
        if self.anti_inject:
            if hasattr(self.anti_inject, 'to_alipay_dict'):
                params['anti_inject'] = self.anti_inject.to_alipay_dict()
            else:
                params['anti_inject'] = self.anti_inject
        if self.anti_multi_app:
            if hasattr(self.anti_multi_app, 'to_alipay_dict'):
                params['anti_multi_app'] = self.anti_multi_app.to_alipay_dict()
            else:
                params['anti_multi_app'] = self.anti_multi_app
        if self.anti_root:
            if hasattr(self.anti_root, 'to_alipay_dict'):
                params['anti_root'] = self.anti_root.to_alipay_dict()
            else:
                params['anti_root'] = self.anti_root
        if self.anti_signature:
            if hasattr(self.anti_signature, 'to_alipay_dict'):
                params['anti_signature'] = self.anti_signature.to_alipay_dict()
            else:
                params['anti_signature'] = self.anti_signature
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RuntimeProtectConfig()
        if 'anti_debug' in d:
            o.anti_debug = d['anti_debug']
        if 'anti_emulator' in d:
            o.anti_emulator = d['anti_emulator']
        if 'anti_hook' in d:
            o.anti_hook = d['anti_hook']
        if 'anti_inject' in d:
            o.anti_inject = d['anti_inject']
        if 'anti_multi_app' in d:
            o.anti_multi_app = d['anti_multi_app']
        if 'anti_root' in d:
            o.anti_root = d['anti_root']
        if 'anti_signature' in d:
            o.anti_signature = d['anti_signature']
        return o


