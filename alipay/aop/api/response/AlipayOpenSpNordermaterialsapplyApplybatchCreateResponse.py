#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenSpNordermaterialsapplyApplybatchCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenSpNordermaterialsapplyApplybatchCreateResponse, self).__init__()
        self._combined_order_no = None

    @property
    def combined_order_no(self):
        return self._combined_order_no

    @combined_order_no.setter
    def combined_order_no(self, value):
        self._combined_order_no = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenSpNordermaterialsapplyApplybatchCreateResponse, self).parse_response_content(response_content)
        if 'combined_order_no' in response:
            self.combined_order_no = response['combined_order_no']
