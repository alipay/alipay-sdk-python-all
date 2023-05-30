#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.DspCreativeQueryRequest import DspCreativeQueryRequest


class AlipayDataDataserviceDspcreativeBatchqueryModel(object):

    def __init__(self):
        self._biz_token = None
        self._creative_query_request = None
        self._dsp_id = None

    @property
    def biz_token(self):
        return self._biz_token

    @biz_token.setter
    def biz_token(self, value):
        self._biz_token = value
    @property
    def creative_query_request(self):
        return self._creative_query_request

    @creative_query_request.setter
    def creative_query_request(self, value):
        if isinstance(value, list):
            self._creative_query_request = list()
            for i in value:
                if isinstance(i, DspCreativeQueryRequest):
                    self._creative_query_request.append(i)
                else:
                    self._creative_query_request.append(DspCreativeQueryRequest.from_alipay_dict(i))
    @property
    def dsp_id(self):
        return self._dsp_id

    @dsp_id.setter
    def dsp_id(self, value):
        self._dsp_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_token:
            if hasattr(self.biz_token, 'to_alipay_dict'):
                params['biz_token'] = self.biz_token.to_alipay_dict()
            else:
                params['biz_token'] = self.biz_token
        if self.creative_query_request:
            if isinstance(self.creative_query_request, list):
                for i in range(0, len(self.creative_query_request)):
                    element = self.creative_query_request[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.creative_query_request[i] = element.to_alipay_dict()
            if hasattr(self.creative_query_request, 'to_alipay_dict'):
                params['creative_query_request'] = self.creative_query_request.to_alipay_dict()
            else:
                params['creative_query_request'] = self.creative_query_request
        if self.dsp_id:
            if hasattr(self.dsp_id, 'to_alipay_dict'):
                params['dsp_id'] = self.dsp_id.to_alipay_dict()
            else:
                params['dsp_id'] = self.dsp_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayDataDataserviceDspcreativeBatchqueryModel()
        if 'biz_token' in d:
            o.biz_token = d['biz_token']
        if 'creative_query_request' in d:
            o.creative_query_request = d['creative_query_request']
        if 'dsp_id' in d:
            o.dsp_id = d['dsp_id']
        return o


