#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class ZhimaMerchantZmgoTemplateCreateResponse(AlipayResponse):

    def __init__(self):
        super(ZhimaMerchantZmgoTemplateCreateResponse, self).__init__()
        self._template_no = None

    @property
    def template_no(self):
        return self._template_no

    @template_no.setter
    def template_no(self, value):
        self._template_no = value

    def parse_response_content(self, response_content):
        response = super(ZhimaMerchantZmgoTemplateCreateResponse, self).parse_response_content(response_content)
        if 'template_no' in response:
            self.template_no = response['template_no']
