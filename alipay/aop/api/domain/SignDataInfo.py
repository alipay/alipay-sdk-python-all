#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.FileSignature import FileSignature


class SignDataInfo(object):

    def __init__(self):
        self._data_id = None
        self._data_name = None
        self._data_type = None
        self._file_type = None
        self._oss_file_id = None
        self._preview_url = None
        self._signature_list = None
        self._source_data = None

    @property
    def data_id(self):
        return self._data_id

    @data_id.setter
    def data_id(self, value):
        self._data_id = value
    @property
    def data_name(self):
        return self._data_name

    @data_name.setter
    def data_name(self, value):
        self._data_name = value
    @property
    def data_type(self):
        return self._data_type

    @data_type.setter
    def data_type(self, value):
        self._data_type = value
    @property
    def file_type(self):
        return self._file_type

    @file_type.setter
    def file_type(self, value):
        self._file_type = value
    @property
    def oss_file_id(self):
        return self._oss_file_id

    @oss_file_id.setter
    def oss_file_id(self, value):
        self._oss_file_id = value
    @property
    def preview_url(self):
        return self._preview_url

    @preview_url.setter
    def preview_url(self, value):
        self._preview_url = value
    @property
    def signature_list(self):
        return self._signature_list

    @signature_list.setter
    def signature_list(self, value):
        if isinstance(value, list):
            self._signature_list = list()
            for i in value:
                if isinstance(i, FileSignature):
                    self._signature_list.append(i)
                else:
                    self._signature_list.append(FileSignature.from_alipay_dict(i))
    @property
    def source_data(self):
        return self._source_data

    @source_data.setter
    def source_data(self, value):
        self._source_data = value


    def to_alipay_dict(self):
        params = dict()
        if self.data_id:
            if hasattr(self.data_id, 'to_alipay_dict'):
                params['data_id'] = self.data_id.to_alipay_dict()
            else:
                params['data_id'] = self.data_id
        if self.data_name:
            if hasattr(self.data_name, 'to_alipay_dict'):
                params['data_name'] = self.data_name.to_alipay_dict()
            else:
                params['data_name'] = self.data_name
        if self.data_type:
            if hasattr(self.data_type, 'to_alipay_dict'):
                params['data_type'] = self.data_type.to_alipay_dict()
            else:
                params['data_type'] = self.data_type
        if self.file_type:
            if hasattr(self.file_type, 'to_alipay_dict'):
                params['file_type'] = self.file_type.to_alipay_dict()
            else:
                params['file_type'] = self.file_type
        if self.oss_file_id:
            if hasattr(self.oss_file_id, 'to_alipay_dict'):
                params['oss_file_id'] = self.oss_file_id.to_alipay_dict()
            else:
                params['oss_file_id'] = self.oss_file_id
        if self.preview_url:
            if hasattr(self.preview_url, 'to_alipay_dict'):
                params['preview_url'] = self.preview_url.to_alipay_dict()
            else:
                params['preview_url'] = self.preview_url
        if self.signature_list:
            if isinstance(self.signature_list, list):
                for i in range(0, len(self.signature_list)):
                    element = self.signature_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.signature_list[i] = element.to_alipay_dict()
            if hasattr(self.signature_list, 'to_alipay_dict'):
                params['signature_list'] = self.signature_list.to_alipay_dict()
            else:
                params['signature_list'] = self.signature_list
        if self.source_data:
            if hasattr(self.source_data, 'to_alipay_dict'):
                params['source_data'] = self.source_data.to_alipay_dict()
            else:
                params['source_data'] = self.source_data
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SignDataInfo()
        if 'data_id' in d:
            o.data_id = d['data_id']
        if 'data_name' in d:
            o.data_name = d['data_name']
        if 'data_type' in d:
            o.data_type = d['data_type']
        if 'file_type' in d:
            o.file_type = d['file_type']
        if 'oss_file_id' in d:
            o.oss_file_id = d['oss_file_id']
        if 'preview_url' in d:
            o.preview_url = d['preview_url']
        if 'signature_list' in d:
            o.signature_list = d['signature_list']
        if 'source_data' in d:
            o.source_data = d['source_data']
        return o


