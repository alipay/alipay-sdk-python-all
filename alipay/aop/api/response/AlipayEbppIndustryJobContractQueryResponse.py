#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayEbppIndustryJobContractQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEbppIndustryJobContractQueryResponse, self).__init__()
        self._contract_status = None
        self._download_url = None
        self._sign_url = None
        self._tx_hash = None

    @property
    def contract_status(self):
        return self._contract_status

    @contract_status.setter
    def contract_status(self, value):
        self._contract_status = value
    @property
    def download_url(self):
        return self._download_url

    @download_url.setter
    def download_url(self, value):
        self._download_url = value
    @property
    def sign_url(self):
        return self._sign_url

    @sign_url.setter
    def sign_url(self, value):
        self._sign_url = value
    @property
    def tx_hash(self):
        return self._tx_hash

    @tx_hash.setter
    def tx_hash(self, value):
        self._tx_hash = value

    def parse_response_content(self, response_content):
        response = super(AlipayEbppIndustryJobContractQueryResponse, self).parse_response_content(response_content)
        if 'contract_status' in response:
            self.contract_status = response['contract_status']
        if 'download_url' in response:
            self.download_url = response['download_url']
        if 'sign_url' in response:
            self.sign_url = response['sign_url']
        if 'tx_hash' in response:
            self.tx_hash = response['tx_hash']
