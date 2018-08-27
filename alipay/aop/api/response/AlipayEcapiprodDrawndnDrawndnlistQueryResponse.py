#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.DrawndnVo import DrawndnVo


class AlipayEcapiprodDrawndnDrawndnlistQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEcapiprodDrawndnDrawndnlistQueryResponse, self).__init__()
        self._drawndn_list = None
        self._request_id = None

    @property
    def drawndn_list(self):
        return self._drawndn_list

    @drawndn_list.setter
    def drawndn_list(self, value):
        if isinstance(value, list):
            self._drawndn_list = list()
            for i in value:
                if isinstance(i, DrawndnVo):
                    self._drawndn_list.append(i)
                else:
                    self._drawndn_list.append(DrawndnVo.from_alipay_dict(i))
    @property
    def request_id(self):
        return self._request_id

    @request_id.setter
    def request_id(self, value):
        self._request_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayEcapiprodDrawndnDrawndnlistQueryResponse, self).parse_response_content(response_content)
        if 'drawndn_list' in response:
            self.drawndn_list = response['drawndn_list']
        if 'request_id' in response:
            self.request_id = response['request_id']
