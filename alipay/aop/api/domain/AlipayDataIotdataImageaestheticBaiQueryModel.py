#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayDataIotdataImageaestheticBaiQueryModel(object):

    def __init__(self):
        self._biz_id = None
        self._image_base_64 = None
        self._image_url = None
        self._trace_id = None
        self._type = None

    @property
    def biz_id(self):
        return self._biz_id

    @biz_id.setter
    def biz_id(self, value):
        self._biz_id = value
    @property
    def image_base_64(self):
        return self._image_base_64

    @image_base_64.setter
    def image_base_64(self, value):
        self._image_base_64 = value
    @property
    def image_url(self):
        return self._image_url

    @image_url.setter
    def image_url(self, value):
        self._image_url = value
    @property
    def trace_id(self):
        return self._trace_id

    @trace_id.setter
    def trace_id(self, value):
        self._trace_id = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_id:
            if hasattr(self.biz_id, 'to_alipay_dict'):
                params['biz_id'] = self.biz_id.to_alipay_dict()
            else:
                params['biz_id'] = self.biz_id
        if self.image_base_64:
            if hasattr(self.image_base_64, 'to_alipay_dict'):
                params['image_base_64'] = self.image_base_64.to_alipay_dict()
            else:
                params['image_base_64'] = self.image_base_64
        if self.image_url:
            if hasattr(self.image_url, 'to_alipay_dict'):
                params['image_url'] = self.image_url.to_alipay_dict()
            else:
                params['image_url'] = self.image_url
        if self.trace_id:
            if hasattr(self.trace_id, 'to_alipay_dict'):
                params['trace_id'] = self.trace_id.to_alipay_dict()
            else:
                params['trace_id'] = self.trace_id
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
        o = AlipayDataIotdataImageaestheticBaiQueryModel()
        if 'biz_id' in d:
            o.biz_id = d['biz_id']
        if 'image_base_64' in d:
            o.image_base_64 = d['image_base_64']
        if 'image_url' in d:
            o.image_url = d['image_url']
        if 'trace_id' in d:
            o.trace_id = d['trace_id']
        if 'type' in d:
            o.type = d['type']
        return o


