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
        self._app_key = None
        self._app_logo = None
        self._app_name = None
        self._app_slogan = None
        self._app_sub_type = None
        self._dev_id = None
        self._gmt_create = None
        self._gmt_modified = None
        self._mini_app_id = None
        self._origin = None
        self._owner_entity = None
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
    def app_key(self):
        return self._app_key

    @app_key.setter
    def app_key(self, value):
        self._app_key = value
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
    def app_sub_type(self):
        return self._app_sub_type

    @app_sub_type.setter
    def app_sub_type(self, value):
        self._app_sub_type = value
    @property
    def dev_id(self):
        return self._dev_id

    @dev_id.setter
    def dev_id(self, value):
        self._dev_id = value
    @property
    def gmt_create(self):
        return self._gmt_create

    @gmt_create.setter
    def gmt_create(self, value):
        self._gmt_create = value
    @property
    def gmt_modified(self):
        return self._gmt_modified

    @gmt_modified.setter
    def gmt_modified(self, value):
        self._gmt_modified = value
    @property
    def mini_app_id(self):
        return self._mini_app_id

    @mini_app_id.setter
    def mini_app_id(self, value):
        self._mini_app_id = value
    @property
    def origin(self):
        return self._origin

    @origin.setter
    def origin(self, value):
        self._origin = value
    @property
    def owner_entity(self):
        return self._owner_entity

    @owner_entity.setter
    def owner_entity(self, value):
        self._owner_entity = value
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
        if 'app_key' in response:
            self.app_key = response['app_key']
        if 'app_logo' in response:
            self.app_logo = response['app_logo']
        if 'app_name' in response:
            self.app_name = response['app_name']
        if 'app_slogan' in response:
            self.app_slogan = response['app_slogan']
        if 'app_sub_type' in response:
            self.app_sub_type = response['app_sub_type']
        if 'dev_id' in response:
            self.dev_id = response['dev_id']
        if 'gmt_create' in response:
            self.gmt_create = response['gmt_create']
        if 'gmt_modified' in response:
            self.gmt_modified = response['gmt_modified']
        if 'mini_app_id' in response:
            self.mini_app_id = response['mini_app_id']
        if 'origin' in response:
            self.origin = response['origin']
        if 'owner_entity' in response:
            self.owner_entity = response['owner_entity']
        if 'service_email' in response:
            self.service_email = response['service_email']
        if 'service_phone' in response:
            self.service_phone = response['service_phone']
