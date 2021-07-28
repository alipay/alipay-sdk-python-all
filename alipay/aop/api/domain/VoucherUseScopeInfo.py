#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class VoucherUseScopeInfo(object):

    def __init__(self):
        self._app_id_list = None
        self._pid_list = None
        self._shop_id_list = None

    @property
    def app_id_list(self):
        return self._app_id_list

    @app_id_list.setter
    def app_id_list(self, value):
        if isinstance(value, list):
            self._app_id_list = list()
            for i in value:
                self._app_id_list.append(i)
    @property
    def pid_list(self):
        return self._pid_list

    @pid_list.setter
    def pid_list(self, value):
        if isinstance(value, list):
            self._pid_list = list()
            for i in value:
                self._pid_list.append(i)
    @property
    def shop_id_list(self):
        return self._shop_id_list

    @shop_id_list.setter
    def shop_id_list(self, value):
        if isinstance(value, list):
            self._shop_id_list = list()
            for i in value:
                self._shop_id_list.append(i)


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
        if self.pid_list:
            if isinstance(self.pid_list, list):
                for i in range(0, len(self.pid_list)):
                    element = self.pid_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.pid_list[i] = element.to_alipay_dict()
            if hasattr(self.pid_list, 'to_alipay_dict'):
                params['pid_list'] = self.pid_list.to_alipay_dict()
            else:
                params['pid_list'] = self.pid_list
        if self.shop_id_list:
            if isinstance(self.shop_id_list, list):
                for i in range(0, len(self.shop_id_list)):
                    element = self.shop_id_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.shop_id_list[i] = element.to_alipay_dict()
            if hasattr(self.shop_id_list, 'to_alipay_dict'):
                params['shop_id_list'] = self.shop_id_list.to_alipay_dict()
            else:
                params['shop_id_list'] = self.shop_id_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = VoucherUseScopeInfo()
        if 'app_id_list' in d:
            o.app_id_list = d['app_id_list']
        if 'pid_list' in d:
            o.pid_list = d['pid_list']
        if 'shop_id_list' in d:
            o.shop_id_list = d['shop_id_list']
        return o


