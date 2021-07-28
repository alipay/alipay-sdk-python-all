#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.AppAttribute import AppAttribute
from alipay.aop.api.domain.ServiceUrl import ServiceUrl


class AlipayOpenAppAppcontentFunctionCreateModel(object):

    def __init__(self):
        self._area_codes = None
        self._category_attributes = None
        self._category_ids = None
        self._icon = None
        self._key_words = None
        self._service_name = None
        self._service_time_end = None
        self._service_time_start = None
        self._service_urls = None
        self._short_desc = None

    @property
    def area_codes(self):
        return self._area_codes

    @area_codes.setter
    def area_codes(self, value):
        if isinstance(value, list):
            self._area_codes = list()
            for i in value:
                self._area_codes.append(i)
    @property
    def category_attributes(self):
        return self._category_attributes

    @category_attributes.setter
    def category_attributes(self, value):
        if isinstance(value, list):
            self._category_attributes = list()
            for i in value:
                if isinstance(i, AppAttribute):
                    self._category_attributes.append(i)
                else:
                    self._category_attributes.append(AppAttribute.from_alipay_dict(i))
    @property
    def category_ids(self):
        return self._category_ids

    @category_ids.setter
    def category_ids(self, value):
        if isinstance(value, list):
            self._category_ids = list()
            for i in value:
                self._category_ids.append(i)
    @property
    def icon(self):
        return self._icon

    @icon.setter
    def icon(self, value):
        self._icon = value
    @property
    def key_words(self):
        return self._key_words

    @key_words.setter
    def key_words(self, value):
        if isinstance(value, list):
            self._key_words = list()
            for i in value:
                self._key_words.append(i)
    @property
    def service_name(self):
        return self._service_name

    @service_name.setter
    def service_name(self, value):
        self._service_name = value
    @property
    def service_time_end(self):
        return self._service_time_end

    @service_time_end.setter
    def service_time_end(self, value):
        self._service_time_end = value
    @property
    def service_time_start(self):
        return self._service_time_start

    @service_time_start.setter
    def service_time_start(self, value):
        self._service_time_start = value
    @property
    def service_urls(self):
        return self._service_urls

    @service_urls.setter
    def service_urls(self, value):
        if isinstance(value, list):
            self._service_urls = list()
            for i in value:
                if isinstance(i, ServiceUrl):
                    self._service_urls.append(i)
                else:
                    self._service_urls.append(ServiceUrl.from_alipay_dict(i))
    @property
    def short_desc(self):
        return self._short_desc

    @short_desc.setter
    def short_desc(self, value):
        self._short_desc = value


    def to_alipay_dict(self):
        params = dict()
        if self.area_codes:
            if isinstance(self.area_codes, list):
                for i in range(0, len(self.area_codes)):
                    element = self.area_codes[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.area_codes[i] = element.to_alipay_dict()
            if hasattr(self.area_codes, 'to_alipay_dict'):
                params['area_codes'] = self.area_codes.to_alipay_dict()
            else:
                params['area_codes'] = self.area_codes
        if self.category_attributes:
            if isinstance(self.category_attributes, list):
                for i in range(0, len(self.category_attributes)):
                    element = self.category_attributes[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.category_attributes[i] = element.to_alipay_dict()
            if hasattr(self.category_attributes, 'to_alipay_dict'):
                params['category_attributes'] = self.category_attributes.to_alipay_dict()
            else:
                params['category_attributes'] = self.category_attributes
        if self.category_ids:
            if isinstance(self.category_ids, list):
                for i in range(0, len(self.category_ids)):
                    element = self.category_ids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.category_ids[i] = element.to_alipay_dict()
            if hasattr(self.category_ids, 'to_alipay_dict'):
                params['category_ids'] = self.category_ids.to_alipay_dict()
            else:
                params['category_ids'] = self.category_ids
        if self.icon:
            if hasattr(self.icon, 'to_alipay_dict'):
                params['icon'] = self.icon.to_alipay_dict()
            else:
                params['icon'] = self.icon
        if self.key_words:
            if isinstance(self.key_words, list):
                for i in range(0, len(self.key_words)):
                    element = self.key_words[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.key_words[i] = element.to_alipay_dict()
            if hasattr(self.key_words, 'to_alipay_dict'):
                params['key_words'] = self.key_words.to_alipay_dict()
            else:
                params['key_words'] = self.key_words
        if self.service_name:
            if hasattr(self.service_name, 'to_alipay_dict'):
                params['service_name'] = self.service_name.to_alipay_dict()
            else:
                params['service_name'] = self.service_name
        if self.service_time_end:
            if hasattr(self.service_time_end, 'to_alipay_dict'):
                params['service_time_end'] = self.service_time_end.to_alipay_dict()
            else:
                params['service_time_end'] = self.service_time_end
        if self.service_time_start:
            if hasattr(self.service_time_start, 'to_alipay_dict'):
                params['service_time_start'] = self.service_time_start.to_alipay_dict()
            else:
                params['service_time_start'] = self.service_time_start
        if self.service_urls:
            if isinstance(self.service_urls, list):
                for i in range(0, len(self.service_urls)):
                    element = self.service_urls[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.service_urls[i] = element.to_alipay_dict()
            if hasattr(self.service_urls, 'to_alipay_dict'):
                params['service_urls'] = self.service_urls.to_alipay_dict()
            else:
                params['service_urls'] = self.service_urls
        if self.short_desc:
            if hasattr(self.short_desc, 'to_alipay_dict'):
                params['short_desc'] = self.short_desc.to_alipay_dict()
            else:
                params['short_desc'] = self.short_desc
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenAppAppcontentFunctionCreateModel()
        if 'area_codes' in d:
            o.area_codes = d['area_codes']
        if 'category_attributes' in d:
            o.category_attributes = d['category_attributes']
        if 'category_ids' in d:
            o.category_ids = d['category_ids']
        if 'icon' in d:
            o.icon = d['icon']
        if 'key_words' in d:
            o.key_words = d['key_words']
        if 'service_name' in d:
            o.service_name = d['service_name']
        if 'service_time_end' in d:
            o.service_time_end = d['service_time_end']
        if 'service_time_start' in d:
            o.service_time_start = d['service_time_start']
        if 'service_urls' in d:
            o.service_urls = d['service_urls']
        if 'short_desc' in d:
            o.short_desc = d['short_desc']
        return o


