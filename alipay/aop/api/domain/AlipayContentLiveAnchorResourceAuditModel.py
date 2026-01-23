#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayContentLiveAnchorResourceAuditModel(object):

    def __init__(self):
        self._access_token = None
        self._interactive_name = None
        self._public_id = None
        self._resource_list = None
        self._resource_type = None

    @property
    def access_token(self):
        return self._access_token

    @access_token.setter
    def access_token(self, value):
        self._access_token = value
    @property
    def interactive_name(self):
        return self._interactive_name

    @interactive_name.setter
    def interactive_name(self, value):
        self._interactive_name = value
    @property
    def public_id(self):
        return self._public_id

    @public_id.setter
    def public_id(self, value):
        self._public_id = value
    @property
    def resource_list(self):
        return self._resource_list

    @resource_list.setter
    def resource_list(self, value):
        if isinstance(value, list):
            self._resource_list = list()
            for i in value:
                self._resource_list.append(i)
    @property
    def resource_type(self):
        return self._resource_type

    @resource_type.setter
    def resource_type(self, value):
        self._resource_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.access_token:
            if hasattr(self.access_token, 'to_alipay_dict'):
                params['access_token'] = self.access_token.to_alipay_dict()
            else:
                params['access_token'] = self.access_token
        if self.interactive_name:
            if hasattr(self.interactive_name, 'to_alipay_dict'):
                params['interactive_name'] = self.interactive_name.to_alipay_dict()
            else:
                params['interactive_name'] = self.interactive_name
        if self.public_id:
            if hasattr(self.public_id, 'to_alipay_dict'):
                params['public_id'] = self.public_id.to_alipay_dict()
            else:
                params['public_id'] = self.public_id
        if self.resource_list:
            if isinstance(self.resource_list, list):
                for i in range(0, len(self.resource_list)):
                    element = self.resource_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.resource_list[i] = element.to_alipay_dict()
            if hasattr(self.resource_list, 'to_alipay_dict'):
                params['resource_list'] = self.resource_list.to_alipay_dict()
            else:
                params['resource_list'] = self.resource_list
        if self.resource_type:
            if hasattr(self.resource_type, 'to_alipay_dict'):
                params['resource_type'] = self.resource_type.to_alipay_dict()
            else:
                params['resource_type'] = self.resource_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayContentLiveAnchorResourceAuditModel()
        if 'access_token' in d:
            o.access_token = d['access_token']
        if 'interactive_name' in d:
            o.interactive_name = d['interactive_name']
        if 'public_id' in d:
            o.public_id = d['public_id']
        if 'resource_list' in d:
            o.resource_list = d['resource_list']
        if 'resource_type' in d:
            o.resource_type = d['resource_type']
        return o


