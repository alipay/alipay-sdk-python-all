#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class Data(object):

    def __init__(self):
        self._user_id_list = None

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
        if 'user_id_list' in d:
            o.user_id_list = d['user_id_list']
        return o


