#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenMiniInnerversionLastQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenMiniInnerversionLastQueryResponse, self).__init__()
        self._app_desc = None
        self._app_name = None
        self._app_version = None
        self._bundle_id = None
        self._category_ids = None
        self._english_name = None
        self._logo_url = None
        self._mini_app_id = None
        self._service_phone = None
        self._slogan = None
        self._status = None
        self._sub_application_type = None

    @property
    def app_desc(self):
        return self._app_desc

    @app_desc.setter
    def app_desc(self, value):
        self._app_desc = value
    @property
    def app_name(self):
        return self._app_name

    @app_name.setter
    def app_name(self, value):
        self._app_name = value
    @property
    def app_version(self):
        return self._app_version

    @app_version.setter
    def app_version(self, value):
        self._app_version = value
    @property
    def bundle_id(self):
        return self._bundle_id

    @bundle_id.setter
    def bundle_id(self, value):
        self._bundle_id = value
    @property
    def category_ids(self):
        return self._category_ids

    @category_ids.setter
    def category_ids(self, value):
        self._category_ids = value
    @property
    def english_name(self):
        return self._english_name

    @english_name.setter
    def english_name(self, value):
        self._english_name = value
    @property
    def logo_url(self):
        return self._logo_url

    @logo_url.setter
    def logo_url(self, value):
        self._logo_url = value
    @property
    def mini_app_id(self):
        return self._mini_app_id

    @mini_app_id.setter
    def mini_app_id(self, value):
        self._mini_app_id = value
    @property
    def service_phone(self):
        return self._service_phone

    @service_phone.setter
    def service_phone(self, value):
        self._service_phone = value
    @property
    def slogan(self):
        return self._slogan

    @slogan.setter
    def slogan(self, value):
        self._slogan = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def sub_application_type(self):
        return self._sub_application_type

    @sub_application_type.setter
    def sub_application_type(self, value):
        self._sub_application_type = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenMiniInnerversionLastQueryResponse, self).parse_response_content(response_content)
        if 'app_desc' in response:
            self.app_desc = response['app_desc']
        if 'app_name' in response:
            self.app_name = response['app_name']
        if 'app_version' in response:
            self.app_version = response['app_version']
        if 'bundle_id' in response:
            self.bundle_id = response['bundle_id']
        if 'category_ids' in response:
            self.category_ids = response['category_ids']
        if 'english_name' in response:
            self.english_name = response['english_name']
        if 'logo_url' in response:
            self.logo_url = response['logo_url']
        if 'mini_app_id' in response:
            self.mini_app_id = response['mini_app_id']
        if 'service_phone' in response:
            self.service_phone = response['service_phone']
        if 'slogan' in response:
            self.slogan = response['slogan']
        if 'status' in response:
            self.status = response['status']
        if 'sub_application_type' in response:
            self.sub_application_type = response['sub_application_type']
