#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenMiniMarketMemberQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenMiniMarketMemberQueryResponse, self).__init__()
        self._membership_redirect_url = None

    @property
    def membership_redirect_url(self):
        return self._membership_redirect_url

    @membership_redirect_url.setter
    def membership_redirect_url(self, value):
        self._membership_redirect_url = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenMiniMarketMemberQueryResponse, self).parse_response_content(response_content)
        if 'membership_redirect_url' in response:
            self.membership_redirect_url = response['membership_redirect_url']
