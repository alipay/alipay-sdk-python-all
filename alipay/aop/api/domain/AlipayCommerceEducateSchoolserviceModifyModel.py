#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceEducateSchoolserviceModifyModel(object):

    def __init__(self):
        self._content_id = None
        self._name = None
        self._out_service_id = None
        self._service_app_id = None
        self._service_id = None
        self._source_type = None
        self._url = None

    @property
    def content_id(self):
        return self._content_id

    @content_id.setter
    def content_id(self, value):
        self._content_id = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def out_service_id(self):
        return self._out_service_id

    @out_service_id.setter
    def out_service_id(self, value):
        self._out_service_id = value
    @property
    def service_app_id(self):
        return self._service_app_id

    @service_app_id.setter
    def service_app_id(self, value):
        self._service_app_id = value
    @property
    def service_id(self):
        return self._service_id

    @service_id.setter
    def service_id(self, value):
        self._service_id = value
    @property
    def source_type(self):
        return self._source_type

    @source_type.setter
    def source_type(self, value):
        self._source_type = value
    @property
    def url(self):
        return self._url

    @url.setter
    def url(self, value):
        self._url = value


    def to_alipay_dict(self):
        params = dict()
        if self.content_id:
            if hasattr(self.content_id, 'to_alipay_dict'):
                params['content_id'] = self.content_id.to_alipay_dict()
            else:
                params['content_id'] = self.content_id
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.out_service_id:
            if hasattr(self.out_service_id, 'to_alipay_dict'):
                params['out_service_id'] = self.out_service_id.to_alipay_dict()
            else:
                params['out_service_id'] = self.out_service_id
        if self.service_app_id:
            if hasattr(self.service_app_id, 'to_alipay_dict'):
                params['service_app_id'] = self.service_app_id.to_alipay_dict()
            else:
                params['service_app_id'] = self.service_app_id
        if self.service_id:
            if hasattr(self.service_id, 'to_alipay_dict'):
                params['service_id'] = self.service_id.to_alipay_dict()
            else:
                params['service_id'] = self.service_id
        if self.source_type:
            if hasattr(self.source_type, 'to_alipay_dict'):
                params['source_type'] = self.source_type.to_alipay_dict()
            else:
                params['source_type'] = self.source_type
        if self.url:
            if hasattr(self.url, 'to_alipay_dict'):
                params['url'] = self.url.to_alipay_dict()
            else:
                params['url'] = self.url
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceEducateSchoolserviceModifyModel()
        if 'content_id' in d:
            o.content_id = d['content_id']
        if 'name' in d:
            o.name = d['name']
        if 'out_service_id' in d:
            o.out_service_id = d['out_service_id']
        if 'service_app_id' in d:
            o.service_app_id = d['service_app_id']
        if 'service_id' in d:
            o.service_id = d['service_id']
        if 'source_type' in d:
            o.source_type = d['source_type']
        if 'url' in d:
            o.url = d['url']
        return o


