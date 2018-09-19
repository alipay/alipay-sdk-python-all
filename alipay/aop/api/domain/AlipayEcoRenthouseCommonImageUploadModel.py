#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEcoRenthouseCommonImageUploadModel(object):

    def __init__(self):
        self._file_base = None
        self._file_type = None
        self._is_public = None

    @property
    def file_base(self):
        return self._file_base

    @file_base.setter
    def file_base(self, value):
        self._file_base = value
    @property
    def file_type(self):
        return self._file_type

    @file_type.setter
    def file_type(self, value):
        self._file_type = value
    @property
    def is_public(self):
        return self._is_public

    @is_public.setter
    def is_public(self, value):
        self._is_public = value


    def to_alipay_dict(self):
        params = dict()
        if self.file_base:
            if hasattr(self.file_base, 'to_alipay_dict'):
                params['file_base'] = self.file_base.to_alipay_dict()
            else:
                params['file_base'] = self.file_base
        if self.file_type:
            if hasattr(self.file_type, 'to_alipay_dict'):
                params['file_type'] = self.file_type.to_alipay_dict()
            else:
                params['file_type'] = self.file_type
        if self.is_public:
            if hasattr(self.is_public, 'to_alipay_dict'):
                params['is_public'] = self.is_public.to_alipay_dict()
            else:
                params['is_public'] = self.is_public
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEcoRenthouseCommonImageUploadModel()
        if 'file_base' in d:
            o.file_base = d['file_base']
        if 'file_type' in d:
            o.file_type = d['file_type']
        if 'is_public' in d:
            o.is_public = d['is_public']
        return o


