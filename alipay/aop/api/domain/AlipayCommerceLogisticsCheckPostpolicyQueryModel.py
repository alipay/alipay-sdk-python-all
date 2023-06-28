#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceLogisticsCheckPostpolicyQueryModel(object):

    def __init__(self):
        self._app_id_list = None

    @property
    def app_id_list(self):
        return self._app_id_list

    @app_id_list.setter
    def app_id_list(self, value):
        if isinstance(value, list):
            self._app_id_list = list()
            for i in value:
                self._app_id_list.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.app_id_list:
            if isinstance(self.app_id_list, list):
                for i in range(0, len(self.app_id_list)):
                    element = self.app_id_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.app_id_list[i] = element.to_alipay_dict()
            if hasattr(self.app_id_list, 'to_alipay_dict'):
                params['app_id_list'] = self.app_id_list.to_alipay_dict()
            else:
                params['app_id_list'] = self.app_id_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceLogisticsCheckPostpolicyQueryModel()
        if 'app_id_list' in d:
            o.app_id_list = d['app_id_list']
        return o


