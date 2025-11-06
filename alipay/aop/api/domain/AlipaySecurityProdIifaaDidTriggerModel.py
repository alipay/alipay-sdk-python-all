#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.SelfSignInfo import SelfSignInfo
from alipay.aop.api.domain.DidMethodInfo import DidMethodInfo


class AlipaySecurityProdIifaaDidTriggerModel(object):

    def __init__(self):
        self._action = None
        self._alias = None
        self._did = None
        self._methods = None
        self._pro_version = None
        self._self_sign_info = None
        self._sign_document = None
        self._sign_methods = None

    @property
    def action(self):
        return self._action

    @action.setter
    def action(self, value):
        self._action = value
    @property
    def alias(self):
        return self._alias

    @alias.setter
    def alias(self, value):
        self._alias = value
    @property
    def did(self):
        return self._did

    @did.setter
    def did(self, value):
        self._did = value
    @property
    def methods(self):
        return self._methods

    @methods.setter
    def methods(self, value):
        if isinstance(value, list):
            self._methods = list()
            for i in value:
                self._methods.append(i)
    @property
    def pro_version(self):
        return self._pro_version

    @pro_version.setter
    def pro_version(self, value):
        self._pro_version = value
    @property
    def self_sign_info(self):
        return self._self_sign_info

    @self_sign_info.setter
    def self_sign_info(self, value):
        if isinstance(value, list):
            self._self_sign_info = list()
            for i in value:
                if isinstance(i, SelfSignInfo):
                    self._self_sign_info.append(i)
                else:
                    self._self_sign_info.append(SelfSignInfo.from_alipay_dict(i))
    @property
    def sign_document(self):
        return self._sign_document

    @sign_document.setter
    def sign_document(self, value):
        self._sign_document = value
    @property
    def sign_methods(self):
        return self._sign_methods

    @sign_methods.setter
    def sign_methods(self, value):
        if isinstance(value, list):
            self._sign_methods = list()
            for i in value:
                if isinstance(i, DidMethodInfo):
                    self._sign_methods.append(i)
                else:
                    self._sign_methods.append(DidMethodInfo.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.action:
            if hasattr(self.action, 'to_alipay_dict'):
                params['action'] = self.action.to_alipay_dict()
            else:
                params['action'] = self.action
        if self.alias:
            if hasattr(self.alias, 'to_alipay_dict'):
                params['alias'] = self.alias.to_alipay_dict()
            else:
                params['alias'] = self.alias
        if self.did:
            if hasattr(self.did, 'to_alipay_dict'):
                params['did'] = self.did.to_alipay_dict()
            else:
                params['did'] = self.did
        if self.methods:
            if isinstance(self.methods, list):
                for i in range(0, len(self.methods)):
                    element = self.methods[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.methods[i] = element.to_alipay_dict()
            if hasattr(self.methods, 'to_alipay_dict'):
                params['methods'] = self.methods.to_alipay_dict()
            else:
                params['methods'] = self.methods
        if self.pro_version:
            if hasattr(self.pro_version, 'to_alipay_dict'):
                params['pro_version'] = self.pro_version.to_alipay_dict()
            else:
                params['pro_version'] = self.pro_version
        if self.self_sign_info:
            if isinstance(self.self_sign_info, list):
                for i in range(0, len(self.self_sign_info)):
                    element = self.self_sign_info[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.self_sign_info[i] = element.to_alipay_dict()
            if hasattr(self.self_sign_info, 'to_alipay_dict'):
                params['self_sign_info'] = self.self_sign_info.to_alipay_dict()
            else:
                params['self_sign_info'] = self.self_sign_info
        if self.sign_document:
            if hasattr(self.sign_document, 'to_alipay_dict'):
                params['sign_document'] = self.sign_document.to_alipay_dict()
            else:
                params['sign_document'] = self.sign_document
        if self.sign_methods:
            if isinstance(self.sign_methods, list):
                for i in range(0, len(self.sign_methods)):
                    element = self.sign_methods[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.sign_methods[i] = element.to_alipay_dict()
            if hasattr(self.sign_methods, 'to_alipay_dict'):
                params['sign_methods'] = self.sign_methods.to_alipay_dict()
            else:
                params['sign_methods'] = self.sign_methods
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipaySecurityProdIifaaDidTriggerModel()
        if 'action' in d:
            o.action = d['action']
        if 'alias' in d:
            o.alias = d['alias']
        if 'did' in d:
            o.did = d['did']
        if 'methods' in d:
            o.methods = d['methods']
        if 'pro_version' in d:
            o.pro_version = d['pro_version']
        if 'self_sign_info' in d:
            o.self_sign_info = d['self_sign_info']
        if 'sign_document' in d:
            o.sign_document = d['sign_document']
        if 'sign_methods' in d:
            o.sign_methods = d['sign_methods']
        return o


