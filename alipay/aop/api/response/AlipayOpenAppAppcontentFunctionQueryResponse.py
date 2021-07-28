#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.AppAttribute import AppAttribute
from alipay.aop.api.domain.ServiceUrl import ServiceUrl


class AlipayOpenAppAppcontentFunctionQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenAppAppcontentFunctionQueryResponse, self).__init__()
        self._area_codes = None
        self._audit_status = None
        self._category_attributes = None
        self._category_ids = None
        self._icon = None
        self._key_words = None
        self._major_status = None
        self._reject_reason = None
        self._service_code = None
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
    def audit_status(self):
        return self._audit_status

    @audit_status.setter
    def audit_status(self, value):
        self._audit_status = value
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
    def major_status(self):
        return self._major_status

    @major_status.setter
    def major_status(self, value):
        self._major_status = value
    @property
    def reject_reason(self):
        return self._reject_reason

    @reject_reason.setter
    def reject_reason(self, value):
        self._reject_reason = value
    @property
    def service_code(self):
        return self._service_code

    @service_code.setter
    def service_code(self, value):
        self._service_code = value
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

    def parse_response_content(self, response_content):
        response = super(AlipayOpenAppAppcontentFunctionQueryResponse, self).parse_response_content(response_content)
        if 'area_codes' in response:
            self.area_codes = response['area_codes']
        if 'audit_status' in response:
            self.audit_status = response['audit_status']
        if 'category_attributes' in response:
            self.category_attributes = response['category_attributes']
        if 'category_ids' in response:
            self.category_ids = response['category_ids']
        if 'icon' in response:
            self.icon = response['icon']
        if 'key_words' in response:
            self.key_words = response['key_words']
        if 'major_status' in response:
            self.major_status = response['major_status']
        if 'reject_reason' in response:
            self.reject_reason = response['reject_reason']
        if 'service_code' in response:
            self.service_code = response['service_code']
        if 'service_name' in response:
            self.service_name = response['service_name']
        if 'service_time_end' in response:
            self.service_time_end = response['service_time_end']
        if 'service_time_start' in response:
            self.service_time_start = response['service_time_start']
        if 'service_urls' in response:
            self.service_urls = response['service_urls']
        if 'short_desc' in response:
            self.short_desc = response['short_desc']
