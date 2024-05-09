#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenMiniOrderAftersaleCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenMiniOrderAftersaleCreateResponse, self).__init__()
        self._aftersale_id = None
        self._out_aftersale_id = None

    @property
    def aftersale_id(self):
        return self._aftersale_id

    @aftersale_id.setter
    def aftersale_id(self, value):
        self._aftersale_id = value
    @property
    def out_aftersale_id(self):
        return self._out_aftersale_id

    @out_aftersale_id.setter
    def out_aftersale_id(self, value):
        self._out_aftersale_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenMiniOrderAftersaleCreateResponse, self).parse_response_content(response_content)
        if 'aftersale_id' in response:
            self.aftersale_id = response['aftersale_id']
        if 'out_aftersale_id' in response:
            self.out_aftersale_id = response['out_aftersale_id']
