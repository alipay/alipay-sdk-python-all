#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayMarketingImageListQueryModel(object):

    def __init__(self):
        self._file_name = None
        self._image_directory_id = None
        self._image_index_id = None
        self._page_num = None
        self._page_size = None

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
    @property
    def page_num(self):
        return self._page_num

    @page_num.setter
    def page_num(self, value):
        self._page_num = value
    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, value):
        self._page_size = value


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
        if self.page_num:
            if hasattr(self.page_num, 'to_alipay_dict'):
                params['page_num'] = self.page_num.to_alipay_dict()
            else:
                params['page_num'] = self.page_num
        if self.page_size:
            if hasattr(self.page_size, 'to_alipay_dict'):
                params['page_size'] = self.page_size.to_alipay_dict()
            else:
                params['page_size'] = self.page_size
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayMarketingImageListQueryModel()
        if 'file_name' in d:
            o.file_name = d['file_name']
        if 'image_directory_id' in d:
            o.image_directory_id = d['image_directory_id']
        if 'image_index_id' in d:
            o.image_index_id = d['image_index_id']
        if 'page_num' in d:
            o.page_num = d['page_num']
        if 'page_size' in d:
            o.page_size = d['page_size']
        return o


