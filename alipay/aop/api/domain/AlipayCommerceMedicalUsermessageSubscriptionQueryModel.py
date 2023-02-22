#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceMedicalUsermessageSubscriptionQueryModel(object):

    def __init__(self):
        self._industry_type_id = None
        self._open_id_list = None
        self._user_id_list = None

    @property
    def industry_type_id(self):
        return self._industry_type_id

    @industry_type_id.setter
    def industry_type_id(self, value):
        self._industry_type_id = value
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
        if self.industry_type_id:
            if hasattr(self.industry_type_id, 'to_alipay_dict'):
                params['industry_type_id'] = self.industry_type_id.to_alipay_dict()
            else:
                params['industry_type_id'] = self.industry_type_id
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
        o = AlipayCommerceMedicalUsermessageSubscriptionQueryModel()
        if 'industry_type_id' in d:
            o.industry_type_id = d['industry_type_id']
        if 'open_id_list' in d:
            o.open_id_list = d['open_id_list']
        if 'user_id_list' in d:
            o.user_id_list = d['user_id_list']
        return o


