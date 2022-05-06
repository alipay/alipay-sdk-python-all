#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SubPackageInfo(object):

    def __init__(self):
        self._builded_package_url = None
        self._new_builded_package_url = None
        self._new_size = None
        self._path = None
        self._size = None
        self._source_url = None
        self._type = None

    @property
    def builded_package_url(self):
        return self._builded_package_url

    @builded_package_url.setter
    def builded_package_url(self, value):
        self._builded_package_url = value
    @property
    def new_builded_package_url(self):
        return self._new_builded_package_url

    @new_builded_package_url.setter
    def new_builded_package_url(self, value):
        self._new_builded_package_url = value
    @property
    def new_size(self):
        return self._new_size

    @new_size.setter
    def new_size(self, value):
        self._new_size = value
    @property
    def path(self):
        return self._path

    @path.setter
    def path(self, value):
        self._path = value
    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        self._size = value
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
        if self.builded_package_url:
            if hasattr(self.builded_package_url, 'to_alipay_dict'):
                params['builded_package_url'] = self.builded_package_url.to_alipay_dict()
            else:
                params['builded_package_url'] = self.builded_package_url
        if self.new_builded_package_url:
            if hasattr(self.new_builded_package_url, 'to_alipay_dict'):
                params['new_builded_package_url'] = self.new_builded_package_url.to_alipay_dict()
            else:
                params['new_builded_package_url'] = self.new_builded_package_url
        if self.new_size:
            if hasattr(self.new_size, 'to_alipay_dict'):
                params['new_size'] = self.new_size.to_alipay_dict()
            else:
                params['new_size'] = self.new_size
        if self.path:
            if hasattr(self.path, 'to_alipay_dict'):
                params['path'] = self.path.to_alipay_dict()
            else:
                params['path'] = self.path
        if self.size:
            if hasattr(self.size, 'to_alipay_dict'):
                params['size'] = self.size.to_alipay_dict()
            else:
                params['size'] = self.size
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
        o = SubPackageInfo()
        if 'builded_package_url' in d:
            o.builded_package_url = d['builded_package_url']
        if 'new_builded_package_url' in d:
            o.new_builded_package_url = d['new_builded_package_url']
        if 'new_size' in d:
            o.new_size = d['new_size']
        if 'path' in d:
            o.path = d['path']
        if 'size' in d:
            o.size = d['size']
        if 'source_url' in d:
            o.source_url = d['source_url']
        if 'type' in d:
            o.type = d['type']
        return o


