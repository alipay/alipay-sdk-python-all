#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipaySocialBaseFileUrlGetModel(object):

    def __init__(self):
        self._file_id = None
        self._source_format = None
        self._target_format = None

    @property
    def file_id(self):
        return self._file_id

    @file_id.setter
    def file_id(self, value):
        self._file_id = value
    @property
    def source_format(self):
        return self._source_format

    @source_format.setter
    def source_format(self, value):
        self._source_format = value
    @property
    def target_format(self):
        return self._target_format

    @target_format.setter
    def target_format(self, value):
        self._target_format = value


    def to_alipay_dict(self):
        params = dict()
        if self.file_id:
            if hasattr(self.file_id, 'to_alipay_dict'):
                params['file_id'] = self.file_id.to_alipay_dict()
            else:
                params['file_id'] = self.file_id
        if self.source_format:
            if hasattr(self.source_format, 'to_alipay_dict'):
                params['source_format'] = self.source_format.to_alipay_dict()
            else:
                params['source_format'] = self.source_format
        if self.target_format:
            if hasattr(self.target_format, 'to_alipay_dict'):
                params['target_format'] = self.target_format.to_alipay_dict()
            else:
                params['target_format'] = self.target_format
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipaySocialBaseFileUrlGetModel()
        if 'file_id' in d:
            o.file_id = d['file_id']
        if 'source_format' in d:
            o.source_format = d['source_format']
        if 'target_format' in d:
            o.target_format = d['target_format']
        return o


