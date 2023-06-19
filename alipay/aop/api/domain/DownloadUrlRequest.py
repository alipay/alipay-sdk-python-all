#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class DownloadUrlRequest(object):

    def __init__(self):
        self._expire = None
        self._file_id = None

    @property
    def expire(self):
        return self._expire

    @expire.setter
    def expire(self, value):
        self._expire = value
    @property
    def file_id(self):
        return self._file_id

    @file_id.setter
    def file_id(self, value):
        self._file_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.expire:
            if hasattr(self.expire, 'to_alipay_dict'):
                params['expire'] = self.expire.to_alipay_dict()
            else:
                params['expire'] = self.expire
        if self.file_id:
            if hasattr(self.file_id, 'to_alipay_dict'):
                params['file_id'] = self.file_id.to_alipay_dict()
            else:
                params['file_id'] = self.file_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DownloadUrlRequest()
        if 'expire' in d:
            o.expire = d['expire']
        if 'file_id' in d:
            o.file_id = d['file_id']
        return o


