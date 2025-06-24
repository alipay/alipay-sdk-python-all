#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceCityfacilitatorIotnsphgHgauthGetResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceCityfacilitatorIotnsphgHgauthGetResponse, self).__init__()
        self._agreement_no = None
        self._auth_content = None

    @property
    def agreement_no(self):
        return self._agreement_no

    @agreement_no.setter
    def agreement_no(self, value):
        self._agreement_no = value
    @property
    def auth_content(self):
        return self._auth_content

    @auth_content.setter
    def auth_content(self, value):
        self._auth_content = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceCityfacilitatorIotnsphgHgauthGetResponse, self).parse_response_content(response_content)
        if 'agreement_no' in response:
            self.agreement_no = response['agreement_no']
        if 'auth_content' in response:
            self.auth_content = response['auth_content']
