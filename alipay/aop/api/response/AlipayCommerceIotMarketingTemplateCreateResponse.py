#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceIotMarketingTemplateCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceIotMarketingTemplateCreateResponse, self).__init__()
        self._status_code = None
        self._template_id = None

    @property
    def status_code(self):
        return self._status_code

    @status_code.setter
    def status_code(self, value):
        self._status_code = value
    @property
    def template_id(self):
        return self._template_id

    @template_id.setter
    def template_id(self, value):
        self._template_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceIotMarketingTemplateCreateResponse, self).parse_response_content(response_content)
        if 'status_code' in response:
            self.status_code = response['status_code']
        if 'template_id' in response:
            self.template_id = response['template_id']
