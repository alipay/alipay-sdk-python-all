#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayEbppIndustrySalaryElectronicreceiptQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEbppIndustrySalaryElectronicreceiptQueryResponse, self).__init__()
        self._merchant_id = None
        self._out_trade_no = None
        self._pdf_download_url = None
        self._receipt_no = None
        self._sign_xml = None
        self._status = None

    @property
    def merchant_id(self):
        return self._merchant_id

    @merchant_id.setter
    def merchant_id(self, value):
        self._merchant_id = value
    @property
    def out_trade_no(self):
        return self._out_trade_no

    @out_trade_no.setter
    def out_trade_no(self, value):
        self._out_trade_no = value
    @property
    def pdf_download_url(self):
        return self._pdf_download_url

    @pdf_download_url.setter
    def pdf_download_url(self, value):
        self._pdf_download_url = value
    @property
    def receipt_no(self):
        return self._receipt_no

    @receipt_no.setter
    def receipt_no(self, value):
        self._receipt_no = value
    @property
    def sign_xml(self):
        return self._sign_xml

    @sign_xml.setter
    def sign_xml(self, value):
        self._sign_xml = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value

    def parse_response_content(self, response_content):
        response = super(AlipayEbppIndustrySalaryElectronicreceiptQueryResponse, self).parse_response_content(response_content)
        if 'merchant_id' in response:
            self.merchant_id = response['merchant_id']
        if 'out_trade_no' in response:
            self.out_trade_no = response['out_trade_no']
        if 'pdf_download_url' in response:
            self.pdf_download_url = response['pdf_download_url']
        if 'receipt_no' in response:
            self.receipt_no = response['receipt_no']
        if 'sign_xml' in response:
            self.sign_xml = response['sign_xml']
        if 'status' in response:
            self.status = response['status']
