#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SignedFileInfo(object):

    def __init__(self):
        self._expired_time = None
        self._file_name = None
        self._file_type = None
        self._file_url = None
        self._gmt_time = None
        self._inner_data_id = None
        self._out_data_id = None
        self._signed_data = None
        self._source_type = None

    @property
    def expired_time(self):
        return self._expired_time

    @expired_time.setter
    def expired_time(self, value):
        self._expired_time = value
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
    def file_url(self):
        return self._file_url

    @file_url.setter
    def file_url(self, value):
        self._file_url = value
    @property
    def gmt_time(self):
        return self._gmt_time

    @gmt_time.setter
    def gmt_time(self, value):
        self._gmt_time = value
    @property
    def inner_data_id(self):
        return self._inner_data_id

    @inner_data_id.setter
    def inner_data_id(self, value):
        self._inner_data_id = value
    @property
    def out_data_id(self):
        return self._out_data_id

    @out_data_id.setter
    def out_data_id(self, value):
        self._out_data_id = value
    @property
    def signed_data(self):
        return self._signed_data

    @signed_data.setter
    def signed_data(self, value):
        self._signed_data = value
    @property
    def source_type(self):
        return self._source_type

    @source_type.setter
    def source_type(self, value):
        self._source_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.expired_time:
            if hasattr(self.expired_time, 'to_alipay_dict'):
                params['expired_time'] = self.expired_time.to_alipay_dict()
            else:
                params['expired_time'] = self.expired_time
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
        if self.file_url:
            if hasattr(self.file_url, 'to_alipay_dict'):
                params['file_url'] = self.file_url.to_alipay_dict()
            else:
                params['file_url'] = self.file_url
        if self.gmt_time:
            if hasattr(self.gmt_time, 'to_alipay_dict'):
                params['gmt_time'] = self.gmt_time.to_alipay_dict()
            else:
                params['gmt_time'] = self.gmt_time
        if self.inner_data_id:
            if hasattr(self.inner_data_id, 'to_alipay_dict'):
                params['inner_data_id'] = self.inner_data_id.to_alipay_dict()
            else:
                params['inner_data_id'] = self.inner_data_id
        if self.out_data_id:
            if hasattr(self.out_data_id, 'to_alipay_dict'):
                params['out_data_id'] = self.out_data_id.to_alipay_dict()
            else:
                params['out_data_id'] = self.out_data_id
        if self.signed_data:
            if hasattr(self.signed_data, 'to_alipay_dict'):
                params['signed_data'] = self.signed_data.to_alipay_dict()
            else:
                params['signed_data'] = self.signed_data
        if self.source_type:
            if hasattr(self.source_type, 'to_alipay_dict'):
                params['source_type'] = self.source_type.to_alipay_dict()
            else:
                params['source_type'] = self.source_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SignedFileInfo()
        if 'expired_time' in d:
            o.expired_time = d['expired_time']
        if 'file_name' in d:
            o.file_name = d['file_name']
        if 'file_type' in d:
            o.file_type = d['file_type']
        if 'file_url' in d:
            o.file_url = d['file_url']
        if 'gmt_time' in d:
            o.gmt_time = d['gmt_time']
        if 'inner_data_id' in d:
            o.inner_data_id = d['inner_data_id']
        if 'out_data_id' in d:
            o.out_data_id = d['out_data_id']
        if 'signed_data' in d:
            o.signed_data = d['signed_data']
        if 'source_type' in d:
            o.source_type = d['source_type']
        return o


