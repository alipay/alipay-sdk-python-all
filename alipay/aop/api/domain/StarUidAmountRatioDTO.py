#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class StarUidAmountRatioDTO(object):

    def __init__(self):
        self._ratio = None
        self._uid_list = None
        self._user_open_id_list = None

    @property
    def ratio(self):
        return self._ratio

    @ratio.setter
    def ratio(self, value):
        self._ratio = value
    @property
    def uid_list(self):
        return self._uid_list

    @uid_list.setter
    def uid_list(self, value):
        if isinstance(value, list):
            self._uid_list = list()
            for i in value:
                self._uid_list.append(i)
    @property
    def user_open_id_list(self):
        return self._user_open_id_list

    @user_open_id_list.setter
    def user_open_id_list(self, value):
        if isinstance(value, list):
            self._user_open_id_list = list()
            for i in value:
                self._user_open_id_list.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.ratio:
            if hasattr(self.ratio, 'to_alipay_dict'):
                params['ratio'] = self.ratio.to_alipay_dict()
            else:
                params['ratio'] = self.ratio
        if self.uid_list:
            if isinstance(self.uid_list, list):
                for i in range(0, len(self.uid_list)):
                    element = self.uid_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.uid_list[i] = element.to_alipay_dict()
            if hasattr(self.uid_list, 'to_alipay_dict'):
                params['uid_list'] = self.uid_list.to_alipay_dict()
            else:
                params['uid_list'] = self.uid_list
        if self.user_open_id_list:
            if isinstance(self.user_open_id_list, list):
                for i in range(0, len(self.user_open_id_list)):
                    element = self.user_open_id_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.user_open_id_list[i] = element.to_alipay_dict()
            if hasattr(self.user_open_id_list, 'to_alipay_dict'):
                params['user_open_id_list'] = self.user_open_id_list.to_alipay_dict()
            else:
                params['user_open_id_list'] = self.user_open_id_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = StarUidAmountRatioDTO()
        if 'ratio' in d:
            o.ratio = d['ratio']
        if 'uid_list' in d:
            o.uid_list = d['uid_list']
        if 'user_open_id_list' in d:
            o.user_open_id_list = d['user_open_id_list']
        return o


