#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class KoubeiServindustryPortfolioDataCreateResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiServindustryPortfolioDataCreateResponse, self).__init__()
        self._portfolio_id = None

    @property
    def portfolio_id(self):
        return self._portfolio_id

    @portfolio_id.setter
    def portfolio_id(self, value):
        self._portfolio_id = value

    def parse_response_content(self, response_content):
        response = super(KoubeiServindustryPortfolioDataCreateResponse, self).parse_response_content(response_content)
        if 'portfolio_id' in response:
            self.portfolio_id = response['portfolio_id']
