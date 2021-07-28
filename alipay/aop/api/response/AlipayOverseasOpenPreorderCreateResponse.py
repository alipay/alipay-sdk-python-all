#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.TuitionISVResult import TuitionISVResult


class AlipayOverseasOpenPreorderCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOverseasOpenPreorderCreateResponse, self).__init__()
        self._pre_order_id = None
        self._pre_order_link = None
        self._result = None

    @property
    def pre_order_id(self):
        return self._pre_order_id

    @pre_order_id.setter
    def pre_order_id(self, value):
        self._pre_order_id = value
    @property
    def pre_order_link(self):
        return self._pre_order_link

    @pre_order_link.setter
    def pre_order_link(self, value):
        self._pre_order_link = value
    @property
    def result(self):
        return self._result

    @result.setter
    def result(self, value):
        if isinstance(value, TuitionISVResult):
            self._result = value
        else:
            self._result = TuitionISVResult.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayOverseasOpenPreorderCreateResponse, self).parse_response_content(response_content)
        if 'pre_order_id' in response:
            self.pre_order_id = response['pre_order_id']
        if 'pre_order_link' in response:
            self.pre_order_link = response['pre_order_link']
        if 'result' in response:
            self.result = response['result']
