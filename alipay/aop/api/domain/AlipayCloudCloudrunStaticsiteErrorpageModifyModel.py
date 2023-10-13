#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ErrorPageSetting import ErrorPageSetting


class AlipayCloudCloudrunStaticsiteErrorpageModifyModel(object):

    def __init__(self):
        self._assume_token = None
        self._domain_list = None
        self._env = None
        self._error_page = None

    @property
    def assume_token(self):
        return self._assume_token

    @assume_token.setter
    def assume_token(self, value):
        self._assume_token = value
    @property
    def domain_list(self):
        return self._domain_list

    @domain_list.setter
    def domain_list(self, value):
        if isinstance(value, list):
            self._domain_list = list()
            for i in value:
                self._domain_list.append(i)
    @property
    def env(self):
        return self._env

    @env.setter
    def env(self, value):
        self._env = value
    @property
    def error_page(self):
        return self._error_page

    @error_page.setter
    def error_page(self, value):
        if isinstance(value, ErrorPageSetting):
            self._error_page = value
        else:
            self._error_page = ErrorPageSetting.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.assume_token:
            if hasattr(self.assume_token, 'to_alipay_dict'):
                params['assume_token'] = self.assume_token.to_alipay_dict()
            else:
                params['assume_token'] = self.assume_token
        if self.domain_list:
            if isinstance(self.domain_list, list):
                for i in range(0, len(self.domain_list)):
                    element = self.domain_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.domain_list[i] = element.to_alipay_dict()
            if hasattr(self.domain_list, 'to_alipay_dict'):
                params['domain_list'] = self.domain_list.to_alipay_dict()
            else:
                params['domain_list'] = self.domain_list
        if self.env:
            if hasattr(self.env, 'to_alipay_dict'):
                params['env'] = self.env.to_alipay_dict()
            else:
                params['env'] = self.env
        if self.error_page:
            if hasattr(self.error_page, 'to_alipay_dict'):
                params['error_page'] = self.error_page.to_alipay_dict()
            else:
                params['error_page'] = self.error_page
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCloudCloudrunStaticsiteErrorpageModifyModel()
        if 'assume_token' in d:
            o.assume_token = d['assume_token']
        if 'domain_list' in d:
            o.domain_list = d['domain_list']
        if 'env' in d:
            o.env = d['env']
        if 'error_page' in d:
            o.error_page = d['error_page']
        return o


