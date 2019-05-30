#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.MiniAppBaseInfoQueryInfo import MiniAppBaseInfoQueryInfo


class AlipayOpenMiniInnerbaseinfoBatchqueryModel(object):

    def __init__(self):
        self._inst_code = None
        self._mini_app_id_list = None

    @property
    def inst_code(self):
        return self._inst_code

    @inst_code.setter
    def inst_code(self, value):
        self._inst_code = value
    @property
    def mini_app_id_list(self):
        return self._mini_app_id_list

    @mini_app_id_list.setter
    def mini_app_id_list(self, value):
        if isinstance(value, list):
            self._mini_app_id_list = list()
            for i in value:
                if isinstance(i, MiniAppBaseInfoQueryInfo):
                    self._mini_app_id_list.append(i)
                else:
                    self._mini_app_id_list.append(MiniAppBaseInfoQueryInfo.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.inst_code:
            if hasattr(self.inst_code, 'to_alipay_dict'):
                params['inst_code'] = self.inst_code.to_alipay_dict()
            else:
                params['inst_code'] = self.inst_code
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
        o = AlipayOpenMiniInnerbaseinfoBatchqueryModel()
        if 'inst_code' in d:
            o.inst_code = d['inst_code']
        if 'mini_app_id_list' in d:
            o.mini_app_id_list = d['mini_app_id_list']
        return o


