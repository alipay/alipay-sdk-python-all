#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenMiniIsvFastregisterCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenMiniIsvFastregisterCreateResponse, self).__init__()
        self._authorize_url = None
        self._order_no = None

    @property
    def authorize_url(self):
        return self._authorize_url

    @authorize_url.setter
    def authorize_url(self, value):
        self._authorize_url = value
    @property
    def order_no(self):
        return self._order_no

    @order_no.setter
    def order_no(self, value):
        self._order_no = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenMiniIsvFastregisterCreateResponse, self).parse_response_content(response_content)
        if 'authorize_url' in response:
            self.authorize_url = response['authorize_url']
        if 'order_no' in response:
            self.order_no = response['order_no']
