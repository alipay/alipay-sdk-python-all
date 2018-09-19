#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class KoubeiServindustryShopLicenseQueryResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiServindustryShopLicenseQueryResponse, self).__init__()
        self._have_permit = None

    @property
    def have_permit(self):
        return self._have_permit

    @have_permit.setter
    def have_permit(self, value):
        self._have_permit = value

    def parse_response_content(self, response_content):
        response = super(KoubeiServindustryShopLicenseQueryResponse, self).parse_response_content(response_content)
        if 'have_permit' in response:
            self.have_permit = response['have_permit']
