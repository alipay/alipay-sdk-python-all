#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.AppGroupExt import AppGroupExt
from alipay.aop.api.domain.AppSecurityExt import AppSecurityExt
from alipay.aop.api.domain.EncryptConfigExt import EncryptConfigExt
from alipay.aop.api.domain.ExterfaceExt import ExterfaceExt
from alipay.aop.api.domain.OpenIdConfigRequestExt import OpenIdConfigRequestExt
from alipay.aop.api.domain.QueryAppInfoExt import QueryAppInfoExt
from alipay.aop.api.domain.SecurityProfileExt import SecurityProfileExt


class AlipayOpenOpenbizmocktoolsQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenOpenbizmocktoolsQueryResponse, self).__init__()
        self._app_group_ext = None
        self._app_security_ext = None
        self._encrypt_config_ext = None
        self._exterface_ext = None
        self._open_id_config_request_ext = None
        self._private_key = None
        self._query_app_info_ext = None
        self._security_profile_ext = None
        self._spi_config = None

    @property
    def app_group_ext(self):
        return self._app_group_ext

    @app_group_ext.setter
    def app_group_ext(self, value):
        if isinstance(value, AppGroupExt):
            self._app_group_ext = value
        else:
            self._app_group_ext = AppGroupExt.from_alipay_dict(value)
    @property
    def app_security_ext(self):
        return self._app_security_ext

    @app_security_ext.setter
    def app_security_ext(self, value):
        if isinstance(value, list):
            self._app_security_ext = list()
            for i in value:
                if isinstance(i, AppSecurityExt):
                    self._app_security_ext.append(i)
                else:
                    self._app_security_ext.append(AppSecurityExt.from_alipay_dict(i))
    @property
    def encrypt_config_ext(self):
        return self._encrypt_config_ext

    @encrypt_config_ext.setter
    def encrypt_config_ext(self, value):
        if isinstance(value, list):
            self._encrypt_config_ext = list()
            for i in value:
                if isinstance(i, EncryptConfigExt):
                    self._encrypt_config_ext.append(i)
                else:
                    self._encrypt_config_ext.append(EncryptConfigExt.from_alipay_dict(i))
    @property
    def exterface_ext(self):
        return self._exterface_ext

    @exterface_ext.setter
    def exterface_ext(self, value):
        if isinstance(value, ExterfaceExt):
            self._exterface_ext = value
        else:
            self._exterface_ext = ExterfaceExt.from_alipay_dict(value)
    @property
    def open_id_config_request_ext(self):
        return self._open_id_config_request_ext

    @open_id_config_request_ext.setter
    def open_id_config_request_ext(self, value):
        if isinstance(value, OpenIdConfigRequestExt):
            self._open_id_config_request_ext = value
        else:
            self._open_id_config_request_ext = OpenIdConfigRequestExt.from_alipay_dict(value)
    @property
    def private_key(self):
        return self._private_key

    @private_key.setter
    def private_key(self, value):
        self._private_key = value
    @property
    def query_app_info_ext(self):
        return self._query_app_info_ext

    @query_app_info_ext.setter
    def query_app_info_ext(self, value):
        if isinstance(value, QueryAppInfoExt):
            self._query_app_info_ext = value
        else:
            self._query_app_info_ext = QueryAppInfoExt.from_alipay_dict(value)
    @property
    def security_profile_ext(self):
        return self._security_profile_ext

    @security_profile_ext.setter
    def security_profile_ext(self, value):
        if isinstance(value, list):
            self._security_profile_ext = list()
            for i in value:
                if isinstance(i, SecurityProfileExt):
                    self._security_profile_ext.append(i)
                else:
                    self._security_profile_ext.append(SecurityProfileExt.from_alipay_dict(i))
    @property
    def spi_config(self):
        return self._spi_config

    @spi_config.setter
    def spi_config(self, value):
        self._spi_config = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenOpenbizmocktoolsQueryResponse, self).parse_response_content(response_content)
        if 'app_group_ext' in response:
            self.app_group_ext = response['app_group_ext']
        if 'app_security_ext' in response:
            self.app_security_ext = response['app_security_ext']
        if 'encrypt_config_ext' in response:
            self.encrypt_config_ext = response['encrypt_config_ext']
        if 'exterface_ext' in response:
            self.exterface_ext = response['exterface_ext']
        if 'open_id_config_request_ext' in response:
            self.open_id_config_request_ext = response['open_id_config_request_ext']
        if 'private_key' in response:
            self.private_key = response['private_key']
        if 'query_app_info_ext' in response:
            self.query_app_info_ext = response['query_app_info_ext']
        if 'security_profile_ext' in response:
            self.security_profile_ext = response['security_profile_ext']
        if 'spi_config' in response:
            self.spi_config = response['spi_config']
