#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenMiniInnerbaseinfoQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenMiniInnerbaseinfoQueryResponse, self).__init__()
        self._app_category_ids = None
        self._app_desc = None
        self._app_english_name = None
        self._app_logo = None
        self._app_name = None
        self._app_slogan = None
        self._service_email = None
        self._service_phone = None

    @property
    def app_category_ids(self):
        return self._app_category_ids

    @app_category_ids.setter
    def app_category_ids(self, value):
        self._app_category_ids = value
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
        response = super(AlipayOpenMiniInnerbaseinfoQueryResponse, self).parse_response_content(response_content)
        if 'app_category_ids' in response:
            self.app_category_ids = response['app_category_ids']
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
        if 'service_email' in response:
            self.service_email = response['service_email']
        if 'service_phone' in response:
            self.service_phone = response['service_phone']
