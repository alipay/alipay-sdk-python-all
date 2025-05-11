#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceMedicalHealthcaPharmorprscrsignQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalHealthcaPharmorprscrsignQueryResponse, self).__init__()
        self._sign_name_file_id = None
        self._sign_pdf_file_id = None
        self._sign_pdf_url = None
        self._sign_status = None

    @property
    def sign_name_file_id(self):
        return self._sign_name_file_id

    @sign_name_file_id.setter
    def sign_name_file_id(self, value):
        self._sign_name_file_id = value
    @property
    def sign_pdf_file_id(self):
        return self._sign_pdf_file_id

    @sign_pdf_file_id.setter
    def sign_pdf_file_id(self, value):
        self._sign_pdf_file_id = value
    @property
    def sign_pdf_url(self):
        return self._sign_pdf_url

    @sign_pdf_url.setter
    def sign_pdf_url(self, value):
        self._sign_pdf_url = value
    @property
    def sign_status(self):
        return self._sign_status

    @sign_status.setter
    def sign_status(self, value):
        self._sign_status = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalHealthcaPharmorprscrsignQueryResponse, self).parse_response_content(response_content)
        if 'sign_name_file_id' in response:
            self.sign_name_file_id = response['sign_name_file_id']
        if 'sign_pdf_file_id' in response:
            self.sign_pdf_file_id = response['sign_pdf_file_id']
        if 'sign_pdf_url' in response:
            self.sign_pdf_url = response['sign_pdf_url']
        if 'sign_status' in response:
            self.sign_status = response['sign_status']
