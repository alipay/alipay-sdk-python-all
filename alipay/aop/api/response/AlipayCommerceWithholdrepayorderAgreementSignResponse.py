#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceWithholdrepayorderAgreementSignResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceWithholdrepayorderAgreementSignResponse, self).__init__()
        self._page_redirection_data = None

    @property
    def page_redirection_data(self):
        return self._page_redirection_data

    @page_redirection_data.setter
    def page_redirection_data(self, value):
        self._page_redirection_data = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceWithholdrepayorderAgreementSignResponse, self).parse_response_content(response_content)
        if 'page_redirection_data' in response:
            self.page_redirection_data = response['page_redirection_data']
