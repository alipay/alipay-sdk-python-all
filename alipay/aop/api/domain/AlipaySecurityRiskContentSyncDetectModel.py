#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipaySecurityRiskContentSyncDetectModel(object):

    def __init__(self):
        self._channel = None
        self._content_type = None
        self._data_list = None
        self._open_id = None
        self._products = None
        self._request_id = None
        self._tenants = None
        self._user_id = None

    @property
    def channel(self):
        return self._channel

    @channel.setter
    def channel(self, value):
        self._channel = value
    @property
    def content_type(self):
        return self._content_type

    @content_type.setter
    def content_type(self, value):
        self._content_type = value
    @property
    def data_list(self):
        return self._data_list

    @data_list.setter
    def data_list(self, value):
        if isinstance(value, list):
            self._data_list = list()
            for i in value:
                self._data_list.append(i)
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def products(self):
        return self._products

    @products.setter
    def products(self, value):
        self._products = value
    @property
    def request_id(self):
        return self._request_id

    @request_id.setter
    def request_id(self, value):
        self._request_id = value
    @property
    def tenants(self):
        return self._tenants

    @tenants.setter
    def tenants(self, value):
        self._tenants = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.channel:
            if hasattr(self.channel, 'to_alipay_dict'):
                params['channel'] = self.channel.to_alipay_dict()
            else:
                params['channel'] = self.channel
        if self.content_type:
            if hasattr(self.content_type, 'to_alipay_dict'):
                params['content_type'] = self.content_type.to_alipay_dict()
            else:
                params['content_type'] = self.content_type
        if self.data_list:
            if isinstance(self.data_list, list):
                for i in range(0, len(self.data_list)):
                    element = self.data_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.data_list[i] = element.to_alipay_dict()
            if hasattr(self.data_list, 'to_alipay_dict'):
                params['data_list'] = self.data_list.to_alipay_dict()
            else:
                params['data_list'] = self.data_list
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.products:
            if hasattr(self.products, 'to_alipay_dict'):
                params['products'] = self.products.to_alipay_dict()
            else:
                params['products'] = self.products
        if self.request_id:
            if hasattr(self.request_id, 'to_alipay_dict'):
                params['request_id'] = self.request_id.to_alipay_dict()
            else:
                params['request_id'] = self.request_id
        if self.tenants:
            if hasattr(self.tenants, 'to_alipay_dict'):
                params['tenants'] = self.tenants.to_alipay_dict()
            else:
                params['tenants'] = self.tenants
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipaySecurityRiskContentSyncDetectModel()
        if 'channel' in d:
            o.channel = d['channel']
        if 'content_type' in d:
            o.content_type = d['content_type']
        if 'data_list' in d:
            o.data_list = d['data_list']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'products' in d:
            o.products = d['products']
        if 'request_id' in d:
            o.request_id = d['request_id']
        if 'tenants' in d:
            o.tenants = d['tenants']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


