#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayPcreditCreditriskCustlabelQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayPcreditCreditriskCustlabelQueryResponse, self).__init__()
        self._show_jb = None
        self._show_my = None

    @property
    def show_jb(self):
        return self._show_jb

    @show_jb.setter
    def show_jb(self, value):
        self._show_jb = value
    @property
    def show_my(self):
        return self._show_my

    @show_my.setter
    def show_my(self, value):
        self._show_my = value

    def parse_response_content(self, response_content):
        response = super(AlipayPcreditCreditriskCustlabelQueryResponse, self).parse_response_content(response_content)
        if 'show_jb' in response:
            self.show_jb = response['show_jb']
        if 'show_my' in response:
            self.show_my = response['show_my']
