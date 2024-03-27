#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayMarketingImageModifyModel(object):

    def __init__(self):
        self._file_name = None
        self._image_directory_id = None
        self._image_index_id = None

    @property
    def file_name(self):
        return self._file_name

    @file_name.setter
    def file_name(self, value):
        self._file_name = value
    @property
    def image_directory_id(self):
        return self._image_directory_id

    @image_directory_id.setter
    def image_directory_id(self, value):
        self._image_directory_id = value
    @property
    def image_index_id(self):
        return self._image_index_id

    @image_index_id.setter
    def image_index_id(self, value):
        self._image_index_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.file_name:
            if hasattr(self.file_name, 'to_alipay_dict'):
                params['file_name'] = self.file_name.to_alipay_dict()
            else:
                params['file_name'] = self.file_name
        if self.image_directory_id:
            if hasattr(self.image_directory_id, 'to_alipay_dict'):
                params['image_directory_id'] = self.image_directory_id.to_alipay_dict()
            else:
                params['image_directory_id'] = self.image_directory_id
        if self.image_index_id:
            if hasattr(self.image_index_id, 'to_alipay_dict'):
                params['image_index_id'] = self.image_index_id.to_alipay_dict()
            else:
                params['image_index_id'] = self.image_index_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayMarketingImageModifyModel()
        if 'file_name' in d:
            o.file_name = d['file_name']
        if 'image_directory_id' in d:
            o.image_directory_id = d['image_directory_id']
        if 'image_index_id' in d:
            o.image_index_id = d['image_index_id']
        return o


