#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenOpenbizmocktoolsCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenOpenbizmocktoolsCreateResponse, self).__init__()
        self._app_number = None
        self._auth_token = None
        self._group_id = None
        self._open_id = None
        self._package_code = None
        self._spi_config = None
        self._uid = None
        self._union_id = None

    @property
    def app_number(self):
        return self._app_number

    @app_number.setter
    def app_number(self, value):
        self._app_number = value
    @property
    def auth_token(self):
        return self._auth_token

    @auth_token.setter
    def auth_token(self, value):
        self._auth_token = value
    @property
    def group_id(self):
        return self._group_id

    @group_id.setter
    def group_id(self, value):
        self._group_id = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def package_code(self):
        return self._package_code

    @package_code.setter
    def package_code(self, value):
        self._package_code = value
    @property
    def spi_config(self):
        return self._spi_config

    @spi_config.setter
    def spi_config(self, value):
        self._spi_config = value
    @property
    def uid(self):
        return self._uid

    @uid.setter
    def uid(self, value):
        self._uid = value
    @property
    def union_id(self):
        return self._union_id

    @union_id.setter
    def union_id(self, value):
        self._union_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenOpenbizmocktoolsCreateResponse, self).parse_response_content(response_content)
        if 'app_number' in response:
            self.app_number = response['app_number']
        if 'auth_token' in response:
            self.auth_token = response['auth_token']
        if 'group_id' in response:
            self.group_id = response['group_id']
        if 'open_id' in response:
            self.open_id = response['open_id']
        if 'package_code' in response:
            self.package_code = response['package_code']
        if 'spi_config' in response:
            self.spi_config = response['spi_config']
        if 'uid' in response:
            self.uid = response['uid']
        if 'union_id' in response:
            self.union_id = response['union_id']
