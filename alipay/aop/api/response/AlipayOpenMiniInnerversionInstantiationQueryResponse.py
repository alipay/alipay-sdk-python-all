#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenMiniInnerversionInstantiationQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenMiniInnerversionInstantiationQueryResponse, self).__init__()
        self._app_version = None
        self._bundle_id = None
        self._mini_app_id = None
        self._template_id = None
        self._template_version = None

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
    def mini_app_id(self):
        return self._mini_app_id

    @mini_app_id.setter
    def mini_app_id(self, value):
        self._mini_app_id = value
    @property
    def template_id(self):
        return self._template_id

    @template_id.setter
    def template_id(self, value):
        self._template_id = value
    @property
    def template_version(self):
        return self._template_version

    @template_version.setter
    def template_version(self, value):
        self._template_version = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenMiniInnerversionInstantiationQueryResponse, self).parse_response_content(response_content)
        if 'app_version' in response:
            self.app_version = response['app_version']
        if 'bundle_id' in response:
            self.bundle_id = response['bundle_id']
        if 'mini_app_id' in response:
            self.mini_app_id = response['mini_app_id']
        if 'template_id' in response:
            self.template_id = response['template_id']
        if 'template_version' in response:
            self.template_version = response['template_version']
