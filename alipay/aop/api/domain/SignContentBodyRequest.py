#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SignContentBodyRequest(object):

    def __init__(self):
        self._file_name = None
        self._plain_content = None
        self._sha_content = None

    @property
    def file_name(self):
        return self._file_name

    @file_name.setter
    def file_name(self, value):
        self._file_name = value
    @property
    def plain_content(self):
        return self._plain_content

    @plain_content.setter
    def plain_content(self, value):
        self._plain_content = value
    @property
    def sha_content(self):
        return self._sha_content

    @sha_content.setter
    def sha_content(self, value):
        self._sha_content = value


    def to_alipay_dict(self):
        params = dict()
        if self.file_name:
            if hasattr(self.file_name, 'to_alipay_dict'):
                params['file_name'] = self.file_name.to_alipay_dict()
            else:
                params['file_name'] = self.file_name
        if self.plain_content:
            if hasattr(self.plain_content, 'to_alipay_dict'):
                params['plain_content'] = self.plain_content.to_alipay_dict()
            else:
                params['plain_content'] = self.plain_content
        if self.sha_content:
            if hasattr(self.sha_content, 'to_alipay_dict'):
                params['sha_content'] = self.sha_content.to_alipay_dict()
            else:
                params['sha_content'] = self.sha_content
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SignContentBodyRequest()
        if 'file_name' in d:
            o.file_name = d['file_name']
        if 'plain_content' in d:
            o.plain_content = d['plain_content']
        if 'sha_content' in d:
            o.sha_content = d['sha_content']
        return o


