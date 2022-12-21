#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SignedFileInfoDTO(object):

    def __init__(self):
        self._e_signed_file_key = None
        self._file_key = None

    @property
    def e_signed_file_key(self):
        return self._e_signed_file_key

    @e_signed_file_key.setter
    def e_signed_file_key(self, value):
        self._e_signed_file_key = value
    @property
    def file_key(self):
        return self._file_key

    @file_key.setter
    def file_key(self, value):
        self._file_key = value


    def to_alipay_dict(self):
        params = dict()
        if self.e_signed_file_key:
            if hasattr(self.e_signed_file_key, 'to_alipay_dict'):
                params['e_signed_file_key'] = self.e_signed_file_key.to_alipay_dict()
            else:
                params['e_signed_file_key'] = self.e_signed_file_key
        if self.file_key:
            if hasattr(self.file_key, 'to_alipay_dict'):
                params['file_key'] = self.file_key.to_alipay_dict()
            else:
                params['file_key'] = self.file_key
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SignedFileInfoDTO()
        if 'e_signed_file_key' in d:
            o.e_signed_file_key = d['e_signed_file_key']
        if 'file_key' in d:
            o.file_key = d['file_key']
        return o


