#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MallFile(object):

    def __init__(self):
        self._file_md_5 = None
        self._file_name = None
        self._file_url = None

    @property
    def file_md_5(self):
        return self._file_md_5

    @file_md_5.setter
    def file_md_5(self, value):
        self._file_md_5 = value
    @property
    def file_name(self):
        return self._file_name

    @file_name.setter
    def file_name(self, value):
        self._file_name = value
    @property
    def file_url(self):
        return self._file_url

    @file_url.setter
    def file_url(self, value):
        self._file_url = value


    def to_alipay_dict(self):
        params = dict()
        if self.file_md_5:
            if hasattr(self.file_md_5, 'to_alipay_dict'):
                params['file_md_5'] = self.file_md_5.to_alipay_dict()
            else:
                params['file_md_5'] = self.file_md_5
        if self.file_name:
            if hasattr(self.file_name, 'to_alipay_dict'):
                params['file_name'] = self.file_name.to_alipay_dict()
            else:
                params['file_name'] = self.file_name
        if self.file_url:
            if hasattr(self.file_url, 'to_alipay_dict'):
                params['file_url'] = self.file_url.to_alipay_dict()
            else:
                params['file_url'] = self.file_url
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MallFile()
        if 'file_md_5' in d:
            o.file_md_5 = d['file_md_5']
        if 'file_name' in d:
            o.file_name = d['file_name']
        if 'file_url' in d:
            o.file_url = d['file_url']
        return o


