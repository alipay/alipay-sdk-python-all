#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEcoCityserviceAppinfoQueryModel(object):

    def __init__(self):
        self._biz_type = None
        self._ext_info = None
        self._request_context = None

    @property
    def biz_type(self):
        return self._biz_type

    @biz_type.setter
    def biz_type(self, value):
        self._biz_type = value
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value
    @property
    def request_context(self):
        return self._request_context

    @request_context.setter
    def request_context(self, value):
        self._request_context = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_type:
            if hasattr(self.biz_type, 'to_alipay_dict'):
                params['biz_type'] = self.biz_type.to_alipay_dict()
            else:
                params['biz_type'] = self.biz_type
        if self.ext_info:
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        if self.request_context:
            if hasattr(self.request_context, 'to_alipay_dict'):
                params['request_context'] = self.request_context.to_alipay_dict()
            else:
                params['request_context'] = self.request_context
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEcoCityserviceAppinfoQueryModel()
        if 'biz_type' in d:
            o.biz_type = d['biz_type']
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'request_context' in d:
            o.request_context = d['request_context']
        return o


