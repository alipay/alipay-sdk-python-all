#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenMiniInnerappPluginrelationQueryModel(object):

    def __init__(self):
        self._mini_app_id_list = None
        self._page_num = None
        self._page_size = None
        self._plugin_id = None
        self._plugin_relation_status_list = None
        self._run_model_type = None
        self._show_beta_info = None

    @property
    def mini_app_id_list(self):
        return self._mini_app_id_list

    @mini_app_id_list.setter
    def mini_app_id_list(self, value):
        if isinstance(value, list):
            self._mini_app_id_list = list()
            for i in value:
                self._mini_app_id_list.append(i)
    @property
    def page_num(self):
        return self._page_num

    @page_num.setter
    def page_num(self, value):
        self._page_num = value
    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, value):
        self._page_size = value
    @property
    def plugin_id(self):
        return self._plugin_id

    @plugin_id.setter
    def plugin_id(self, value):
        self._plugin_id = value
    @property
    def plugin_relation_status_list(self):
        return self._plugin_relation_status_list

    @plugin_relation_status_list.setter
    def plugin_relation_status_list(self, value):
        if isinstance(value, list):
            self._plugin_relation_status_list = list()
            for i in value:
                self._plugin_relation_status_list.append(i)
    @property
    def run_model_type(self):
        return self._run_model_type

    @run_model_type.setter
    def run_model_type(self, value):
        self._run_model_type = value
    @property
    def show_beta_info(self):
        return self._show_beta_info

    @show_beta_info.setter
    def show_beta_info(self, value):
        self._show_beta_info = value


    def to_alipay_dict(self):
        params = dict()
        if self.mini_app_id_list:
            if isinstance(self.mini_app_id_list, list):
                for i in range(0, len(self.mini_app_id_list)):
                    element = self.mini_app_id_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.mini_app_id_list[i] = element.to_alipay_dict()
            if hasattr(self.mini_app_id_list, 'to_alipay_dict'):
                params['mini_app_id_list'] = self.mini_app_id_list.to_alipay_dict()
            else:
                params['mini_app_id_list'] = self.mini_app_id_list
        if self.page_num:
            if hasattr(self.page_num, 'to_alipay_dict'):
                params['page_num'] = self.page_num.to_alipay_dict()
            else:
                params['page_num'] = self.page_num
        if self.page_size:
            if hasattr(self.page_size, 'to_alipay_dict'):
                params['page_size'] = self.page_size.to_alipay_dict()
            else:
                params['page_size'] = self.page_size
        if self.plugin_id:
            if hasattr(self.plugin_id, 'to_alipay_dict'):
                params['plugin_id'] = self.plugin_id.to_alipay_dict()
            else:
                params['plugin_id'] = self.plugin_id
        if self.plugin_relation_status_list:
            if isinstance(self.plugin_relation_status_list, list):
                for i in range(0, len(self.plugin_relation_status_list)):
                    element = self.plugin_relation_status_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.plugin_relation_status_list[i] = element.to_alipay_dict()
            if hasattr(self.plugin_relation_status_list, 'to_alipay_dict'):
                params['plugin_relation_status_list'] = self.plugin_relation_status_list.to_alipay_dict()
            else:
                params['plugin_relation_status_list'] = self.plugin_relation_status_list
        if self.run_model_type:
            if hasattr(self.run_model_type, 'to_alipay_dict'):
                params['run_model_type'] = self.run_model_type.to_alipay_dict()
            else:
                params['run_model_type'] = self.run_model_type
        if self.show_beta_info:
            if hasattr(self.show_beta_info, 'to_alipay_dict'):
                params['show_beta_info'] = self.show_beta_info.to_alipay_dict()
            else:
                params['show_beta_info'] = self.show_beta_info
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenMiniInnerappPluginrelationQueryModel()
        if 'mini_app_id_list' in d:
            o.mini_app_id_list = d['mini_app_id_list']
        if 'page_num' in d:
            o.page_num = d['page_num']
        if 'page_size' in d:
            o.page_size = d['page_size']
        if 'plugin_id' in d:
            o.plugin_id = d['plugin_id']
        if 'plugin_relation_status_list' in d:
            o.plugin_relation_status_list = d['plugin_relation_status_list']
        if 'run_model_type' in d:
            o.run_model_type = d['run_model_type']
        if 'show_beta_info' in d:
            o.show_beta_info = d['show_beta_info']
        return o


