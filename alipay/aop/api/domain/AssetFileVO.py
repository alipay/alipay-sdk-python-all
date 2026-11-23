#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AssetFileVO(object):

    def __init__(self):
        self._bucket = None
        self._file_key = None
        self._file_md_5 = None
        self._file_sha_256 = None
        self._file_size = None
        self._file_type = None
        self._file_url = None
        self._name = None
        self._sha_256 = None
        self._sort_order = None

    @property
    def bucket(self):
        return self._bucket

    @bucket.setter
    def bucket(self, value):
        self._bucket = value
    @property
    def file_key(self):
        return self._file_key

    @file_key.setter
    def file_key(self, value):
        self._file_key = value
    @property
    def file_md_5(self):
        return self._file_md_5

    @file_md_5.setter
    def file_md_5(self, value):
        self._file_md_5 = value
    @property
    def file_sha_256(self):
        return self._file_sha_256

    @file_sha_256.setter
    def file_sha_256(self, value):
        self._file_sha_256 = value
    @property
    def file_size(self):
        return self._file_size

    @file_size.setter
    def file_size(self, value):
        self._file_size = value
    @property
    def file_type(self):
        return self._file_type

    @file_type.setter
    def file_type(self, value):
        self._file_type = value
    @property
    def file_url(self):
        return self._file_url

    @file_url.setter
    def file_url(self, value):
        self._file_url = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def sha_256(self):
        return self._sha_256

    @sha_256.setter
    def sha_256(self, value):
        self._sha_256 = value
    @property
    def sort_order(self):
        return self._sort_order

    @sort_order.setter
    def sort_order(self, value):
        self._sort_order = value


    def to_alipay_dict(self):
        params = dict()
        if self.bucket:
            if hasattr(self.bucket, 'to_alipay_dict'):
                params['bucket'] = self.bucket.to_alipay_dict()
            else:
                params['bucket'] = self.bucket
        if self.file_key:
            if hasattr(self.file_key, 'to_alipay_dict'):
                params['file_key'] = self.file_key.to_alipay_dict()
            else:
                params['file_key'] = self.file_key
        if self.file_md_5:
            if hasattr(self.file_md_5, 'to_alipay_dict'):
                params['file_md_5'] = self.file_md_5.to_alipay_dict()
            else:
                params['file_md_5'] = self.file_md_5
        if self.file_sha_256:
            if hasattr(self.file_sha_256, 'to_alipay_dict'):
                params['file_sha_256'] = self.file_sha_256.to_alipay_dict()
            else:
                params['file_sha_256'] = self.file_sha_256
        if self.file_size:
            if hasattr(self.file_size, 'to_alipay_dict'):
                params['file_size'] = self.file_size.to_alipay_dict()
            else:
                params['file_size'] = self.file_size
        if self.file_type:
            if hasattr(self.file_type, 'to_alipay_dict'):
                params['file_type'] = self.file_type.to_alipay_dict()
            else:
                params['file_type'] = self.file_type
        if self.file_url:
            if hasattr(self.file_url, 'to_alipay_dict'):
                params['file_url'] = self.file_url.to_alipay_dict()
            else:
                params['file_url'] = self.file_url
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.sha_256:
            if hasattr(self.sha_256, 'to_alipay_dict'):
                params['sha_256'] = self.sha_256.to_alipay_dict()
            else:
                params['sha_256'] = self.sha_256
        if self.sort_order:
            if hasattr(self.sort_order, 'to_alipay_dict'):
                params['sort_order'] = self.sort_order.to_alipay_dict()
            else:
                params['sort_order'] = self.sort_order
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AssetFileVO()
        if 'bucket' in d:
            o.bucket = d['bucket']
        if 'file_key' in d:
            o.file_key = d['file_key']
        if 'file_md_5' in d:
            o.file_md_5 = d['file_md_5']
        if 'file_sha_256' in d:
            o.file_sha_256 = d['file_sha_256']
        if 'file_size' in d:
            o.file_size = d['file_size']
        if 'file_type' in d:
            o.file_type = d['file_type']
        if 'file_url' in d:
            o.file_url = d['file_url']
        if 'name' in d:
            o.name = d['name']
        if 'sha_256' in d:
            o.sha_256 = d['sha_256']
        if 'sort_order' in d:
            o.sort_order = d['sort_order']
        return o


