#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenMiniHmcodeCreateModel(object):

    def __init__(self):
        self._describe = None
        self._hm_bg_color = None
        self._hm_front_color = None
        self._query_param = None
        self._url_param = None

    @property
    def describe(self):
        return self._describe

    @describe.setter
    def describe(self, value):
        self._describe = value
    @property
    def hm_bg_color(self):
        return self._hm_bg_color

    @hm_bg_color.setter
    def hm_bg_color(self, value):
        self._hm_bg_color = value
    @property
    def hm_front_color(self):
        return self._hm_front_color

    @hm_front_color.setter
    def hm_front_color(self, value):
        self._hm_front_color = value
    @property
    def query_param(self):
        return self._query_param

    @query_param.setter
    def query_param(self, value):
        self._query_param = value
    @property
    def url_param(self):
        return self._url_param

    @url_param.setter
    def url_param(self, value):
        self._url_param = value


    def to_alipay_dict(self):
        params = dict()
        if self.describe:
            if hasattr(self.describe, 'to_alipay_dict'):
                params['describe'] = self.describe.to_alipay_dict()
            else:
                params['describe'] = self.describe
        if self.hm_bg_color:
            if hasattr(self.hm_bg_color, 'to_alipay_dict'):
                params['hm_bg_color'] = self.hm_bg_color.to_alipay_dict()
            else:
                params['hm_bg_color'] = self.hm_bg_color
        if self.hm_front_color:
            if hasattr(self.hm_front_color, 'to_alipay_dict'):
                params['hm_front_color'] = self.hm_front_color.to_alipay_dict()
            else:
                params['hm_front_color'] = self.hm_front_color
        if self.query_param:
            if hasattr(self.query_param, 'to_alipay_dict'):
                params['query_param'] = self.query_param.to_alipay_dict()
            else:
                params['query_param'] = self.query_param
        if self.url_param:
            if hasattr(self.url_param, 'to_alipay_dict'):
                params['url_param'] = self.url_param.to_alipay_dict()
            else:
                params['url_param'] = self.url_param
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenMiniHmcodeCreateModel()
        if 'describe' in d:
            o.describe = d['describe']
        if 'hm_bg_color' in d:
            o.hm_bg_color = d['hm_bg_color']
        if 'hm_front_color' in d:
            o.hm_front_color = d['hm_front_color']
        if 'query_param' in d:
            o.query_param = d['query_param']
        if 'url_param' in d:
            o.url_param = d['url_param']
        return o


