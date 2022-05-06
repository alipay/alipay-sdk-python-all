#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AmapMapMapserviceIotfcaeIotfcaeQueryModel(object):

    def __init__(self):
        self._cert_no = None
        self._client_version = None
        self._skin_id_list = None
        self._tips_collect_rate = None
        self._user_id = None

    @property
    def cert_no(self):
        return self._cert_no

    @cert_no.setter
    def cert_no(self, value):
        self._cert_no = value
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
    def tips_collect_rate(self):
        return self._tips_collect_rate

    @tips_collect_rate.setter
    def tips_collect_rate(self, value):
        if isinstance(value, list):
            self._tips_collect_rate = list()
            for i in value:
                self._tips_collect_rate.append(i)
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.cert_no:
            if hasattr(self.cert_no, 'to_alipay_dict'):
                params['cert_no'] = self.cert_no.to_alipay_dict()
            else:
                params['cert_no'] = self.cert_no
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
        if self.tips_collect_rate:
            if isinstance(self.tips_collect_rate, list):
                for i in range(0, len(self.tips_collect_rate)):
                    element = self.tips_collect_rate[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.tips_collect_rate[i] = element.to_alipay_dict()
            if hasattr(self.tips_collect_rate, 'to_alipay_dict'):
                params['tips_collect_rate'] = self.tips_collect_rate.to_alipay_dict()
            else:
                params['tips_collect_rate'] = self.tips_collect_rate
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
        o = AmapMapMapserviceIotfcaeIotfcaeQueryModel()
        if 'cert_no' in d:
            o.cert_no = d['cert_no']
        if 'client_version' in d:
            o.client_version = d['client_version']
        if 'skin_id_list' in d:
            o.skin_id_list = d['skin_id_list']
        if 'tips_collect_rate' in d:
            o.tips_collect_rate = d['tips_collect_rate']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


