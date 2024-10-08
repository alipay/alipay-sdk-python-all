#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCloudCloudrunObDumpresultQueryModel(object):

    def __init__(self):
        self._env = None
        self._instance_id = None
        self._page_no = None
        self._page_size = None
        self._status_list = None
        self._user_name_list = None

    @property
    def env(self):
        return self._env

    @env.setter
    def env(self, value):
        self._env = value
    @property
    def instance_id(self):
        return self._instance_id

    @instance_id.setter
    def instance_id(self, value):
        self._instance_id = value
    @property
    def page_no(self):
        return self._page_no

    @page_no.setter
    def page_no(self, value):
        self._page_no = value
    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, value):
        self._page_size = value
    @property
    def status_list(self):
        return self._status_list

    @status_list.setter
    def status_list(self, value):
        if isinstance(value, list):
            self._status_list = list()
            for i in value:
                self._status_list.append(i)
    @property
    def user_name_list(self):
        return self._user_name_list

    @user_name_list.setter
    def user_name_list(self, value):
        if isinstance(value, list):
            self._user_name_list = list()
            for i in value:
                self._user_name_list.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.env:
            if hasattr(self.env, 'to_alipay_dict'):
                params['env'] = self.env.to_alipay_dict()
            else:
                params['env'] = self.env
        if self.instance_id:
            if hasattr(self.instance_id, 'to_alipay_dict'):
                params['instance_id'] = self.instance_id.to_alipay_dict()
            else:
                params['instance_id'] = self.instance_id
        if self.page_no:
            if hasattr(self.page_no, 'to_alipay_dict'):
                params['page_no'] = self.page_no.to_alipay_dict()
            else:
                params['page_no'] = self.page_no
        if self.page_size:
            if hasattr(self.page_size, 'to_alipay_dict'):
                params['page_size'] = self.page_size.to_alipay_dict()
            else:
                params['page_size'] = self.page_size
        if self.status_list:
            if isinstance(self.status_list, list):
                for i in range(0, len(self.status_list)):
                    element = self.status_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.status_list[i] = element.to_alipay_dict()
            if hasattr(self.status_list, 'to_alipay_dict'):
                params['status_list'] = self.status_list.to_alipay_dict()
            else:
                params['status_list'] = self.status_list
        if self.user_name_list:
            if isinstance(self.user_name_list, list):
                for i in range(0, len(self.user_name_list)):
                    element = self.user_name_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.user_name_list[i] = element.to_alipay_dict()
            if hasattr(self.user_name_list, 'to_alipay_dict'):
                params['user_name_list'] = self.user_name_list.to_alipay_dict()
            else:
                params['user_name_list'] = self.user_name_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCloudCloudrunObDumpresultQueryModel()
        if 'env' in d:
            o.env = d['env']
        if 'instance_id' in d:
            o.instance_id = d['instance_id']
        if 'page_no' in d:
            o.page_no = d['page_no']
        if 'page_size' in d:
            o.page_size = d['page_size']
        if 'status_list' in d:
            o.status_list = d['status_list']
        if 'user_name_list' in d:
            o.user_name_list = d['user_name_list']
        return o


