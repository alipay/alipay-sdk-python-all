#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEbppDetectReportQueryModel(object):

    def __init__(self):
        self._biz_type = None
        self._biz_unique_id = None
        self._out_biz_no = None

    @property
    def biz_type(self):
        return self._biz_type

    @biz_type.setter
    def biz_type(self, value):
        self._biz_type = value
    @property
    def biz_unique_id(self):
        return self._biz_unique_id

    @biz_unique_id.setter
    def biz_unique_id(self, value):
        self._biz_unique_id = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_type:
            if hasattr(self.biz_type, 'to_alipay_dict'):
                params['biz_type'] = self.biz_type.to_alipay_dict()
            else:
                params['biz_type'] = self.biz_type
        if self.biz_unique_id:
            if hasattr(self.biz_unique_id, 'to_alipay_dict'):
                params['biz_unique_id'] = self.biz_unique_id.to_alipay_dict()
            else:
                params['biz_unique_id'] = self.biz_unique_id
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEbppDetectReportQueryModel()
        if 'biz_type' in d:
            o.biz_type = d['biz_type']
        if 'biz_unique_id' in d:
            o.biz_unique_id = d['biz_unique_id']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        return o


