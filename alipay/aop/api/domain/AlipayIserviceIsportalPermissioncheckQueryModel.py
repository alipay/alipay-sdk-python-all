#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayIserviceIsportalPermissioncheckQueryModel(object):

    def __init__(self):
        self._busvc_cloud_id = None
        self._busvc_id = None
        self._codes = None
        self._uri = None

    @property
    def busvc_cloud_id(self):
        return self._busvc_cloud_id

    @busvc_cloud_id.setter
    def busvc_cloud_id(self, value):
        self._busvc_cloud_id = value
    @property
    def busvc_id(self):
        return self._busvc_id

    @busvc_id.setter
    def busvc_id(self, value):
        self._busvc_id = value
    @property
    def codes(self):
        return self._codes

    @codes.setter
    def codes(self, value):
        if isinstance(value, list):
            self._codes = list()
            for i in value:
                self._codes.append(i)
    @property
    def uri(self):
        return self._uri

    @uri.setter
    def uri(self, value):
        self._uri = value


    def to_alipay_dict(self):
        params = dict()
        if self.busvc_cloud_id:
            if hasattr(self.busvc_cloud_id, 'to_alipay_dict'):
                params['busvc_cloud_id'] = self.busvc_cloud_id.to_alipay_dict()
            else:
                params['busvc_cloud_id'] = self.busvc_cloud_id
        if self.busvc_id:
            if hasattr(self.busvc_id, 'to_alipay_dict'):
                params['busvc_id'] = self.busvc_id.to_alipay_dict()
            else:
                params['busvc_id'] = self.busvc_id
        if self.codes:
            if isinstance(self.codes, list):
                for i in range(0, len(self.codes)):
                    element = self.codes[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.codes[i] = element.to_alipay_dict()
            if hasattr(self.codes, 'to_alipay_dict'):
                params['codes'] = self.codes.to_alipay_dict()
            else:
                params['codes'] = self.codes
        if self.uri:
            if hasattr(self.uri, 'to_alipay_dict'):
                params['uri'] = self.uri.to_alipay_dict()
            else:
                params['uri'] = self.uri
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayIserviceIsportalPermissioncheckQueryModel()
        if 'busvc_cloud_id' in d:
            o.busvc_cloud_id = d['busvc_cloud_id']
        if 'busvc_id' in d:
            o.busvc_id = d['busvc_id']
        if 'codes' in d:
            o.codes = d['codes']
        if 'uri' in d:
            o.uri = d['uri']
        return o


