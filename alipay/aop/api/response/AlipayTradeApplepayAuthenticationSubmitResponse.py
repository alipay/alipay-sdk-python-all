#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.OpenApiResponseHeader import OpenApiResponseHeader
from alipay.aop.api.domain.UpdatedAuthenticationDetails import UpdatedAuthenticationDetails


class AlipayTradeApplepayAuthenticationSubmitResponse(AlipayResponse):

    def __init__(self):
        super(AlipayTradeApplepayAuthenticationSubmitResponse, self).__init__()
        self._authentication_error = None
        self._fallback_authentication_mechanisms = None
        self._response_header = None
        self._retry_authentication_mechanisms = None
        self._signing_certificate = None
        self._updated_authentication_details = None
        self._updated_transaction_status = None

    @property
    def authentication_error(self):
        return self._authentication_error

    @authentication_error.setter
    def authentication_error(self, value):
        self._authentication_error = value
    @property
    def fallback_authentication_mechanisms(self):
        return self._fallback_authentication_mechanisms

    @fallback_authentication_mechanisms.setter
    def fallback_authentication_mechanisms(self, value):
        if isinstance(value, list):
            self._fallback_authentication_mechanisms = list()
            for i in value:
                self._fallback_authentication_mechanisms.append(i)
    @property
    def response_header(self):
        return self._response_header

    @response_header.setter
    def response_header(self, value):
        if isinstance(value, OpenApiResponseHeader):
            self._response_header = value
        else:
            self._response_header = OpenApiResponseHeader.from_alipay_dict(value)
    @property
    def retry_authentication_mechanisms(self):
        return self._retry_authentication_mechanisms

    @retry_authentication_mechanisms.setter
    def retry_authentication_mechanisms(self, value):
        if isinstance(value, list):
            self._retry_authentication_mechanisms = list()
            for i in value:
                self._retry_authentication_mechanisms.append(i)
    @property
    def signing_certificate(self):
        return self._signing_certificate

    @signing_certificate.setter
    def signing_certificate(self, value):
        self._signing_certificate = value
    @property
    def updated_authentication_details(self):
        return self._updated_authentication_details

    @updated_authentication_details.setter
    def updated_authentication_details(self, value):
        if isinstance(value, UpdatedAuthenticationDetails):
            self._updated_authentication_details = value
        else:
            self._updated_authentication_details = UpdatedAuthenticationDetails.from_alipay_dict(value)
    @property
    def updated_transaction_status(self):
        return self._updated_transaction_status

    @updated_transaction_status.setter
    def updated_transaction_status(self, value):
        self._updated_transaction_status = value

    def parse_response_content(self, response_content):
        response = super(AlipayTradeApplepayAuthenticationSubmitResponse, self).parse_response_content(response_content)
        if 'authentication_error' in response:
            self.authentication_error = response['authentication_error']
        if 'fallback_authentication_mechanisms' in response:
            self.fallback_authentication_mechanisms = response['fallback_authentication_mechanisms']
        if 'response_header' in response:
            self.response_header = response['response_header']
        if 'retry_authentication_mechanisms' in response:
            self.retry_authentication_mechanisms = response['retry_authentication_mechanisms']
        if 'signing_certificate' in response:
            self.signing_certificate = response['signing_certificate']
        if 'updated_authentication_details' in response:
            self.updated_authentication_details = response['updated_authentication_details']
        if 'updated_transaction_status' in response:
            self.updated_transaction_status = response['updated_transaction_status']
