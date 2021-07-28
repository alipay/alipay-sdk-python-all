#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class JsApiBaseDTO(object):

    def __init__(self):
        self._appx_min_version = None
        self._bundle_id = None
        self._bundle_min_version = None
        self._cn_name = None
        self._demo_url = None
        self._description = None
        self._en_name = None
        self._general = None
        self._is_async = None
        self._jsapi_version = None
        self._open_range = None
        self._owner = None
        self._sample_code = None

    @property
    def appx_min_version(self):
        return self._appx_min_version

    @appx_min_version.setter
    def appx_min_version(self, value):
        self._appx_min_version = value
    @property
    def bundle_id(self):
        return self._bundle_id

    @bundle_id.setter
    def bundle_id(self, value):
        self._bundle_id = value
    @property
    def bundle_min_version(self):
        return self._bundle_min_version

    @bundle_min_version.setter
    def bundle_min_version(self, value):
        self._bundle_min_version = value
    @property
    def cn_name(self):
        return self._cn_name

    @cn_name.setter
    def cn_name(self, value):
        self._cn_name = value
    @property
    def demo_url(self):
        return self._demo_url

    @demo_url.setter
    def demo_url(self, value):
        self._demo_url = value
    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        self._description = value
    @property
    def en_name(self):
        return self._en_name

    @en_name.setter
    def en_name(self, value):
        self._en_name = value
    @property
    def general(self):
        return self._general

    @general.setter
    def general(self, value):
        self._general = value
    @property
    def is_async(self):
        return self._is_async

    @is_async.setter
    def is_async(self, value):
        self._is_async = value
    @property
    def jsapi_version(self):
        return self._jsapi_version

    @jsapi_version.setter
    def jsapi_version(self, value):
        self._jsapi_version = value
    @property
    def open_range(self):
        return self._open_range

    @open_range.setter
    def open_range(self, value):
        self._open_range = value
    @property
    def owner(self):
        return self._owner

    @owner.setter
    def owner(self, value):
        self._owner = value
    @property
    def sample_code(self):
        return self._sample_code

    @sample_code.setter
    def sample_code(self, value):
        self._sample_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.appx_min_version:
            if hasattr(self.appx_min_version, 'to_alipay_dict'):
                params['appx_min_version'] = self.appx_min_version.to_alipay_dict()
            else:
                params['appx_min_version'] = self.appx_min_version
        if self.bundle_id:
            if hasattr(self.bundle_id, 'to_alipay_dict'):
                params['bundle_id'] = self.bundle_id.to_alipay_dict()
            else:
                params['bundle_id'] = self.bundle_id
        if self.bundle_min_version:
            if hasattr(self.bundle_min_version, 'to_alipay_dict'):
                params['bundle_min_version'] = self.bundle_min_version.to_alipay_dict()
            else:
                params['bundle_min_version'] = self.bundle_min_version
        if self.cn_name:
            if hasattr(self.cn_name, 'to_alipay_dict'):
                params['cn_name'] = self.cn_name.to_alipay_dict()
            else:
                params['cn_name'] = self.cn_name
        if self.demo_url:
            if hasattr(self.demo_url, 'to_alipay_dict'):
                params['demo_url'] = self.demo_url.to_alipay_dict()
            else:
                params['demo_url'] = self.demo_url
        if self.description:
            if hasattr(self.description, 'to_alipay_dict'):
                params['description'] = self.description.to_alipay_dict()
            else:
                params['description'] = self.description
        if self.en_name:
            if hasattr(self.en_name, 'to_alipay_dict'):
                params['en_name'] = self.en_name.to_alipay_dict()
            else:
                params['en_name'] = self.en_name
        if self.general:
            if hasattr(self.general, 'to_alipay_dict'):
                params['general'] = self.general.to_alipay_dict()
            else:
                params['general'] = self.general
        if self.is_async:
            if hasattr(self.is_async, 'to_alipay_dict'):
                params['is_async'] = self.is_async.to_alipay_dict()
            else:
                params['is_async'] = self.is_async
        if self.jsapi_version:
            if hasattr(self.jsapi_version, 'to_alipay_dict'):
                params['jsapi_version'] = self.jsapi_version.to_alipay_dict()
            else:
                params['jsapi_version'] = self.jsapi_version
        if self.open_range:
            if hasattr(self.open_range, 'to_alipay_dict'):
                params['open_range'] = self.open_range.to_alipay_dict()
            else:
                params['open_range'] = self.open_range
        if self.owner:
            if hasattr(self.owner, 'to_alipay_dict'):
                params['owner'] = self.owner.to_alipay_dict()
            else:
                params['owner'] = self.owner
        if self.sample_code:
            if hasattr(self.sample_code, 'to_alipay_dict'):
                params['sample_code'] = self.sample_code.to_alipay_dict()
            else:
                params['sample_code'] = self.sample_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = JsApiBaseDTO()
        if 'appx_min_version' in d:
            o.appx_min_version = d['appx_min_version']
        if 'bundle_id' in d:
            o.bundle_id = d['bundle_id']
        if 'bundle_min_version' in d:
            o.bundle_min_version = d['bundle_min_version']
        if 'cn_name' in d:
            o.cn_name = d['cn_name']
        if 'demo_url' in d:
            o.demo_url = d['demo_url']
        if 'description' in d:
            o.description = d['description']
        if 'en_name' in d:
            o.en_name = d['en_name']
        if 'general' in d:
            o.general = d['general']
        if 'is_async' in d:
            o.is_async = d['is_async']
        if 'jsapi_version' in d:
            o.jsapi_version = d['jsapi_version']
        if 'open_range' in d:
            o.open_range = d['open_range']
        if 'owner' in d:
            o.owner = d['owner']
        if 'sample_code' in d:
            o.sample_code = d['sample_code']
        return o


