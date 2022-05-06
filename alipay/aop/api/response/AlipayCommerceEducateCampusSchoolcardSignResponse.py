#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceEducateCampusSchoolcardSignResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceEducateCampusSchoolcardSignResponse, self).__init__()
        self._schema_url = None

    @property
    def schema_url(self):
        return self._schema_url

    @schema_url.setter
    def schema_url(self, value):
        self._schema_url = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceEducateCampusSchoolcardSignResponse, self).parse_response_content(response_content)
        if 'schema_url' in response:
            self.schema_url = response['schema_url']
