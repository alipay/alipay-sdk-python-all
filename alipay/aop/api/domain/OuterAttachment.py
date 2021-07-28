#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class OuterAttachment(object):

    def __init__(self):
        self._attachment_type = None
        self._file_key = None
        self._file_url = None
        self._validate_end_time = None
        self._validate_start_time = None

    @property
    def attachment_type(self):
        return self._attachment_type

    @attachment_type.setter
    def attachment_type(self, value):
        self._attachment_type = value
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
    def validate_end_time(self):
        return self._validate_end_time

    @validate_end_time.setter
    def validate_end_time(self, value):
        self._validate_end_time = value
    @property
    def validate_start_time(self):
        return self._validate_start_time

    @validate_start_time.setter
    def validate_start_time(self, value):
        self._validate_start_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.attachment_type:
            if hasattr(self.attachment_type, 'to_alipay_dict'):
                params['attachment_type'] = self.attachment_type.to_alipay_dict()
            else:
                params['attachment_type'] = self.attachment_type
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
        if self.validate_end_time:
            if hasattr(self.validate_end_time, 'to_alipay_dict'):
                params['validate_end_time'] = self.validate_end_time.to_alipay_dict()
            else:
                params['validate_end_time'] = self.validate_end_time
        if self.validate_start_time:
            if hasattr(self.validate_start_time, 'to_alipay_dict'):
                params['validate_start_time'] = self.validate_start_time.to_alipay_dict()
            else:
                params['validate_start_time'] = self.validate_start_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = OuterAttachment()
        if 'attachment_type' in d:
            o.attachment_type = d['attachment_type']
        if 'file_key' in d:
            o.file_key = d['file_key']
        if 'file_url' in d:
            o.file_url = d['file_url']
        if 'validate_end_time' in d:
            o.validate_end_time = d['validate_end_time']
        if 'validate_start_time' in d:
            o.validate_start_time = d['validate_start_time']
        return o


