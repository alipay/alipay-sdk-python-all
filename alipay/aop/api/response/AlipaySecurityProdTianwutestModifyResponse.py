#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipaySecurityProdTianwutestModifyResponse(AlipayResponse):

    def __init__(self):
        super(AlipaySecurityProdTianwutestModifyResponse, self).__init__()
        self._ceshi = None

    @property
    def ceshi(self):
        return self._ceshi

    @ceshi.setter
    def ceshi(self, value):
        self._ceshi = value

    def parse_response_content(self, response_content):
        response = super(AlipaySecurityProdTianwutestModifyResponse, self).parse_response_content(response_content)
        if 'ceshi' in response:
            self.ceshi = response['ceshi']
