#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class TemplateActionMiniAppUrlDTO(object):

    def __init__(self):
        self._display_on_list = None
        self._mini_app_id = None
        self._mini_page_param = None
        self._mini_query_param = None

    @property
    def display_on_list(self):
        return self._display_on_list

    @display_on_list.setter
    def display_on_list(self, value):
        self._display_on_list = value
    @property
    def mini_app_id(self):
        return self._mini_app_id

    @mini_app_id.setter
    def mini_app_id(self, value):
        self._mini_app_id = value
    @property
    def mini_page_param(self):
        return self._mini_page_param

    @mini_page_param.setter
    def mini_page_param(self, value):
        self._mini_page_param = value
    @property
    def mini_query_param(self):
        return self._mini_query_param

    @mini_query_param.setter
    def mini_query_param(self, value):
        self._mini_query_param = value


    def to_alipay_dict(self):
        params = dict()
        if self.display_on_list:
            if hasattr(self.display_on_list, 'to_alipay_dict'):
                params['display_on_list'] = self.display_on_list.to_alipay_dict()
            else:
                params['display_on_list'] = self.display_on_list
        if self.mini_app_id:
            if hasattr(self.mini_app_id, 'to_alipay_dict'):
                params['mini_app_id'] = self.mini_app_id.to_alipay_dict()
            else:
                params['mini_app_id'] = self.mini_app_id
        if self.mini_page_param:
            if hasattr(self.mini_page_param, 'to_alipay_dict'):
                params['mini_page_param'] = self.mini_page_param.to_alipay_dict()
            else:
                params['mini_page_param'] = self.mini_page_param
        if self.mini_query_param:
            if hasattr(self.mini_query_param, 'to_alipay_dict'):
                params['mini_query_param'] = self.mini_query_param.to_alipay_dict()
            else:
                params['mini_query_param'] = self.mini_query_param
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = TemplateActionMiniAppUrlDTO()
        if 'display_on_list' in d:
            o.display_on_list = d['display_on_list']
        if 'mini_app_id' in d:
            o.mini_app_id = d['mini_app_id']
        if 'mini_page_param' in d:
            o.mini_page_param = d['mini_page_param']
        if 'mini_query_param' in d:
            o.mini_query_param = d['mini_query_param']
        return o


