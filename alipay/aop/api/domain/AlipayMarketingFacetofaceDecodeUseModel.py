#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayMarketingFacetofaceDecodeUseModel(object):

    def __init__(self):
        self._dynamic_id = None
        self._sence_no = None

    @property
    def dynamic_id(self):
        return self._dynamic_id

    @dynamic_id.setter
    def dynamic_id(self, value):
        self._dynamic_id = value
    @property
    def sence_no(self):
        return self._sence_no

    @sence_no.setter
    def sence_no(self, value):
        self._sence_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.dynamic_id:
            if hasattr(self.dynamic_id, 'to_alipay_dict'):
                params['dynamic_id'] = self.dynamic_id.to_alipay_dict()
            else:
                params['dynamic_id'] = self.dynamic_id
        if self.sence_no:
            if hasattr(self.sence_no, 'to_alipay_dict'):
                params['sence_no'] = self.sence_no.to_alipay_dict()
            else:
                params['sence_no'] = self.sence_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayMarketingFacetofaceDecodeUseModel()
        if 'dynamic_id' in d:
            o.dynamic_id = d['dynamic_id']
        if 'sence_no' in d:
            o.sence_no = d['sence_no']
        return o


