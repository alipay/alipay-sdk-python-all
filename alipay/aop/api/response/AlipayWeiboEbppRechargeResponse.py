#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayWeiboEbppRechargeResponse(AlipayResponse):

    def __init__(self):
        super(AlipayWeiboEbppRechargeResponse, self).__init__()
        self._partnerpuccharge = None

    @property
    def partnerpuccharge(self):
        return self._partnerpuccharge

    @partnerpuccharge.setter
    def partnerpuccharge(self, value):
        self._partnerpuccharge = value

    def parse_response_content(self, response_content):
        response = super(AlipayWeiboEbppRechargeResponse, self).parse_response_content(response_content)
        if 'partnerpuccharge' in response:
            self.partnerpuccharge = response['partnerpuccharge']
