#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class InsOpenAttachmentDTO(object):

    def __init__(self):
        self._afts_file_id = None
        self._biz_data = None
        self._description = None
        self._file_type = None
        self._name = None
        self._path = None
        self._size = None
        self._type = None

    @property
    def afts_file_id(self):
        return self._afts_file_id

    @afts_file_id.setter
    def afts_file_id(self, value):
        self._afts_file_id = value
    @property
    def biz_data(self):
        return self._biz_data

    @biz_data.setter
    def biz_data(self, value):
        self._biz_data = value
    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        self._description = value
    @property
    def file_type(self):
        return self._file_type

    @file_type.setter
    def file_type(self, value):
        self._file_type = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def path(self):
        return self._path

    @path.setter
    def path(self, value):
        self._path = value
    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        self._size = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value


    def to_alipay_dict(self):
        params = dict()
        if self.afts_file_id:
            if hasattr(self.afts_file_id, 'to_alipay_dict'):
                params['afts_file_id'] = self.afts_file_id.to_alipay_dict()
            else:
                params['afts_file_id'] = self.afts_file_id
        if self.biz_data:
            if hasattr(self.biz_data, 'to_alipay_dict'):
                params['biz_data'] = self.biz_data.to_alipay_dict()
            else:
                params['biz_data'] = self.biz_data
        if self.description:
            if hasattr(self.description, 'to_alipay_dict'):
                params['description'] = self.description.to_alipay_dict()
            else:
                params['description'] = self.description
        if self.file_type:
            if hasattr(self.file_type, 'to_alipay_dict'):
                params['file_type'] = self.file_type.to_alipay_dict()
            else:
                params['file_type'] = self.file_type
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.path:
            if hasattr(self.path, 'to_alipay_dict'):
                params['path'] = self.path.to_alipay_dict()
            else:
                params['path'] = self.path
        if self.size:
            if hasattr(self.size, 'to_alipay_dict'):
                params['size'] = self.size.to_alipay_dict()
            else:
                params['size'] = self.size
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
        o = InsOpenAttachmentDTO()
        if 'afts_file_id' in d:
            o.afts_file_id = d['afts_file_id']
        if 'biz_data' in d:
            o.biz_data = d['biz_data']
        if 'description' in d:
            o.description = d['description']
        if 'file_type' in d:
            o.file_type = d['file_type']
        if 'name' in d:
            o.name = d['name']
        if 'path' in d:
            o.path = d['path']
        if 'size' in d:
            o.size = d['size']
        if 'type' in d:
            o.type = d['type']
        return o


