#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class UserPhotoInfo(object):

    def __init__(self):
        self._file_url = None
        self._keyword = None

    @property
    def file_url(self):
        return self._file_url

    @file_url.setter
    def file_url(self, value):
        self._file_url = value
    @property
    def keyword(self):
        return self._keyword

    @keyword.setter
    def keyword(self, value):
        self._keyword = value


    def to_alipay_dict(self):
        params = dict()
        if self.file_url:
            if hasattr(self.file_url, 'to_alipay_dict'):
                params['file_url'] = self.file_url.to_alipay_dict()
            else:
                params['file_url'] = self.file_url
        if self.keyword:
            if hasattr(self.keyword, 'to_alipay_dict'):
                params['keyword'] = self.keyword.to_alipay_dict()
            else:
                params['keyword'] = self.keyword
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = UserPhotoInfo()
        if 'file_url' in d:
            o.file_url = d['file_url']
        if 'keyword' in d:
            o.keyword = d['keyword']
        return o


