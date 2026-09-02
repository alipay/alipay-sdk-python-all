#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCloudCloudbaseResourcepackageOpenCreateandpayResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCloudCloudbaseResourcepackageOpenCreateandpayResponse, self).__init__()
        self._env_id = None
        self._order_no = None

    @property
    def env_id(self):
        return self._env_id

    @env_id.setter
    def env_id(self, value):
        self._env_id = value
    @property
    def order_no(self):
        return self._order_no

    @order_no.setter
    def order_no(self, value):
        self._order_no = value

    def parse_response_content(self, response_content):
        response = super(AlipayCloudCloudbaseResourcepackageOpenCreateandpayResponse, self).parse_response_content(response_content)
        if 'env_id' in response:
            self.env_id = response['env_id']
        if 'order_no' in response:
            self.order_no = response['order_no']
