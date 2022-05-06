#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.SearchBoxAccountModule import SearchBoxAccountModule
from alipay.aop.api.domain.SearchBoxBasicInfoModule import SearchBoxBasicInfoModule
from alipay.aop.api.domain.SearchBoxKeyWordModule import SearchBoxKeyWordModule
from alipay.aop.api.domain.SearchBoxImageModule import SearchBoxImageModule
from alipay.aop.api.domain.SearchBoxServiceModule import SearchBoxServiceModule
from alipay.aop.api.domain.SearchBoxImageModule import SearchBoxImageModule


class AlipayOpenSearchBoxQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenSearchBoxQueryResponse, self).__init__()
        self._account_module = None
        self._basic_info_module = None
        self._box_id = None
        self._box_status = None
        self._default_keywords = None
        self._keyword_module = None
        self._latest_audit_image = None
        self._service_module = None
        self._valid_image = None

    @property
    def account_module(self):
        return self._account_module

    @account_module.setter
    def account_module(self, value):
        if isinstance(value, SearchBoxAccountModule):
            self._account_module = value
        else:
            self._account_module = SearchBoxAccountModule.from_alipay_dict(value)
    @property
    def basic_info_module(self):
        return self._basic_info_module

    @basic_info_module.setter
    def basic_info_module(self, value):
        if isinstance(value, SearchBoxBasicInfoModule):
            self._basic_info_module = value
        else:
            self._basic_info_module = SearchBoxBasicInfoModule.from_alipay_dict(value)
    @property
    def box_id(self):
        return self._box_id

    @box_id.setter
    def box_id(self, value):
        self._box_id = value
    @property
    def box_status(self):
        return self._box_status

    @box_status.setter
    def box_status(self, value):
        self._box_status = value
    @property
    def default_keywords(self):
        return self._default_keywords

    @default_keywords.setter
    def default_keywords(self, value):
        if isinstance(value, list):
            self._default_keywords = list()
            for i in value:
                self._default_keywords.append(i)
    @property
    def keyword_module(self):
        return self._keyword_module

    @keyword_module.setter
    def keyword_module(self, value):
        if isinstance(value, SearchBoxKeyWordModule):
            self._keyword_module = value
        else:
            self._keyword_module = SearchBoxKeyWordModule.from_alipay_dict(value)
    @property
    def latest_audit_image(self):
        return self._latest_audit_image

    @latest_audit_image.setter
    def latest_audit_image(self, value):
        if isinstance(value, SearchBoxImageModule):
            self._latest_audit_image = value
        else:
            self._latest_audit_image = SearchBoxImageModule.from_alipay_dict(value)
    @property
    def service_module(self):
        return self._service_module

    @service_module.setter
    def service_module(self, value):
        if isinstance(value, SearchBoxServiceModule):
            self._service_module = value
        else:
            self._service_module = SearchBoxServiceModule.from_alipay_dict(value)
    @property
    def valid_image(self):
        return self._valid_image

    @valid_image.setter
    def valid_image(self, value):
        if isinstance(value, SearchBoxImageModule):
            self._valid_image = value
        else:
            self._valid_image = SearchBoxImageModule.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayOpenSearchBoxQueryResponse, self).parse_response_content(response_content)
        if 'account_module' in response:
            self.account_module = response['account_module']
        if 'basic_info_module' in response:
            self.basic_info_module = response['basic_info_module']
        if 'box_id' in response:
            self.box_id = response['box_id']
        if 'box_status' in response:
            self.box_status = response['box_status']
        if 'default_keywords' in response:
            self.default_keywords = response['default_keywords']
        if 'keyword_module' in response:
            self.keyword_module = response['keyword_module']
        if 'latest_audit_image' in response:
            self.latest_audit_image = response['latest_audit_image']
        if 'service_module' in response:
            self.service_module = response['service_module']
        if 'valid_image' in response:
            self.valid_image = response['valid_image']
