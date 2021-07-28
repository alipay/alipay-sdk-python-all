#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class KbdishCommGroupDetailInfo(object):

    def __init__(self):
        self._detail_desc = None
        self._detail_id = None
        self._detail_name = None
        self._ext_info = None
        self._image_id = None
        self._out_detail_id = None
        self._sort = None

    @property
    def detail_desc(self):
        return self._detail_desc

    @detail_desc.setter
    def detail_desc(self, value):
        self._detail_desc = value
    @property
    def detail_id(self):
        return self._detail_id

    @detail_id.setter
    def detail_id(self, value):
        self._detail_id = value
    @property
    def detail_name(self):
        return self._detail_name

    @detail_name.setter
    def detail_name(self, value):
        self._detail_name = value
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value
    @property
    def image_id(self):
        return self._image_id

    @image_id.setter
    def image_id(self, value):
        self._image_id = value
    @property
    def out_detail_id(self):
        return self._out_detail_id

    @out_detail_id.setter
    def out_detail_id(self, value):
        self._out_detail_id = value
    @property
    def sort(self):
        return self._sort

    @sort.setter
    def sort(self, value):
        self._sort = value


    def to_alipay_dict(self):
        params = dict()
        if self.detail_desc:
            if hasattr(self.detail_desc, 'to_alipay_dict'):
                params['detail_desc'] = self.detail_desc.to_alipay_dict()
            else:
                params['detail_desc'] = self.detail_desc
        if self.detail_id:
            if hasattr(self.detail_id, 'to_alipay_dict'):
                params['detail_id'] = self.detail_id.to_alipay_dict()
            else:
                params['detail_id'] = self.detail_id
        if self.detail_name:
            if hasattr(self.detail_name, 'to_alipay_dict'):
                params['detail_name'] = self.detail_name.to_alipay_dict()
            else:
                params['detail_name'] = self.detail_name
        if self.ext_info:
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        if self.image_id:
            if hasattr(self.image_id, 'to_alipay_dict'):
                params['image_id'] = self.image_id.to_alipay_dict()
            else:
                params['image_id'] = self.image_id
        if self.out_detail_id:
            if hasattr(self.out_detail_id, 'to_alipay_dict'):
                params['out_detail_id'] = self.out_detail_id.to_alipay_dict()
            else:
                params['out_detail_id'] = self.out_detail_id
        if self.sort:
            if hasattr(self.sort, 'to_alipay_dict'):
                params['sort'] = self.sort.to_alipay_dict()
            else:
                params['sort'] = self.sort
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KbdishCommGroupDetailInfo()
        if 'detail_desc' in d:
            o.detail_desc = d['detail_desc']
        if 'detail_id' in d:
            o.detail_id = d['detail_id']
        if 'detail_name' in d:
            o.detail_name = d['detail_name']
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'image_id' in d:
            o.image_id = d['image_id']
        if 'out_detail_id' in d:
            o.out_detail_id = d['out_detail_id']
        if 'sort' in d:
            o.sort = d['sort']
        return o


