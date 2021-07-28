#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayDataPrinterTaskSubmitModel(object):

    def __init__(self):
        self._access_token = None
        self._client_id = None
        self._client_secret = None
        self._content = None
        self._device_sn = None
        self._origin_id = None

    @property
    def access_token(self):
        return self._access_token

    @access_token.setter
    def access_token(self, value):
        self._access_token = value
    @property
    def client_id(self):
        return self._client_id

    @client_id.setter
    def client_id(self, value):
        self._client_id = value
    @property
    def client_secret(self):
        return self._client_secret

    @client_secret.setter
    def client_secret(self, value):
        self._client_secret = value
    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, value):
        self._content = value
    @property
    def device_sn(self):
        return self._device_sn

    @device_sn.setter
    def device_sn(self, value):
        self._device_sn = value
    @property
    def origin_id(self):
        return self._origin_id

    @origin_id.setter
    def origin_id(self, value):
        self._origin_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.access_token:
            if hasattr(self.access_token, 'to_alipay_dict'):
                params['access_token'] = self.access_token.to_alipay_dict()
            else:
                params['access_token'] = self.access_token
        if self.client_id:
            if hasattr(self.client_id, 'to_alipay_dict'):
                params['client_id'] = self.client_id.to_alipay_dict()
            else:
                params['client_id'] = self.client_id
        if self.client_secret:
            if hasattr(self.client_secret, 'to_alipay_dict'):
                params['client_secret'] = self.client_secret.to_alipay_dict()
            else:
                params['client_secret'] = self.client_secret
        if self.content:
            if hasattr(self.content, 'to_alipay_dict'):
                params['content'] = self.content.to_alipay_dict()
            else:
                params['content'] = self.content
        if self.device_sn:
            if hasattr(self.device_sn, 'to_alipay_dict'):
                params['device_sn'] = self.device_sn.to_alipay_dict()
            else:
                params['device_sn'] = self.device_sn
        if self.origin_id:
            if hasattr(self.origin_id, 'to_alipay_dict'):
                params['origin_id'] = self.origin_id.to_alipay_dict()
            else:
                params['origin_id'] = self.origin_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayDataPrinterTaskSubmitModel()
        if 'access_token' in d:
            o.access_token = d['access_token']
        if 'client_id' in d:
            o.client_id = d['client_id']
        if 'client_secret' in d:
            o.client_secret = d['client_secret']
        if 'content' in d:
            o.content = d['content']
        if 'device_sn' in d:
            o.device_sn = d['device_sn']
        if 'origin_id' in d:
            o.origin_id = d['origin_id']
        return o


