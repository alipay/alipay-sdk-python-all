#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCloudCloudpromoMessageTemplateModifyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCloudCloudpromoMessageTemplateModifyResponse, self).__init__()
        self._template_code = None

    @property
    def template_code(self):
        return self._template_code

    @template_code.setter
    def template_code(self, value):
        self._template_code = value

    def parse_response_content(self, response_content):
        response = super(AlipayCloudCloudpromoMessageTemplateModifyResponse, self).parse_response_content(response_content)
        if 'template_code' in response:
            self.template_code = response['template_code']
