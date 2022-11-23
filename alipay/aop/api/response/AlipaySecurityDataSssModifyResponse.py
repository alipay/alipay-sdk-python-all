#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ActivityGoods import ActivityGoods


class AlipaySecurityDataSssModifyResponse(AlipayResponse):

    def __init__(self):
        super(AlipaySecurityDataSssModifyResponse, self).__init__()
        self._dff = None
        self._kjkj = None

    @property
    def dff(self):
        return self._dff

    @dff.setter
    def dff(self, value):
        if isinstance(value, ActivityGoods):
            self._dff = value
        else:
            self._dff = ActivityGoods.from_alipay_dict(value)
    @property
    def kjkj(self):
        return self._kjkj

    @kjkj.setter
    def kjkj(self, value):
        self._kjkj = value

    def parse_response_content(self, response_content):
        response = super(AlipaySecurityDataSssModifyResponse, self).parse_response_content(response_content)
        if 'dff' in response:
            self.dff = response['dff']
        if 'kjkj' in response:
            self.kjkj = response['kjkj']
