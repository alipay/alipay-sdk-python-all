#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AnttechAiCvOcrVatinvoiceIdentifyModel(object):

    def __init__(self):
        self._file_type = None
        self._image_raw = None
        self._image_url = None
        self._source = None
        self._trace_id = None

    @property
    def file_type(self):
        return self._file_type

    @file_type.setter
    def file_type(self, value):
        self._file_type = value
    @property
    def image_raw(self):
        return self._image_raw

    @image_raw.setter
    def image_raw(self, value):
        self._image_raw = value
    @property
    def image_url(self):
        return self._image_url

    @image_url.setter
    def image_url(self, value):
        self._image_url = value
    @property
    def source(self):
        return self._source

    @source.setter
    def source(self, value):
        self._source = value
    @property
    def trace_id(self):
        return self._trace_id

    @trace_id.setter
    def trace_id(self, value):
        self._trace_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.file_type:
            if hasattr(self.file_type, 'to_alipay_dict'):
                params['file_type'] = self.file_type.to_alipay_dict()
            else:
                params['file_type'] = self.file_type
        if self.image_raw:
            if hasattr(self.image_raw, 'to_alipay_dict'):
                params['image_raw'] = self.image_raw.to_alipay_dict()
            else:
                params['image_raw'] = self.image_raw
        if self.image_url:
            if hasattr(self.image_url, 'to_alipay_dict'):
                params['image_url'] = self.image_url.to_alipay_dict()
            else:
                params['image_url'] = self.image_url
        if self.source:
            if hasattr(self.source, 'to_alipay_dict'):
                params['source'] = self.source.to_alipay_dict()
            else:
                params['source'] = self.source
        if self.trace_id:
            if hasattr(self.trace_id, 'to_alipay_dict'):
                params['trace_id'] = self.trace_id.to_alipay_dict()
            else:
                params['trace_id'] = self.trace_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AnttechAiCvOcrVatinvoiceIdentifyModel()
        if 'file_type' in d:
            o.file_type = d['file_type']
        if 'image_raw' in d:
            o.image_raw = d['image_raw']
        if 'image_url' in d:
            o.image_url = d['image_url']
        if 'source' in d:
            o.source = d['source']
        if 'trace_id' in d:
            o.trace_id = d['trace_id']
        return o


