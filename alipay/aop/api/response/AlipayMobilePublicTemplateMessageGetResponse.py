#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayMobilePublicTemplateMessageGetResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMobilePublicTemplateMessageGetResponse, self).__init__()
        self._msg_template_id = None
        self._template = None

    @property
    def msg_template_id(self):
        return self._msg_template_id

    @msg_template_id.setter
    def msg_template_id(self, value):
        self._msg_template_id = value
    @property
    def template(self):
        return self._template

    @template.setter
    def template(self, value):
        self._template = value

    def parse_response_content(self, response_content):
        response = super(AlipayMobilePublicTemplateMessageGetResponse, self).parse_response_content(response_content)
        if 'msg_template_id' in response:
            self.msg_template_id = response['msg_template_id']
        if 'template' in response:
            self.template = response['template']
