#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ResourceRelatedItem(object):

    def __init__(self):
        self._resource_ask_url = None
        self._resource_id = None
        self._resource_type = None
        self._resource_url = None

    @property
    def resource_ask_url(self):
        return self._resource_ask_url

    @resource_ask_url.setter
    def resource_ask_url(self, value):
        self._resource_ask_url = value
    @property
    def resource_id(self):
        return self._resource_id

    @resource_id.setter
    def resource_id(self, value):
        self._resource_id = value
    @property
    def resource_type(self):
        return self._resource_type

    @resource_type.setter
    def resource_type(self, value):
        self._resource_type = value
    @property
    def resource_url(self):
        return self._resource_url

    @resource_url.setter
    def resource_url(self, value):
        self._resource_url = value


    def to_alipay_dict(self):
        params = dict()
        if self.resource_ask_url:
            if hasattr(self.resource_ask_url, 'to_alipay_dict'):
                params['resource_ask_url'] = self.resource_ask_url.to_alipay_dict()
            else:
                params['resource_ask_url'] = self.resource_ask_url
        if self.resource_id:
            if hasattr(self.resource_id, 'to_alipay_dict'):
                params['resource_id'] = self.resource_id.to_alipay_dict()
            else:
                params['resource_id'] = self.resource_id
        if self.resource_type:
            if hasattr(self.resource_type, 'to_alipay_dict'):
                params['resource_type'] = self.resource_type.to_alipay_dict()
            else:
                params['resource_type'] = self.resource_type
        if self.resource_url:
            if hasattr(self.resource_url, 'to_alipay_dict'):
                params['resource_url'] = self.resource_url.to_alipay_dict()
            else:
                params['resource_url'] = self.resource_url
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ResourceRelatedItem()
        if 'resource_ask_url' in d:
            o.resource_ask_url = d['resource_ask_url']
        if 'resource_id' in d:
            o.resource_id = d['resource_id']
        if 'resource_type' in d:
            o.resource_type = d['resource_type']
        if 'resource_url' in d:
            o.resource_url = d['resource_url']
        return o


