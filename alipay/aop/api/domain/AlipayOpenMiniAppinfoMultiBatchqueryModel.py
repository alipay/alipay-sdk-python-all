#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenMiniAppinfoMultiBatchqueryModel(object):

    def __init__(self):
        self._bundle_id = None
        self._mini_app_id_list = None

    @property
    def bundle_id(self):
        return self._bundle_id

    @bundle_id.setter
    def bundle_id(self, value):
        self._bundle_id = value
    @property
    def mini_app_id_list(self):
        return self._mini_app_id_list

    @mini_app_id_list.setter
    def mini_app_id_list(self, value):
        if isinstance(value, list):
            self._mini_app_id_list = list()
            for i in value:
                self._mini_app_id_list.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.bundle_id:
            if hasattr(self.bundle_id, 'to_alipay_dict'):
                params['bundle_id'] = self.bundle_id.to_alipay_dict()
            else:
                params['bundle_id'] = self.bundle_id
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
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenMiniAppinfoMultiBatchqueryModel()
        if 'bundle_id' in d:
            o.bundle_id = d['bundle_id']
        if 'mini_app_id_list' in d:
            o.mini_app_id_list = d['mini_app_id_list']
        return o


