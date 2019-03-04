#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.Agreement import Agreement


class AlipayOpenAuthAppContentQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenAuthAppContentQueryResponse, self).__init__()
        self._agreement = None
        self._auth_text = None

    @property
    def agreement(self):
        return self._agreement

    @agreement.setter
    def agreement(self, value):
        if isinstance(value, list):
            self._agreement = list()
            for i in value:
                if isinstance(i, Agreement):
                    self._agreement.append(i)
                else:
                    self._agreement.append(Agreement.from_alipay_dict(i))
    @property
    def auth_text(self):
        return self._auth_text

    @auth_text.setter
    def auth_text(self, value):
        if isinstance(value, list):
            self._auth_text = list()
            for i in value:
                self._auth_text.append(i)

    def parse_response_content(self, response_content):
        response = super(AlipayOpenAuthAppContentQueryResponse, self).parse_response_content(response_content)
        if 'agreement' in response:
            self.agreement = response['agreement']
        if 'auth_text' in response:
            self.auth_text = response['auth_text']
