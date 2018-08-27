#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenMiniTemplatemessageUsertemplateApplyModel(object):

    def __init__(self):
        self._keyword_list = None
        self._template_library_id = None

    @property
    def keyword_list(self):
        return self._keyword_list

    @keyword_list.setter
    def keyword_list(self, value):
        self._keyword_list = value
    @property
    def template_library_id(self):
        return self._template_library_id

    @template_library_id.setter
    def template_library_id(self, value):
        self._template_library_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.keyword_list:
            if hasattr(self.keyword_list, 'to_alipay_dict'):
                params['keyword_list'] = self.keyword_list.to_alipay_dict()
            else:
                params['keyword_list'] = self.keyword_list
        if self.template_library_id:
            if hasattr(self.template_library_id, 'to_alipay_dict'):
                params['template_library_id'] = self.template_library_id.to_alipay_dict()
            else:
                params['template_library_id'] = self.template_library_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenMiniTemplatemessageUsertemplateApplyModel()
        if 'keyword_list' in d:
            o.keyword_list = d['keyword_list']
        if 'template_library_id' in d:
            o.template_library_id = d['template_library_id']
        return o


