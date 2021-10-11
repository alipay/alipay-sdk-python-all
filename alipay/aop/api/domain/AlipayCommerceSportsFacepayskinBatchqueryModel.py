#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceSportsFacepayskinBatchqueryModel(object):

    def __init__(self):
        self._client_version = None
        self._skin_id_list = None
        self._user_id = None

    @property
    def client_version(self):
        return self._client_version

    @client_version.setter
    def client_version(self, value):
        self._client_version = value
    @property
    def skin_id_list(self):
        return self._skin_id_list

    @skin_id_list.setter
    def skin_id_list(self, value):
        if isinstance(value, list):
            self._skin_id_list = list()
            for i in value:
                self._skin_id_list.append(i)
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.client_version:
            if hasattr(self.client_version, 'to_alipay_dict'):
                params['client_version'] = self.client_version.to_alipay_dict()
            else:
                params['client_version'] = self.client_version
        if self.skin_id_list:
            if isinstance(self.skin_id_list, list):
                for i in range(0, len(self.skin_id_list)):
                    element = self.skin_id_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.skin_id_list[i] = element.to_alipay_dict()
            if hasattr(self.skin_id_list, 'to_alipay_dict'):
                params['skin_id_list'] = self.skin_id_list.to_alipay_dict()
            else:
                params['skin_id_list'] = self.skin_id_list
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
        o = AlipayCommerceSportsFacepayskinBatchqueryModel()
        if 'client_version' in d:
            o.client_version = d['client_version']
        if 'skin_id_list' in d:
            o.skin_id_list = d['skin_id_list']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


