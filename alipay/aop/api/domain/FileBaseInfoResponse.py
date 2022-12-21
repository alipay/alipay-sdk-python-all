#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class FileBaseInfoResponse(object):

    def __init__(self):
        self._absolute_path = None
        self._download_url = None
        self._enable = None
        self._file_id = None
        self._file_name = None
        self._file_type = None
        self._path = None

    @property
    def absolute_path(self):
        return self._absolute_path

    @absolute_path.setter
    def absolute_path(self, value):
        self._absolute_path = value
    @property
    def download_url(self):
        return self._download_url

    @download_url.setter
    def download_url(self, value):
        self._download_url = value
    @property
    def enable(self):
        return self._enable

    @enable.setter
    def enable(self, value):
        self._enable = value
    @property
    def file_id(self):
        return self._file_id

    @file_id.setter
    def file_id(self, value):
        self._file_id = value
    @property
    def file_name(self):
        return self._file_name

    @file_name.setter
    def file_name(self, value):
        self._file_name = value
    @property
    def file_type(self):
        return self._file_type

    @file_type.setter
    def file_type(self, value):
        self._file_type = value
    @property
    def path(self):
        return self._path

    @path.setter
    def path(self, value):
        self._path = value


    def to_alipay_dict(self):
        params = dict()
        if self.absolute_path:
            if hasattr(self.absolute_path, 'to_alipay_dict'):
                params['absolute_path'] = self.absolute_path.to_alipay_dict()
            else:
                params['absolute_path'] = self.absolute_path
        if self.download_url:
            if hasattr(self.download_url, 'to_alipay_dict'):
                params['download_url'] = self.download_url.to_alipay_dict()
            else:
                params['download_url'] = self.download_url
        if self.enable:
            if hasattr(self.enable, 'to_alipay_dict'):
                params['enable'] = self.enable.to_alipay_dict()
            else:
                params['enable'] = self.enable
        if self.file_id:
            if hasattr(self.file_id, 'to_alipay_dict'):
                params['file_id'] = self.file_id.to_alipay_dict()
            else:
                params['file_id'] = self.file_id
        if self.file_name:
            if hasattr(self.file_name, 'to_alipay_dict'):
                params['file_name'] = self.file_name.to_alipay_dict()
            else:
                params['file_name'] = self.file_name
        if self.file_type:
            if hasattr(self.file_type, 'to_alipay_dict'):
                params['file_type'] = self.file_type.to_alipay_dict()
            else:
                params['file_type'] = self.file_type
        if self.path:
            if hasattr(self.path, 'to_alipay_dict'):
                params['path'] = self.path.to_alipay_dict()
            else:
                params['path'] = self.path
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = FileBaseInfoResponse()
        if 'absolute_path' in d:
            o.absolute_path = d['absolute_path']
        if 'download_url' in d:
            o.download_url = d['download_url']
        if 'enable' in d:
            o.enable = d['enable']
        if 'file_id' in d:
            o.file_id = d['file_id']
        if 'file_name' in d:
            o.file_name = d['file_name']
        if 'file_type' in d:
            o.file_type = d['file_type']
        if 'path' in d:
            o.path = d['path']
        return o


