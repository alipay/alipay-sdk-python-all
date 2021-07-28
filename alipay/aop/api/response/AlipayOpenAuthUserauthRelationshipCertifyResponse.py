#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenAuthUserauthRelationshipCertifyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenAuthUserauthRelationshipCertifyResponse, self).__init__()
        self._effective = None

    @property
    def effective(self):
        return self._effective

    @effective.setter
    def effective(self, value):
        self._effective = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenAuthUserauthRelationshipCertifyResponse, self).parse_response_content(response_content)
        if 'effective' in response:
            self.effective = response['effective']
