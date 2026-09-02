#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayTradeSaasInvoiceDownloadResponse(AlipayResponse):

    def __init__(self):
        super(AlipayTradeSaasInvoiceDownloadResponse, self).__init__()
        self._download_url = None
        self._expire_time = None
        self._file_name = None
        self._file_sha_256 = None
        self._file_size = None
        self._file_type = None
        self._saas_invoice_order_no = None

    @property
    def download_url(self):
        return self._download_url

    @download_url.setter
    def download_url(self, value):
        self._download_url = value
    @property
    def expire_time(self):
        return self._expire_time

    @expire_time.setter
    def expire_time(self, value):
        self._expire_time = value
    @property
    def file_name(self):
        return self._file_name

    @file_name.setter
    def file_name(self, value):
        self._file_name = value
    @property
    def file_sha_256(self):
        return self._file_sha_256

    @file_sha_256.setter
    def file_sha_256(self, value):
        self._file_sha_256 = value
    @property
    def file_size(self):
        return self._file_size

    @file_size.setter
    def file_size(self, value):
        self._file_size = value
    @property
    def file_type(self):
        return self._file_type

    @file_type.setter
    def file_type(self, value):
        self._file_type = value
    @property
    def saas_invoice_order_no(self):
        return self._saas_invoice_order_no

    @saas_invoice_order_no.setter
    def saas_invoice_order_no(self, value):
        self._saas_invoice_order_no = value

    def parse_response_content(self, response_content):
        response = super(AlipayTradeSaasInvoiceDownloadResponse, self).parse_response_content(response_content)
        if 'download_url' in response:
            self.download_url = response['download_url']
        if 'expire_time' in response:
            self.expire_time = response['expire_time']
        if 'file_name' in response:
            self.file_name = response['file_name']
        if 'file_sha_256' in response:
            self.file_sha_256 = response['file_sha_256']
        if 'file_size' in response:
            self.file_size = response['file_size']
        if 'file_type' in response:
            self.file_type = response['file_type']
        if 'saas_invoice_order_no' in response:
            self.saas_invoice_order_no = response['saas_invoice_order_no']
