#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AnttechNftFileUrlQueryModel(object):

    def __init__(self):
        self._file_id = None
        self._file_type = None
        self._is_private = None

    @property
    def file_id(self):
        return self._file_id

    @file_id.setter
    def file_id(self, value):
        self._file_id = value
    @property
    def file_type(self):
        return self._file_type

    @file_type.setter
    def file_type(self, value):
        self._file_type = value
    @property
    def is_private(self):
        return self._is_private

    @is_private.setter
    def is_private(self, value):
        self._is_private = value


    def to_alipay_dict(self):
        params = dict()
        if self.file_id:
            if hasattr(self.file_id, 'to_alipay_dict'):
                params['file_id'] = self.file_id.to_alipay_dict()
            else:
                params['file_id'] = self.file_id
        if self.file_type:
            if hasattr(self.file_type, 'to_alipay_dict'):
                params['file_type'] = self.file_type.to_alipay_dict()
            else:
                params['file_type'] = self.file_type
        if self.is_private:
            if hasattr(self.is_private, 'to_alipay_dict'):
                params['is_private'] = self.is_private.to_alipay_dict()
            else:
                params['is_private'] = self.is_private
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AnttechNftFileUrlQueryModel()
        if 'file_id' in d:
            o.file_id = d['file_id']
        if 'file_type' in d:
            o.file_type = d['file_type']
        if 'is_private' in d:
            o.is_private = d['is_private']
        return o


