#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipaySecurityProdEdgeColorfeedbackCreateModel(object):

    def __init__(self):
        self._biz_param = None
        self._biz_token = None
        self._sec_info = None
        self._tinyapp_id = None
        self._trace_id = None

    @property
    def biz_param(self):
        return self._biz_param

    @biz_param.setter
    def biz_param(self, value):
        self._biz_param = value
    @property
    def biz_token(self):
        return self._biz_token

    @biz_token.setter
    def biz_token(self, value):
        self._biz_token = value
    @property
    def sec_info(self):
        return self._sec_info

    @sec_info.setter
    def sec_info(self, value):
        self._sec_info = value
    @property
    def tinyapp_id(self):
        return self._tinyapp_id

    @tinyapp_id.setter
    def tinyapp_id(self, value):
        self._tinyapp_id = value
    @property
    def trace_id(self):
        return self._trace_id

    @trace_id.setter
    def trace_id(self, value):
        self._trace_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_param:
            if hasattr(self.biz_param, 'to_alipay_dict'):
                params['biz_param'] = self.biz_param.to_alipay_dict()
            else:
                params['biz_param'] = self.biz_param
        if self.biz_token:
            if hasattr(self.biz_token, 'to_alipay_dict'):
                params['biz_token'] = self.biz_token.to_alipay_dict()
            else:
                params['biz_token'] = self.biz_token
        if self.sec_info:
            if hasattr(self.sec_info, 'to_alipay_dict'):
                params['sec_info'] = self.sec_info.to_alipay_dict()
            else:
                params['sec_info'] = self.sec_info
        if self.tinyapp_id:
            if hasattr(self.tinyapp_id, 'to_alipay_dict'):
                params['tinyapp_id'] = self.tinyapp_id.to_alipay_dict()
            else:
                params['tinyapp_id'] = self.tinyapp_id
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
        o = AlipaySecurityProdEdgeColorfeedbackCreateModel()
        if 'biz_param' in d:
            o.biz_param = d['biz_param']
        if 'biz_token' in d:
            o.biz_token = d['biz_token']
        if 'sec_info' in d:
            o.sec_info = d['sec_info']
        if 'tinyapp_id' in d:
            o.tinyapp_id = d['tinyapp_id']
        if 'trace_id' in d:
            o.trace_id = d['trace_id']
        return o


