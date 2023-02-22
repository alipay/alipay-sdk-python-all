#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayFinancialnetAuthYepModelConsultResponse(AlipayResponse):

    def __init__(self):
        super(AlipayFinancialnetAuthYepModelConsultResponse, self).__init__()
        self._biz_model = None
        self._redirect_url = None

    @property
    def biz_model(self):
        return self._biz_model

    @biz_model.setter
    def biz_model(self, value):
        self._biz_model = value
    @property
    def redirect_url(self):
        return self._redirect_url

    @redirect_url.setter
    def redirect_url(self, value):
        self._redirect_url = value

    def parse_response_content(self, response_content):
        response = super(AlipayFinancialnetAuthYepModelConsultResponse, self).parse_response_content(response_content)
        if 'biz_model' in response:
            self.biz_model = response['biz_model']
        if 'redirect_url' in response:
            self.redirect_url = response['redirect_url']
