#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceMedicalFileAccessQueryModel(object):

    def __init__(self):
        self._file_id_list = None
        self._open_id = None
        self._order_id = None
        self._user_id = None

    @property
    def file_id_list(self):
        return self._file_id_list

    @file_id_list.setter
    def file_id_list(self, value):
        if isinstance(value, list):
            self._file_id_list = list()
            for i in value:
                self._file_id_list.append(i)
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        self._order_id = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.file_id_list:
            if isinstance(self.file_id_list, list):
                for i in range(0, len(self.file_id_list)):
                    element = self.file_id_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.file_id_list[i] = element.to_alipay_dict()
            if hasattr(self.file_id_list, 'to_alipay_dict'):
                params['file_id_list'] = self.file_id_list.to_alipay_dict()
            else:
                params['file_id_list'] = self.file_id_list
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.order_id:
            if hasattr(self.order_id, 'to_alipay_dict'):
                params['order_id'] = self.order_id.to_alipay_dict()
            else:
                params['order_id'] = self.order_id
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMedicalFileAccessQueryModel()
        if 'file_id_list' in d:
            o.file_id_list = d['file_id_list']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'order_id' in d:
            o.order_id = d['order_id']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


