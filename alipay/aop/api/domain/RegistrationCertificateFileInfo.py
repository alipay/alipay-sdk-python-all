#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RegistrationCertificateFileInfo(object):

    def __init__(self):
        self._file_path = None
        self._tag = None

    @property
    def file_path(self):
        return self._file_path

    @file_path.setter
    def file_path(self, value):
        self._file_path = value
    @property
    def tag(self):
        return self._tag

    @tag.setter
    def tag(self, value):
        self._tag = value


    def to_alipay_dict(self):
        params = dict()
        if self.file_path:
            if hasattr(self.file_path, 'to_alipay_dict'):
                params['file_path'] = self.file_path.to_alipay_dict()
            else:
                params['file_path'] = self.file_path
        if self.tag:
            if hasattr(self.tag, 'to_alipay_dict'):
                params['tag'] = self.tag.to_alipay_dict()
            else:
                params['tag'] = self.tag
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RegistrationCertificateFileInfo()
        if 'file_path' in d:
            o.file_path = d['file_path']
        if 'tag' in d:
            o.tag = d['tag']
        return o


