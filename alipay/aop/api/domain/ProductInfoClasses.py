#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.FileInfoClasses import FileInfoClasses
from alipay.aop.api.domain.OnlineShopClasses import OnlineShopClasses


class ProductInfoClasses(object):

    def __init__(self):
        self._file_list = None
        self._online_store_info_list = None
        self._product_description = None
        self._product_name = None
        self._service_url = None

    @property
    def file_list(self):
        return self._file_list

    @file_list.setter
    def file_list(self, value):
        if isinstance(value, list):
            self._file_list = list()
            for i in value:
                if isinstance(i, FileInfoClasses):
                    self._file_list.append(i)
                else:
                    self._file_list.append(FileInfoClasses.from_alipay_dict(i))
    @property
    def online_store_info_list(self):
        return self._online_store_info_list

    @online_store_info_list.setter
    def online_store_info_list(self, value):
        if isinstance(value, list):
            self._online_store_info_list = list()
            for i in value:
                if isinstance(i, OnlineShopClasses):
                    self._online_store_info_list.append(i)
                else:
                    self._online_store_info_list.append(OnlineShopClasses.from_alipay_dict(i))
    @property
    def product_description(self):
        return self._product_description

    @product_description.setter
    def product_description(self, value):
        self._product_description = value
    @property
    def product_name(self):
        return self._product_name

    @product_name.setter
    def product_name(self, value):
        self._product_name = value
    @property
    def service_url(self):
        return self._service_url

    @service_url.setter
    def service_url(self, value):
        if isinstance(value, list):
            self._service_url = list()
            for i in value:
                self._service_url.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.file_list:
            if isinstance(self.file_list, list):
                for i in range(0, len(self.file_list)):
                    element = self.file_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.file_list[i] = element.to_alipay_dict()
            if hasattr(self.file_list, 'to_alipay_dict'):
                params['file_list'] = self.file_list.to_alipay_dict()
            else:
                params['file_list'] = self.file_list
        if self.online_store_info_list:
            if isinstance(self.online_store_info_list, list):
                for i in range(0, len(self.online_store_info_list)):
                    element = self.online_store_info_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.online_store_info_list[i] = element.to_alipay_dict()
            if hasattr(self.online_store_info_list, 'to_alipay_dict'):
                params['online_store_info_list'] = self.online_store_info_list.to_alipay_dict()
            else:
                params['online_store_info_list'] = self.online_store_info_list
        if self.product_description:
            if hasattr(self.product_description, 'to_alipay_dict'):
                params['product_description'] = self.product_description.to_alipay_dict()
            else:
                params['product_description'] = self.product_description
        if self.product_name:
            if hasattr(self.product_name, 'to_alipay_dict'):
                params['product_name'] = self.product_name.to_alipay_dict()
            else:
                params['product_name'] = self.product_name
        if self.service_url:
            if isinstance(self.service_url, list):
                for i in range(0, len(self.service_url)):
                    element = self.service_url[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.service_url[i] = element.to_alipay_dict()
            if hasattr(self.service_url, 'to_alipay_dict'):
                params['service_url'] = self.service_url.to_alipay_dict()
            else:
                params['service_url'] = self.service_url
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ProductInfoClasses()
        if 'file_list' in d:
            o.file_list = d['file_list']
        if 'online_store_info_list' in d:
            o.online_store_info_list = d['online_store_info_list']
        if 'product_description' in d:
            o.product_description = d['product_description']
        if 'product_name' in d:
            o.product_name = d['product_name']
        if 'service_url' in d:
            o.service_url = d['service_url']
        return o


