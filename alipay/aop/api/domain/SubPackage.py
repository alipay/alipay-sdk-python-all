#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SubPackage(object):

    def __init__(self):
        self._build_package_url = None
        self._new_build_package_url = None
        self._path = None
        self._source_url = None
        self._type = None

    @property
    def build_package_url(self):
        return self._build_package_url

    @build_package_url.setter
    def build_package_url(self, value):
        self._build_package_url = value
    @property
    def new_build_package_url(self):
        return self._new_build_package_url

    @new_build_package_url.setter
    def new_build_package_url(self, value):
        self._new_build_package_url = value
    @property
    def path(self):
        return self._path

    @path.setter
    def path(self, value):
        self._path = value
    @property
    def source_url(self):
        return self._source_url

    @source_url.setter
    def source_url(self, value):
        self._source_url = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value


    def to_alipay_dict(self):
        params = dict()
        if self.build_package_url:
            if hasattr(self.build_package_url, 'to_alipay_dict'):
                params['build_package_url'] = self.build_package_url.to_alipay_dict()
            else:
                params['build_package_url'] = self.build_package_url
        if self.new_build_package_url:
            if hasattr(self.new_build_package_url, 'to_alipay_dict'):
                params['new_build_package_url'] = self.new_build_package_url.to_alipay_dict()
            else:
                params['new_build_package_url'] = self.new_build_package_url
        if self.path:
            if hasattr(self.path, 'to_alipay_dict'):
                params['path'] = self.path.to_alipay_dict()
            else:
                params['path'] = self.path
        if self.source_url:
            if hasattr(self.source_url, 'to_alipay_dict'):
                params['source_url'] = self.source_url.to_alipay_dict()
            else:
                params['source_url'] = self.source_url
        if self.type:
            if hasattr(self.type, 'to_alipay_dict'):
                params['type'] = self.type.to_alipay_dict()
            else:
                params['type'] = self.type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SubPackage()
        if 'build_package_url' in d:
            o.build_package_url = d['build_package_url']
        if 'new_build_package_url' in d:
            o.new_build_package_url = d['new_build_package_url']
        if 'path' in d:
            o.path = d['path']
        if 'source_url' in d:
            o.source_url = d['source_url']
        if 'type' in d:
            o.type = d['type']
        return o


