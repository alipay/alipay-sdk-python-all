#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class FileDTO(object):

    def __init__(self):
        self._file_download_url = None
        self._file_name = None

    @property
    def file_download_url(self):
        return self._file_download_url

    @file_download_url.setter
    def file_download_url(self, value):
        self._file_download_url = value
    @property
    def file_name(self):
        return self._file_name

    @file_name.setter
    def file_name(self, value):
        self._file_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.file_download_url:
            if hasattr(self.file_download_url, 'to_alipay_dict'):
                params['file_download_url'] = self.file_download_url.to_alipay_dict()
            else:
                params['file_download_url'] = self.file_download_url
        if self.file_name:
            if hasattr(self.file_name, 'to_alipay_dict'):
                params['file_name'] = self.file_name.to_alipay_dict()
            else:
                params['file_name'] = self.file_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = FileDTO()
        if 'file_download_url' in d:
            o.file_download_url = d['file_download_url']
        if 'file_name' in d:
            o.file_name = d['file_name']
        return o


