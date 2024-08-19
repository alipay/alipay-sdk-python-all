#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.AssistantServiceVO import AssistantServiceVO


class AlipayMerchantGroupAssistantServiceCreateormodifyModel(object):

    def __init__(self):
        self._content_id = None
        self._group_ids = None
        self._name = None
        self._services = None

    @property
    def content_id(self):
        return self._content_id

    @content_id.setter
    def content_id(self, value):
        self._content_id = value
    @property
    def group_ids(self):
        return self._group_ids

    @group_ids.setter
    def group_ids(self, value):
        if isinstance(value, list):
            self._group_ids = list()
            for i in value:
                self._group_ids.append(i)
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def services(self):
        return self._services

    @services.setter
    def services(self, value):
        if isinstance(value, list):
            self._services = list()
            for i in value:
                if isinstance(i, AssistantServiceVO):
                    self._services.append(i)
                else:
                    self._services.append(AssistantServiceVO.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.content_id:
            if hasattr(self.content_id, 'to_alipay_dict'):
                params['content_id'] = self.content_id.to_alipay_dict()
            else:
                params['content_id'] = self.content_id
        if self.group_ids:
            if isinstance(self.group_ids, list):
                for i in range(0, len(self.group_ids)):
                    element = self.group_ids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.group_ids[i] = element.to_alipay_dict()
            if hasattr(self.group_ids, 'to_alipay_dict'):
                params['group_ids'] = self.group_ids.to_alipay_dict()
            else:
                params['group_ids'] = self.group_ids
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.services:
            if isinstance(self.services, list):
                for i in range(0, len(self.services)):
                    element = self.services[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.services[i] = element.to_alipay_dict()
            if hasattr(self.services, 'to_alipay_dict'):
                params['services'] = self.services.to_alipay_dict()
            else:
                params['services'] = self.services
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayMerchantGroupAssistantServiceCreateormodifyModel()
        if 'content_id' in d:
            o.content_id = d['content_id']
        if 'group_ids' in d:
            o.group_ids = d['group_ids']
        if 'name' in d:
            o.name = d['name']
        if 'services' in d:
            o.services = d['services']
        return o


