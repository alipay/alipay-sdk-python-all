#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommercePropertyRiskdetectContentSyncModel(object):

    def __init__(self):
        self._create_time = None
        self._device_id = None
        self._file_key = None
        self._file_url = None
        self._out_content_id = None
        self._out_device_id = None
        self._upload_mode = None

    @property
    def create_time(self):
        return self._create_time

    @create_time.setter
    def create_time(self, value):
        self._create_time = value
    @property
    def device_id(self):
        return self._device_id

    @device_id.setter
    def device_id(self, value):
        self._device_id = value
    @property
    def file_key(self):
        return self._file_key

    @file_key.setter
    def file_key(self, value):
        self._file_key = value
    @property
    def file_url(self):
        return self._file_url

    @file_url.setter
    def file_url(self, value):
        self._file_url = value
    @property
    def out_content_id(self):
        return self._out_content_id

    @out_content_id.setter
    def out_content_id(self, value):
        self._out_content_id = value
    @property
    def out_device_id(self):
        return self._out_device_id

    @out_device_id.setter
    def out_device_id(self, value):
        self._out_device_id = value
    @property
    def upload_mode(self):
        return self._upload_mode

    @upload_mode.setter
    def upload_mode(self, value):
        self._upload_mode = value


    def to_alipay_dict(self):
        params = dict()
        if self.create_time:
            if hasattr(self.create_time, 'to_alipay_dict'):
                params['create_time'] = self.create_time.to_alipay_dict()
            else:
                params['create_time'] = self.create_time
        if self.device_id:
            if hasattr(self.device_id, 'to_alipay_dict'):
                params['device_id'] = self.device_id.to_alipay_dict()
            else:
                params['device_id'] = self.device_id
        if self.file_key:
            if hasattr(self.file_key, 'to_alipay_dict'):
                params['file_key'] = self.file_key.to_alipay_dict()
            else:
                params['file_key'] = self.file_key
        if self.file_url:
            if hasattr(self.file_url, 'to_alipay_dict'):
                params['file_url'] = self.file_url.to_alipay_dict()
            else:
                params['file_url'] = self.file_url
        if self.out_content_id:
            if hasattr(self.out_content_id, 'to_alipay_dict'):
                params['out_content_id'] = self.out_content_id.to_alipay_dict()
            else:
                params['out_content_id'] = self.out_content_id
        if self.out_device_id:
            if hasattr(self.out_device_id, 'to_alipay_dict'):
                params['out_device_id'] = self.out_device_id.to_alipay_dict()
            else:
                params['out_device_id'] = self.out_device_id
        if self.upload_mode:
            if hasattr(self.upload_mode, 'to_alipay_dict'):
                params['upload_mode'] = self.upload_mode.to_alipay_dict()
            else:
                params['upload_mode'] = self.upload_mode
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommercePropertyRiskdetectContentSyncModel()
        if 'create_time' in d:
            o.create_time = d['create_time']
        if 'device_id' in d:
            o.device_id = d['device_id']
        if 'file_key' in d:
            o.file_key = d['file_key']
        if 'file_url' in d:
            o.file_url = d['file_url']
        if 'out_content_id' in d:
            o.out_content_id = d['out_content_id']
        if 'out_device_id' in d:
            o.out_device_id = d['out_device_id']
        if 'upload_mode' in d:
            o.upload_mode = d['upload_mode']
        return o


