#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ObTemplateParamRequest import ObTemplateParamRequest


class AnttechOceanbaseTemplateInstanceUploadModel(object):

    def __init__(self):
        self._biz_id = None
        self._biz_key = None
        self._biz_type = None
        self._channel = None
        self._config_id = None
        self._file_name = None
        self._file_type = None
        self._fill_data = None
        self._upload_prefix = None

    @property
    def biz_id(self):
        return self._biz_id

    @biz_id.setter
    def biz_id(self, value):
        self._biz_id = value
    @property
    def biz_key(self):
        return self._biz_key

    @biz_key.setter
    def biz_key(self, value):
        self._biz_key = value
    @property
    def biz_type(self):
        return self._biz_type

    @biz_type.setter
    def biz_type(self, value):
        self._biz_type = value
    @property
    def channel(self):
        return self._channel

    @channel.setter
    def channel(self, value):
        self._channel = value
    @property
    def config_id(self):
        return self._config_id

    @config_id.setter
    def config_id(self, value):
        self._config_id = value
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
    def fill_data(self):
        return self._fill_data

    @fill_data.setter
    def fill_data(self, value):
        if isinstance(value, list):
            self._fill_data = list()
            for i in value:
                if isinstance(i, ObTemplateParamRequest):
                    self._fill_data.append(i)
                else:
                    self._fill_data.append(ObTemplateParamRequest.from_alipay_dict(i))
    @property
    def upload_prefix(self):
        return self._upload_prefix

    @upload_prefix.setter
    def upload_prefix(self, value):
        self._upload_prefix = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_id:
            if hasattr(self.biz_id, 'to_alipay_dict'):
                params['biz_id'] = self.biz_id.to_alipay_dict()
            else:
                params['biz_id'] = self.biz_id
        if self.biz_key:
            if hasattr(self.biz_key, 'to_alipay_dict'):
                params['biz_key'] = self.biz_key.to_alipay_dict()
            else:
                params['biz_key'] = self.biz_key
        if self.biz_type:
            if hasattr(self.biz_type, 'to_alipay_dict'):
                params['biz_type'] = self.biz_type.to_alipay_dict()
            else:
                params['biz_type'] = self.biz_type
        if self.channel:
            if hasattr(self.channel, 'to_alipay_dict'):
                params['channel'] = self.channel.to_alipay_dict()
            else:
                params['channel'] = self.channel
        if self.config_id:
            if hasattr(self.config_id, 'to_alipay_dict'):
                params['config_id'] = self.config_id.to_alipay_dict()
            else:
                params['config_id'] = self.config_id
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
        if self.fill_data:
            if isinstance(self.fill_data, list):
                for i in range(0, len(self.fill_data)):
                    element = self.fill_data[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.fill_data[i] = element.to_alipay_dict()
            if hasattr(self.fill_data, 'to_alipay_dict'):
                params['fill_data'] = self.fill_data.to_alipay_dict()
            else:
                params['fill_data'] = self.fill_data
        if self.upload_prefix:
            if hasattr(self.upload_prefix, 'to_alipay_dict'):
                params['upload_prefix'] = self.upload_prefix.to_alipay_dict()
            else:
                params['upload_prefix'] = self.upload_prefix
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AnttechOceanbaseTemplateInstanceUploadModel()
        if 'biz_id' in d:
            o.biz_id = d['biz_id']
        if 'biz_key' in d:
            o.biz_key = d['biz_key']
        if 'biz_type' in d:
            o.biz_type = d['biz_type']
        if 'channel' in d:
            o.channel = d['channel']
        if 'config_id' in d:
            o.config_id = d['config_id']
        if 'file_name' in d:
            o.file_name = d['file_name']
        if 'file_type' in d:
            o.file_type = d['file_type']
        if 'fill_data' in d:
            o.fill_data = d['fill_data']
        if 'upload_prefix' in d:
            o.upload_prefix = d['upload_prefix']
        return o


