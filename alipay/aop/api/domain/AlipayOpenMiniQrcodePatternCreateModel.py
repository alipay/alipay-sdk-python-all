#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenMiniQrcodePatternCreateModel(object):

    def __init__(self):
        self._invoke_type = None
        self._pattern_url = None
        self._template_id = None

    @property
    def invoke_type(self):
        return self._invoke_type

    @invoke_type.setter
    def invoke_type(self, value):
        self._invoke_type = value
    @property
    def pattern_url(self):
        return self._pattern_url

    @pattern_url.setter
    def pattern_url(self, value):
        self._pattern_url = value
    @property
    def template_id(self):
        return self._template_id

    @template_id.setter
    def template_id(self, value):
        self._template_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.invoke_type:
            if hasattr(self.invoke_type, 'to_alipay_dict'):
                params['invoke_type'] = self.invoke_type.to_alipay_dict()
            else:
                params['invoke_type'] = self.invoke_type
        if self.pattern_url:
            if hasattr(self.pattern_url, 'to_alipay_dict'):
                params['pattern_url'] = self.pattern_url.to_alipay_dict()
            else:
                params['pattern_url'] = self.pattern_url
        if self.template_id:
            if hasattr(self.template_id, 'to_alipay_dict'):
                params['template_id'] = self.template_id.to_alipay_dict()
            else:
                params['template_id'] = self.template_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenMiniQrcodePatternCreateModel()
        if 'invoke_type' in d:
            o.invoke_type = d['invoke_type']
        if 'pattern_url' in d:
            o.pattern_url = d['pattern_url']
        if 'template_id' in d:
            o.template_id = d['template_id']
        return o


