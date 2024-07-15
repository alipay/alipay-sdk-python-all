#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipaySecurityProdTemplateVersionPublishResponse(AlipayResponse):

    def __init__(self):
        super(AlipaySecurityProdTemplateVersionPublishResponse, self).__init__()
        self._publish_result = None

    @property
    def publish_result(self):
        return self._publish_result

    @publish_result.setter
    def publish_result(self, value):
        self._publish_result = value

    def parse_response_content(self, response_content):
        response = super(AlipaySecurityProdTemplateVersionPublishResponse, self).parse_response_content(response_content)
        if 'publish_result' in response:
            self.publish_result = response['publish_result']
