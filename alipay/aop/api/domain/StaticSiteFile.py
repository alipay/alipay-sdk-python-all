#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class StaticSiteFile(object):

    def __init__(self):
        self._file_id = None
        self._file_name = None
        self._last_modified = None
        self._size = None
        self._status = None

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
    def last_modified(self):
        return self._last_modified

    @last_modified.setter
    def last_modified(self, value):
        self._last_modified = value
    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        self._size = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value


    def to_alipay_dict(self):
        params = dict()
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
        if self.last_modified:
            if hasattr(self.last_modified, 'to_alipay_dict'):
                params['last_modified'] = self.last_modified.to_alipay_dict()
            else:
                params['last_modified'] = self.last_modified
        if self.size:
            if hasattr(self.size, 'to_alipay_dict'):
                params['size'] = self.size.to_alipay_dict()
            else:
                params['size'] = self.size
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = StaticSiteFile()
        if 'file_id' in d:
            o.file_id = d['file_id']
        if 'file_name' in d:
            o.file_name = d['file_name']
        if 'last_modified' in d:
            o.last_modified = d['last_modified']
        if 'size' in d:
            o.size = d['size']
        if 'status' in d:
            o.status = d['status']
        return o


