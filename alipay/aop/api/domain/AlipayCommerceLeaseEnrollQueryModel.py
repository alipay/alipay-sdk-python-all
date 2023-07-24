#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceLeaseEnrollQueryModel(object):

    def __init__(self):
        self._brand_tags = None
        self._name = None
        self._page = None
        self._page_size = None

    @property
    def brand_tags(self):
        return self._brand_tags

    @brand_tags.setter
    def brand_tags(self, value):
        if isinstance(value, list):
            self._brand_tags = list()
            for i in value:
                self._brand_tags.append(i)
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def page(self):
        return self._page

    @page.setter
    def page(self, value):
        self._page = value
    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, value):
        self._page_size = value


    def to_alipay_dict(self):
        params = dict()
        if self.brand_tags:
            if isinstance(self.brand_tags, list):
                for i in range(0, len(self.brand_tags)):
                    element = self.brand_tags[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.brand_tags[i] = element.to_alipay_dict()
            if hasattr(self.brand_tags, 'to_alipay_dict'):
                params['brand_tags'] = self.brand_tags.to_alipay_dict()
            else:
                params['brand_tags'] = self.brand_tags
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.page:
            if hasattr(self.page, 'to_alipay_dict'):
                params['page'] = self.page.to_alipay_dict()
            else:
                params['page'] = self.page
        if self.page_size:
            if hasattr(self.page_size, 'to_alipay_dict'):
                params['page_size'] = self.page_size.to_alipay_dict()
            else:
                params['page_size'] = self.page_size
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceLeaseEnrollQueryModel()
        if 'brand_tags' in d:
            o.brand_tags = d['brand_tags']
        if 'name' in d:
            o.name = d['name']
        if 'page' in d:
            o.page = d['page']
        if 'page_size' in d:
            o.page_size = d['page_size']
        return o


