#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class FileItem(object):

    def __init__(self):
        self._afts_id = None
        self._file_type = None

    @property
    def afts_id(self):
        return self._afts_id

    @afts_id.setter
    def afts_id(self, value):
        self._afts_id = value
    @property
    def file_type(self):
        return self._file_type

    @file_type.setter
    def file_type(self, value):
        self._file_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.afts_id:
            if hasattr(self.afts_id, 'to_alipay_dict'):
                params['afts_id'] = self.afts_id.to_alipay_dict()
            else:
                params['afts_id'] = self.afts_id
        if self.file_type:
            if hasattr(self.file_type, 'to_alipay_dict'):
                params['file_type'] = self.file_type.to_alipay_dict()
            else:
                params['file_type'] = self.file_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = FileItem()
        if 'afts_id' in d:
            o.afts_id = d['afts_id']
        if 'file_type' in d:
            o.file_type = d['file_type']
        return o


