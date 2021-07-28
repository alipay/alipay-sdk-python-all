#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayEcoDocTemplateCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEcoDocTemplateCreateResponse, self).__init__()
        self._template_id = None
        self._upload_url = None

    @property
    def template_id(self):
        return self._template_id

    @template_id.setter
    def template_id(self, value):
        self._template_id = value
    @property
    def upload_url(self):
        return self._upload_url

    @upload_url.setter
    def upload_url(self, value):
        self._upload_url = value

    def parse_response_content(self, response_content):
        response = super(AlipayEcoDocTemplateCreateResponse, self).parse_response_content(response_content)
        if 'template_id' in response:
            self.template_id = response['template_id']
        if 'upload_url' in response:
            self.upload_url = response['upload_url']
