#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.GravityParam import GravityParam
from alipay.aop.api.domain.SecGravityServiceHeader import SecGravityServiceHeader
from alipay.aop.api.domain.GravityParam import GravityParam


class AlipaySecurityRiskGravityConsultModel(object):

    def __init__(self):
        self._authorized_client_id = None
        self._extension = None
        self._header = None
        self._params = None
        self._product_id = None
        self._session_token = None

    @property
    def authorized_client_id(self):
        return self._authorized_client_id

    @authorized_client_id.setter
    def authorized_client_id(self, value):
        self._authorized_client_id = value
    @property
    def extension(self):
        return self._extension

    @extension.setter
    def extension(self, value):
        if isinstance(value, list):
            self._extension = list()
            for i in value:
                if isinstance(i, GravityParam):
                    self._extension.append(i)
                else:
                    self._extension.append(GravityParam.from_alipay_dict(i))
    @property
    def header(self):
        return self._header

    @header.setter
    def header(self, value):
        if isinstance(value, SecGravityServiceHeader):
            self._header = value
        else:
            self._header = SecGravityServiceHeader.from_alipay_dict(value)
    @property
    def params(self):
        return self._params

    @params.setter
    def params(self, value):
        if isinstance(value, list):
            self._params = list()
            for i in value:
                if isinstance(i, GravityParam):
                    self._params.append(i)
                else:
                    self._params.append(GravityParam.from_alipay_dict(i))
    @property
    def product_id(self):
        return self._product_id

    @product_id.setter
    def product_id(self, value):
        self._product_id = value
    @property
    def session_token(self):
        return self._session_token

    @session_token.setter
    def session_token(self, value):
        self._session_token = value


    def to_alipay_dict(self):
        params = dict()
        if self.authorized_client_id:
            if hasattr(self.authorized_client_id, 'to_alipay_dict'):
                params['authorized_client_id'] = self.authorized_client_id.to_alipay_dict()
            else:
                params['authorized_client_id'] = self.authorized_client_id
        if self.extension:
            if isinstance(self.extension, list):
                for i in range(0, len(self.extension)):
                    element = self.extension[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.extension[i] = element.to_alipay_dict()
            if hasattr(self.extension, 'to_alipay_dict'):
                params['extension'] = self.extension.to_alipay_dict()
            else:
                params['extension'] = self.extension
        if self.header:
            if hasattr(self.header, 'to_alipay_dict'):
                params['header'] = self.header.to_alipay_dict()
            else:
                params['header'] = self.header
        if self.params:
            if isinstance(self.params, list):
                for i in range(0, len(self.params)):
                    element = self.params[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.params[i] = element.to_alipay_dict()
            if hasattr(self.params, 'to_alipay_dict'):
                params['params'] = self.params.to_alipay_dict()
            else:
                params['params'] = self.params
        if self.product_id:
            if hasattr(self.product_id, 'to_alipay_dict'):
                params['product_id'] = self.product_id.to_alipay_dict()
            else:
                params['product_id'] = self.product_id
        if self.session_token:
            if hasattr(self.session_token, 'to_alipay_dict'):
                params['session_token'] = self.session_token.to_alipay_dict()
            else:
                params['session_token'] = self.session_token
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipaySecurityRiskGravityConsultModel()
        if 'authorized_client_id' in d:
            o.authorized_client_id = d['authorized_client_id']
        if 'extension' in d:
            o.extension = d['extension']
        if 'header' in d:
            o.header = d['header']
        if 'params' in d:
            o.params = d['params']
        if 'product_id' in d:
            o.product_id = d['product_id']
        if 'session_token' in d:
            o.session_token = d['session_token']
        return o


