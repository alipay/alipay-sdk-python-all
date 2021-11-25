#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class FileUploadExtraParam(object):

    def __init__(self):
        self._extern_upload = None
        self._file_encrypt_type = None

    @property
    def extern_upload(self):
        return self._extern_upload

    @extern_upload.setter
    def extern_upload(self, value):
        self._extern_upload = value
    @property
    def file_encrypt_type(self):
        return self._file_encrypt_type

    @file_encrypt_type.setter
    def file_encrypt_type(self, value):
        self._file_encrypt_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.extern_upload:
            if hasattr(self.extern_upload, 'to_alipay_dict'):
                params['extern_upload'] = self.extern_upload.to_alipay_dict()
            else:
                params['extern_upload'] = self.extern_upload
        if self.file_encrypt_type:
            if hasattr(self.file_encrypt_type, 'to_alipay_dict'):
                params['file_encrypt_type'] = self.file_encrypt_type.to_alipay_dict()
            else:
                params['file_encrypt_type'] = self.file_encrypt_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = FileUploadExtraParam()
        if 'extern_upload' in d:
            o.extern_upload = d['extern_upload']
        if 'file_encrypt_type' in d:
            o.file_encrypt_type = d['file_encrypt_type']
        return o


