#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SsdataDataserviceDtevalDataanalysisSendModel(object):

    def __init__(self):
        self._biz_number = None
        self._biz_source = None
        self._data_content = None
        self._process_biz_type = None

    @property
    def biz_number(self):
        return self._biz_number

    @biz_number.setter
    def biz_number(self, value):
        self._biz_number = value
    @property
    def biz_source(self):
        return self._biz_source

    @biz_source.setter
    def biz_source(self, value):
        self._biz_source = value
    @property
    def data_content(self):
        return self._data_content

    @data_content.setter
    def data_content(self, value):
        self._data_content = value
    @property
    def process_biz_type(self):
        return self._process_biz_type

    @process_biz_type.setter
    def process_biz_type(self, value):
        self._process_biz_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_number:
            if hasattr(self.biz_number, 'to_alipay_dict'):
                params['biz_number'] = self.biz_number.to_alipay_dict()
            else:
                params['biz_number'] = self.biz_number
        if self.biz_source:
            if hasattr(self.biz_source, 'to_alipay_dict'):
                params['biz_source'] = self.biz_source.to_alipay_dict()
            else:
                params['biz_source'] = self.biz_source
        if self.data_content:
            if hasattr(self.data_content, 'to_alipay_dict'):
                params['data_content'] = self.data_content.to_alipay_dict()
            else:
                params['data_content'] = self.data_content
        if self.process_biz_type:
            if hasattr(self.process_biz_type, 'to_alipay_dict'):
                params['process_biz_type'] = self.process_biz_type.to_alipay_dict()
            else:
                params['process_biz_type'] = self.process_biz_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SsdataDataserviceDtevalDataanalysisSendModel()
        if 'biz_number' in d:
            o.biz_number = d['biz_number']
        if 'biz_source' in d:
            o.biz_source = d['biz_source']
        if 'data_content' in d:
            o.data_content = d['data_content']
        if 'process_biz_type' in d:
            o.process_biz_type = d['process_biz_type']
        return o


