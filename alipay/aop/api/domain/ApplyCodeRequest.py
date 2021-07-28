#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ApplyCodeRequest(object):

    def __init__(self):
        self._biz_code = None
        self._biz_id = None
        self._context_data = None
        self._logo_url = None

    @property
    def biz_code(self):
        return self._biz_code

    @biz_code.setter
    def biz_code(self, value):
        self._biz_code = value
    @property
    def biz_id(self):
        return self._biz_id

    @biz_id.setter
    def biz_id(self, value):
        self._biz_id = value
    @property
    def context_data(self):
        return self._context_data

    @context_data.setter
    def context_data(self, value):
        self._context_data = value
    @property
    def logo_url(self):
        return self._logo_url

    @logo_url.setter
    def logo_url(self, value):
        self._logo_url = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_code:
            if hasattr(self.biz_code, 'to_alipay_dict'):
                params['biz_code'] = self.biz_code.to_alipay_dict()
            else:
                params['biz_code'] = self.biz_code
        if self.biz_id:
            if hasattr(self.biz_id, 'to_alipay_dict'):
                params['biz_id'] = self.biz_id.to_alipay_dict()
            else:
                params['biz_id'] = self.biz_id
        if self.context_data:
            if hasattr(self.context_data, 'to_alipay_dict'):
                params['context_data'] = self.context_data.to_alipay_dict()
            else:
                params['context_data'] = self.context_data
        if self.logo_url:
            if hasattr(self.logo_url, 'to_alipay_dict'):
                params['logo_url'] = self.logo_url.to_alipay_dict()
            else:
                params['logo_url'] = self.logo_url
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ApplyCodeRequest()
        if 'biz_code' in d:
            o.biz_code = d['biz_code']
        if 'biz_id' in d:
            o.biz_id = d['biz_id']
        if 'context_data' in d:
            o.context_data = d['context_data']
        if 'logo_url' in d:
            o.logo_url = d['logo_url']
        return o


