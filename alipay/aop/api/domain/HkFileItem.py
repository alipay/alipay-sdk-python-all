#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class HkFileItem(object):

    def __init__(self):
        self._doc_type = None
        self._file_content = None
        self._file_id = None
        self._file_index = None
        self._file_name = None
        self._file_sha_256 = None
        self._file_size = None
        self._file_type = None
        self._file_url = None
        self._original_copy_indicator = None

    @property
    def doc_type(self):
        return self._doc_type

    @doc_type.setter
    def doc_type(self, value):
        self._doc_type = value
    @property
    def file_content(self):
        return self._file_content

    @file_content.setter
    def file_content(self, value):
        self._file_content = value
    @property
    def file_id(self):
        return self._file_id

    @file_id.setter
    def file_id(self, value):
        self._file_id = value
    @property
    def file_index(self):
        return self._file_index

    @file_index.setter
    def file_index(self, value):
        self._file_index = value
    @property
    def file_name(self):
        return self._file_name

    @file_name.setter
    def file_name(self, value):
        self._file_name = value
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
    def original_copy_indicator(self):
        return self._original_copy_indicator

    @original_copy_indicator.setter
    def original_copy_indicator(self, value):
        self._original_copy_indicator = value


    def to_alipay_dict(self):
        params = dict()
        if self.doc_type:
            if hasattr(self.doc_type, 'to_alipay_dict'):
                params['doc_type'] = self.doc_type.to_alipay_dict()
            else:
                params['doc_type'] = self.doc_type
        if self.file_content:
            if hasattr(self.file_content, 'to_alipay_dict'):
                params['file_content'] = self.file_content.to_alipay_dict()
            else:
                params['file_content'] = self.file_content
        if self.file_id:
            if hasattr(self.file_id, 'to_alipay_dict'):
                params['file_id'] = self.file_id.to_alipay_dict()
            else:
                params['file_id'] = self.file_id
        if self.file_index:
            if hasattr(self.file_index, 'to_alipay_dict'):
                params['file_index'] = self.file_index.to_alipay_dict()
            else:
                params['file_index'] = self.file_index
        if self.file_name:
            if hasattr(self.file_name, 'to_alipay_dict'):
                params['file_name'] = self.file_name.to_alipay_dict()
            else:
                params['file_name'] = self.file_name
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
        if self.original_copy_indicator:
            if hasattr(self.original_copy_indicator, 'to_alipay_dict'):
                params['original_copy_indicator'] = self.original_copy_indicator.to_alipay_dict()
            else:
                params['original_copy_indicator'] = self.original_copy_indicator
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = HkFileItem()
        if 'doc_type' in d:
            o.doc_type = d['doc_type']
        if 'file_content' in d:
            o.file_content = d['file_content']
        if 'file_id' in d:
            o.file_id = d['file_id']
        if 'file_index' in d:
            o.file_index = d['file_index']
        if 'file_name' in d:
            o.file_name = d['file_name']
        if 'file_sha_256' in d:
            o.file_sha_256 = d['file_sha_256']
        if 'file_size' in d:
            o.file_size = d['file_size']
        if 'file_type' in d:
            o.file_type = d['file_type']
        if 'file_url' in d:
            o.file_url = d['file_url']
        if 'original_copy_indicator' in d:
            o.original_copy_indicator = d['original_copy_indicator']
        return o


