#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayFundWalletTemplateModifyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayFundWalletTemplateModifyResponse, self).__init__()
        self._template_id = None
        self._template_name = None

    @property
    def template_id(self):
        return self._template_id

    @template_id.setter
    def template_id(self, value):
        self._template_id = value
    @property
    def template_name(self):
        return self._template_name

    @template_name.setter
    def template_name(self, value):
        self._template_name = value

    def parse_response_content(self, response_content):
        response = super(AlipayFundWalletTemplateModifyResponse, self).parse_response_content(response_content)
        if 'template_id' in response:
            self.template_id = response['template_id']
        if 'template_name' in response:
            self.template_name = response['template_name']
