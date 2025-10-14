#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CarfinExpressFile(object):

    def __init__(self):
        self._file_id = None
        self._tag = None
        self._type = None

    @property
    def file_id(self):
        return self._file_id

    @file_id.setter
    def file_id(self, value):
        self._file_id = value
    @property
    def tag(self):
        return self._tag

    @tag.setter
    def tag(self, value):
        self._tag = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value


    def to_alipay_dict(self):
        params = dict()
        if self.file_id:
            if hasattr(self.file_id, 'to_alipay_dict'):
                params['file_id'] = self.file_id.to_alipay_dict()
            else:
                params['file_id'] = self.file_id
        if self.tag:
            if hasattr(self.tag, 'to_alipay_dict'):
                params['tag'] = self.tag.to_alipay_dict()
            else:
                params['tag'] = self.tag
        if self.type:
            if hasattr(self.type, 'to_alipay_dict'):
                params['type'] = self.type.to_alipay_dict()
            else:
                params['type'] = self.type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CarfinExpressFile()
        if 'file_id' in d:
            o.file_id = d['file_id']
        if 'tag' in d:
            o.tag = d['tag']
        if 'type' in d:
            o.type = d['type']
        return o


