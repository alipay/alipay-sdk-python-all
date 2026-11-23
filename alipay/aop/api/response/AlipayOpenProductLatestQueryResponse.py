#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.AbilityItem import AbilityItem
from alipay.aop.api.domain.MiniAppInfo import MiniAppInfo


class AlipayOpenProductLatestQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenProductLatestQueryResponse, self).__init__()
        self._abilities = None
        self._interaction_protocol = None
        self._mini_apps = None
        self._product_code = None
        self._product_version = None

    @property
    def abilities(self):
        return self._abilities

    @abilities.setter
    def abilities(self, value):
        if isinstance(value, list):
            self._abilities = list()
            for i in value:
                if isinstance(i, AbilityItem):
                    self._abilities.append(i)
                else:
                    self._abilities.append(AbilityItem.from_alipay_dict(i))
    @property
    def interaction_protocol(self):
        return self._interaction_protocol

    @interaction_protocol.setter
    def interaction_protocol(self, value):
        self._interaction_protocol = value
    @property
    def mini_apps(self):
        return self._mini_apps

    @mini_apps.setter
    def mini_apps(self, value):
        if isinstance(value, list):
            self._mini_apps = list()
            for i in value:
                if isinstance(i, MiniAppInfo):
                    self._mini_apps.append(i)
                else:
                    self._mini_apps.append(MiniAppInfo.from_alipay_dict(i))
    @property
    def product_code(self):
        return self._product_code

    @product_code.setter
    def product_code(self, value):
        self._product_code = value
    @property
    def product_version(self):
        return self._product_version

    @product_version.setter
    def product_version(self, value):
        self._product_version = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenProductLatestQueryResponse, self).parse_response_content(response_content)
        if 'abilities' in response:
            self.abilities = response['abilities']
        if 'interaction_protocol' in response:
            self.interaction_protocol = response['interaction_protocol']
        if 'mini_apps' in response:
            self.mini_apps = response['mini_apps']
        if 'product_code' in response:
            self.product_code = response['product_code']
        if 'product_version' in response:
            self.product_version = response['product_version']
