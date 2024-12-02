#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceWithholdrepayorderAgreementSignResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceWithholdrepayorderAgreementSignResponse, self).__init__()
        self._page_redirection_data = None
        self._shortened_page_redirection_url = None

    @property
    def page_redirection_data(self):
        return self._page_redirection_data

    @page_redirection_data.setter
    def page_redirection_data(self, value):
        self._page_redirection_data = value
    @property
    def shortened_page_redirection_url(self):
        return self._shortened_page_redirection_url

    @shortened_page_redirection_url.setter
    def shortened_page_redirection_url(self, value):
        self._shortened_page_redirection_url = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceWithholdrepayorderAgreementSignResponse, self).parse_response_content(response_content)
        if 'page_redirection_data' in response:
            self.page_redirection_data = response['page_redirection_data']
        if 'shortened_page_redirection_url' in response:
            self.shortened_page_redirection_url = response['shortened_page_redirection_url']
