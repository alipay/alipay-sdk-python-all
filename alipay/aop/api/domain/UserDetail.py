#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class UserDetail(object):

    def __init__(self):
        self._appid_one = None
        self._list_open_id = None
        self._open_id = None
        self._user_id = None
        self._user_id_list = None

    @property
    def appid_one(self):
        return self._appid_one

    @appid_one.setter
    def appid_one(self, value):
        self._appid_one = value
    @property
    def list_open_id(self):
        return self._list_open_id

    @list_open_id.setter
    def list_open_id(self, value):
        if isinstance(value, list):
            self._list_open_id = list()
            for i in value:
                self._list_open_id.append(i)
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value
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
        if self.appid_one:
            if hasattr(self.appid_one, 'to_alipay_dict'):
                params['appid_one'] = self.appid_one.to_alipay_dict()
            else:
                params['appid_one'] = self.appid_one
        if self.list_open_id:
            if isinstance(self.list_open_id, list):
                for i in range(0, len(self.list_open_id)):
                    element = self.list_open_id[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.list_open_id[i] = element.to_alipay_dict()
            if hasattr(self.list_open_id, 'to_alipay_dict'):
                params['list_open_id'] = self.list_open_id.to_alipay_dict()
            else:
                params['list_open_id'] = self.list_open_id
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
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
        o = UserDetail()
        if 'appid_one' in d:
            o.appid_one = d['appid_one']
        if 'list_open_id' in d:
            o.list_open_id = d['list_open_id']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'user_id' in d:
            o.user_id = d['user_id']
        if 'user_id_list' in d:
            o.user_id_list = d['user_id_list']
        return o


