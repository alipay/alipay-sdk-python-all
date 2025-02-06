#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayEbppIndustrySalaryReconQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEbppIndustrySalaryReconQueryResponse, self).__init__()
        self._date = None
        self._download_url = None
        self._out_trade_no = None
        self._sign_xml = None
        self._type = None

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, value):
        self._date = value
    @property
    def download_url(self):
        return self._download_url

    @download_url.setter
    def download_url(self, value):
        self._download_url = value
    @property
    def out_trade_no(self):
        return self._out_trade_no

    @out_trade_no.setter
    def out_trade_no(self, value):
        self._out_trade_no = value
    @property
    def sign_xml(self):
        return self._sign_xml

    @sign_xml.setter
    def sign_xml(self, value):
        self._sign_xml = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value

    def parse_response_content(self, response_content):
        response = super(AlipayEbppIndustrySalaryReconQueryResponse, self).parse_response_content(response_content)
        if 'date' in response:
            self.date = response['date']
        if 'download_url' in response:
            self.download_url = response['download_url']
        if 'out_trade_no' in response:
            self.out_trade_no = response['out_trade_no']
        if 'sign_xml' in response:
            self.sign_xml = response['sign_xml']
        if 'type' in response:
            self.type = response['type']
