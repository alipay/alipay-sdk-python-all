#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ServiceItemRestrictRule(object):

    def __init__(self):
        self._restrict_type = None
        self._service_item_id = None
        self._user_cert_no_list = None
        self._user_cert_type_list = None
        self._user_phone_no_list = None

    @property
    def restrict_type(self):
        return self._restrict_type

    @restrict_type.setter
    def restrict_type(self, value):
        self._restrict_type = value
    @property
    def service_item_id(self):
        return self._service_item_id

    @service_item_id.setter
    def service_item_id(self, value):
        self._service_item_id = value
    @property
    def user_cert_no_list(self):
        return self._user_cert_no_list

    @user_cert_no_list.setter
    def user_cert_no_list(self, value):
        if isinstance(value, list):
            self._user_cert_no_list = list()
            for i in value:
                self._user_cert_no_list.append(i)
    @property
    def user_cert_type_list(self):
        return self._user_cert_type_list

    @user_cert_type_list.setter
    def user_cert_type_list(self, value):
        if isinstance(value, list):
            self._user_cert_type_list = list()
            for i in value:
                self._user_cert_type_list.append(i)
    @property
    def user_phone_no_list(self):
        return self._user_phone_no_list

    @user_phone_no_list.setter
    def user_phone_no_list(self, value):
        if isinstance(value, list):
            self._user_phone_no_list = list()
            for i in value:
                self._user_phone_no_list.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.restrict_type:
            if hasattr(self.restrict_type, 'to_alipay_dict'):
                params['restrict_type'] = self.restrict_type.to_alipay_dict()
            else:
                params['restrict_type'] = self.restrict_type
        if self.service_item_id:
            if hasattr(self.service_item_id, 'to_alipay_dict'):
                params['service_item_id'] = self.service_item_id.to_alipay_dict()
            else:
                params['service_item_id'] = self.service_item_id
        if self.user_cert_no_list:
            if isinstance(self.user_cert_no_list, list):
                for i in range(0, len(self.user_cert_no_list)):
                    element = self.user_cert_no_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.user_cert_no_list[i] = element.to_alipay_dict()
            if hasattr(self.user_cert_no_list, 'to_alipay_dict'):
                params['user_cert_no_list'] = self.user_cert_no_list.to_alipay_dict()
            else:
                params['user_cert_no_list'] = self.user_cert_no_list
        if self.user_cert_type_list:
            if isinstance(self.user_cert_type_list, list):
                for i in range(0, len(self.user_cert_type_list)):
                    element = self.user_cert_type_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.user_cert_type_list[i] = element.to_alipay_dict()
            if hasattr(self.user_cert_type_list, 'to_alipay_dict'):
                params['user_cert_type_list'] = self.user_cert_type_list.to_alipay_dict()
            else:
                params['user_cert_type_list'] = self.user_cert_type_list
        if self.user_phone_no_list:
            if isinstance(self.user_phone_no_list, list):
                for i in range(0, len(self.user_phone_no_list)):
                    element = self.user_phone_no_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.user_phone_no_list[i] = element.to_alipay_dict()
            if hasattr(self.user_phone_no_list, 'to_alipay_dict'):
                params['user_phone_no_list'] = self.user_phone_no_list.to_alipay_dict()
            else:
                params['user_phone_no_list'] = self.user_phone_no_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ServiceItemRestrictRule()
        if 'restrict_type' in d:
            o.restrict_type = d['restrict_type']
        if 'service_item_id' in d:
            o.service_item_id = d['service_item_id']
        if 'user_cert_no_list' in d:
            o.user_cert_no_list = d['user_cert_no_list']
        if 'user_cert_type_list' in d:
            o.user_cert_type_list = d['user_cert_type_list']
        if 'user_phone_no_list' in d:
            o.user_phone_no_list = d['user_phone_no_list']
        return o


