#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenMiniBaseinfoQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenMiniBaseinfoQueryResponse, self).__init__()
        self._app_desc = None
        self._app_english_name = None
        self._app_logo = None
        self._app_name = None
        self._app_slogan = None
        self._category_names = None
        self._package_names = None
        self._safe_domains = None
        self._service_email = None
        self._service_phone = None

    @property
    def app_desc(self):
        return self._app_desc

    @app_desc.setter
    def app_desc(self, value):
        self._app_desc = value
    @property
    def app_english_name(self):
        return self._app_english_name

    @app_english_name.setter
    def app_english_name(self, value):
        self._app_english_name = value
    @property
    def app_logo(self):
        return self._app_logo

    @app_logo.setter
    def app_logo(self, value):
        self._app_logo = value
    @property
    def app_name(self):
        return self._app_name

    @app_name.setter
    def app_name(self, value):
        self._app_name = value
    @property
    def app_slogan(self):
        return self._app_slogan

    @app_slogan.setter
    def app_slogan(self, value):
        self._app_slogan = value
    @property
    def category_names(self):
        return self._category_names

    @category_names.setter
    def category_names(self, value):
        self._category_names = value
    @property
    def package_names(self):
        return self._package_names

    @package_names.setter
    def package_names(self, value):
        if isinstance(value, list):
            self._package_names = list()
            for i in value:
                self._package_names.append(i)
    @property
    def safe_domains(self):
        return self._safe_domains

    @safe_domains.setter
    def safe_domains(self, value):
        if isinstance(value, list):
            self._safe_domains = list()
            for i in value:
                self._safe_domains.append(i)
    @property
    def service_email(self):
        return self._service_email

    @service_email.setter
    def service_email(self, value):
        self._service_email = value
    @property
    def service_phone(self):
        return self._service_phone

    @service_phone.setter
    def service_phone(self, value):
        self._service_phone = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenMiniBaseinfoQueryResponse, self).parse_response_content(response_content)
        if 'app_desc' in response:
            self.app_desc = response['app_desc']
        if 'app_english_name' in response:
            self.app_english_name = response['app_english_name']
        if 'app_logo' in response:
            self.app_logo = response['app_logo']
        if 'app_name' in response:
            self.app_name = response['app_name']
        if 'app_slogan' in response:
            self.app_slogan = response['app_slogan']
        if 'category_names' in response:
            self.category_names = response['category_names']
        if 'package_names' in response:
            self.package_names = response['package_names']
        if 'safe_domains' in response:
            self.safe_domains = response['safe_domains']
        if 'service_email' in response:
            self.service_email = response['service_email']
        if 'service_phone' in response:
            self.service_phone = response['service_phone']
