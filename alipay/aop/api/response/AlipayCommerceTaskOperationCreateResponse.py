#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceTaskOperationCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceTaskOperationCreateResponse, self).__init__()
        self._platform_template_id = None
        self._template_id = None
        self._type = None

    @property
    def platform_template_id(self):
        return self._platform_template_id

    @platform_template_id.setter
    def platform_template_id(self, value):
        self._platform_template_id = value
    @property
    def template_id(self):
        return self._template_id

    @template_id.setter
    def template_id(self, value):
        self._template_id = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceTaskOperationCreateResponse, self).parse_response_content(response_content)
        if 'platform_template_id' in response:
            self.platform_template_id = response['platform_template_id']
        if 'template_id' in response:
            self.template_id = response['template_id']
        if 'type' in response:
            self.type = response['type']
