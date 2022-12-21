#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class Data(object):

    def __init__(self):
        self._alipay_open_id_list = None
        self._alipay_user_id_list = None
        self._open_id_list = None
        self._user_id_list = None

    @property
    def alipay_open_id_list(self):
        return self._alipay_open_id_list

    @alipay_open_id_list.setter
    def alipay_open_id_list(self, value):
        if isinstance(value, list):
            self._alipay_open_id_list = list()
            for i in value:
                self._alipay_open_id_list.append(i)
    @property
    def alipay_user_id_list(self):
        return self._alipay_user_id_list

    @alipay_user_id_list.setter
    def alipay_user_id_list(self, value):
        if isinstance(value, list):
            self._alipay_user_id_list = list()
            for i in value:
                self._alipay_user_id_list.append(i)
    @property
    def open_id_list(self):
        return self._open_id_list

    @open_id_list.setter
    def open_id_list(self, value):
        if isinstance(value, list):
            self._open_id_list = list()
            for i in value:
                self._open_id_list.append(i)
    @property
    def user_id_list(self):
        return self._user_id_list

    @user_id_list.setter
    def user_id_list(self, value):
        if isinstance(value, list):
            self._user_id_list = list()
            for i in value:
                self._user_id_list.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.alipay_open_id_list:
            if isinstance(self.alipay_open_id_list, list):
                for i in range(0, len(self.alipay_open_id_list)):
                    element = self.alipay_open_id_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.alipay_open_id_list[i] = element.to_alipay_dict()
            if hasattr(self.alipay_open_id_list, 'to_alipay_dict'):
                params['alipay_open_id_list'] = self.alipay_open_id_list.to_alipay_dict()
            else:
                params['alipay_open_id_list'] = self.alipay_open_id_list
        if self.alipay_user_id_list:
            if isinstance(self.alipay_user_id_list, list):
                for i in range(0, len(self.alipay_user_id_list)):
                    element = self.alipay_user_id_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.alipay_user_id_list[i] = element.to_alipay_dict()
            if hasattr(self.alipay_user_id_list, 'to_alipay_dict'):
                params['alipay_user_id_list'] = self.alipay_user_id_list.to_alipay_dict()
            else:
                params['alipay_user_id_list'] = self.alipay_user_id_list
        if self.open_id_list:
            if isinstance(self.open_id_list, list):
                for i in range(0, len(self.open_id_list)):
                    element = self.open_id_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.open_id_list[i] = element.to_alipay_dict()
            if hasattr(self.open_id_list, 'to_alipay_dict'):
                params['open_id_list'] = self.open_id_list.to_alipay_dict()
            else:
                params['open_id_list'] = self.open_id_list
        if self.user_id_list:
            if isinstance(self.user_id_list, list):
                for i in range(0, len(self.user_id_list)):
                    element = self.user_id_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.user_id_list[i] = element.to_alipay_dict()
            if hasattr(self.user_id_list, 'to_alipay_dict'):
                params['user_id_list'] = self.user_id_list.to_alipay_dict()
            else:
                params['user_id_list'] = self.user_id_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = Data()
        if 'alipay_open_id_list' in d:
            o.alipay_open_id_list = d['alipay_open_id_list']
        if 'alipay_user_id_list' in d:
            o.alipay_user_id_list = d['alipay_user_id_list']
        if 'open_id_list' in d:
            o.open_id_list = d['open_id_list']
        if 'user_id_list' in d:
            o.user_id_list = d['user_id_list']
        return o


