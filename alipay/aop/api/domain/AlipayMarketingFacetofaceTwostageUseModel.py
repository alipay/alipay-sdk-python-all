#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayMarketingFacetofaceTwostageUseModel(object):

    def __init__(self):
        self._biz_sence = None
        self._dynamic_id = None
        self._ext_data = None
        self._sence_no = None

    @property
    def biz_sence(self):
        return self._biz_sence

    @biz_sence.setter
    def biz_sence(self, value):
        self._biz_sence = value
    @property
    def dynamic_id(self):
        return self._dynamic_id

    @dynamic_id.setter
    def dynamic_id(self, value):
        self._dynamic_id = value
    @property
    def ext_data(self):
        return self._ext_data

    @ext_data.setter
    def ext_data(self, value):
        self._ext_data = value
    @property
    def sence_no(self):
        return self._sence_no

    @sence_no.setter
    def sence_no(self, value):
        self._sence_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_sence:
            if hasattr(self.biz_sence, 'to_alipay_dict'):
                params['biz_sence'] = self.biz_sence.to_alipay_dict()
            else:
                params['biz_sence'] = self.biz_sence
        if self.dynamic_id:
            if hasattr(self.dynamic_id, 'to_alipay_dict'):
                params['dynamic_id'] = self.dynamic_id.to_alipay_dict()
            else:
                params['dynamic_id'] = self.dynamic_id
        if self.ext_data:
            if hasattr(self.ext_data, 'to_alipay_dict'):
                params['ext_data'] = self.ext_data.to_alipay_dict()
            else:
                params['ext_data'] = self.ext_data
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
        o = AlipayMarketingFacetofaceTwostageUseModel()
        if 'biz_sence' in d:
            o.biz_sence = d['biz_sence']
        if 'dynamic_id' in d:
            o.dynamic_id = d['dynamic_id']
        if 'ext_data' in d:
            o.ext_data = d['ext_data']
        if 'sence_no' in d:
            o.sence_no = d['sence_no']
        return o


