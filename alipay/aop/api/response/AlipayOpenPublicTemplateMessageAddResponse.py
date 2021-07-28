#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenPublicTemplateMessageAddResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenPublicTemplateMessageAddResponse, self).__init__()
        self._template = None
        self._template_id = None

    @property
    def template(self):
        return self._template

    @template.setter
    def template(self, value):
        self._template = value
    @property
    def template_id(self):
        return self._template_id

    @template_id.setter
    def template_id(self, value):
        self._template_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenPublicTemplateMessageAddResponse, self).parse_response_content(response_content)
        if 'template' in response:
            self.template = response['template']
        if 'template_id' in response:
            self.template_id = response['template_id']
