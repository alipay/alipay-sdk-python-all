#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ExternalInfo(object):

    def __init__(self):
        self._client_id = None
        self._ext_info = None
        self._external_id = None
        self._external_name = None
        self._id = None

    @property
    def client_id(self):
        return self._client_id

    @client_id.setter
    def client_id(self, value):
        self._client_id = value
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value
    @property
    def external_id(self):
        return self._external_id

    @external_id.setter
    def external_id(self, value):
        self._external_id = value
    @property
    def external_name(self):
        return self._external_name

    @external_name.setter
    def external_name(self, value):
        self._external_name = value
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value


    def to_alipay_dict(self):
        params = dict()
        if self.client_id:
            if hasattr(self.client_id, 'to_alipay_dict'):
                params['client_id'] = self.client_id.to_alipay_dict()
            else:
                params['client_id'] = self.client_id
        if self.ext_info:
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        if self.external_id:
            if hasattr(self.external_id, 'to_alipay_dict'):
                params['external_id'] = self.external_id.to_alipay_dict()
            else:
                params['external_id'] = self.external_id
        if self.external_name:
            if hasattr(self.external_name, 'to_alipay_dict'):
                params['external_name'] = self.external_name.to_alipay_dict()
            else:
                params['external_name'] = self.external_name
        if self.id:
            if hasattr(self.id, 'to_alipay_dict'):
                params['id'] = self.id.to_alipay_dict()
            else:
                params['id'] = self.id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ExternalInfo()
        if 'client_id' in d:
            o.client_id = d['client_id']
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'external_id' in d:
            o.external_id = d['external_id']
        if 'external_name' in d:
            o.external_name = d['external_name']
        if 'id' in d:
            o.id = d['id']
        return o


