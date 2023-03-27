#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AttachmentFile(object):

    def __init__(self):
        self._file_name = None
        self._oss_key = None

    @property
    def file_name(self):
        return self._file_name

    @file_name.setter
    def file_name(self, value):
        self._file_name = value
    @property
    def oss_key(self):
        return self._oss_key

    @oss_key.setter
    def oss_key(self, value):
        self._oss_key = value


    def to_alipay_dict(self):
        params = dict()
        if self.file_name:
            if hasattr(self.file_name, 'to_alipay_dict'):
                params['file_name'] = self.file_name.to_alipay_dict()
            else:
                params['file_name'] = self.file_name
        if self.oss_key:
            if hasattr(self.oss_key, 'to_alipay_dict'):
                params['oss_key'] = self.oss_key.to_alipay_dict()
            else:
                params['oss_key'] = self.oss_key
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AttachmentFile()
        if 'file_name' in d:
            o.file_name = d['file_name']
        if 'oss_key' in d:
            o.oss_key = d['oss_key']
        return o


