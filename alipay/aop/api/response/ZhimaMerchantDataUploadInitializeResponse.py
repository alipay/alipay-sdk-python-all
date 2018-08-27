#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class ZhimaMerchantDataUploadInitializeResponse(AlipayResponse):

    def __init__(self):
        super(ZhimaMerchantDataUploadInitializeResponse, self).__init__()
        self._template_url = None

    @property
    def template_url(self):
        return self._template_url

    @template_url.setter
    def template_url(self, value):
        self._template_url = value

    def parse_response_content(self, response_content):
        response = super(ZhimaMerchantDataUploadInitializeResponse, self).parse_response_content(response_content)
        if 'template_url' in response:
            self.template_url = response['template_url']
