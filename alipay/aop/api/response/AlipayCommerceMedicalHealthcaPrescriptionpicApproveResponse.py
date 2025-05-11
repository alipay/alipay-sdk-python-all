#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceMedicalHealthcaPrescriptionpicApproveResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalHealthcaPrescriptionpicApproveResponse, self).__init__()
        self._sign_pic_file_id = None
        self._sign_pic_url = None

    @property
    def sign_pic_file_id(self):
        return self._sign_pic_file_id

    @sign_pic_file_id.setter
    def sign_pic_file_id(self, value):
        self._sign_pic_file_id = value
    @property
    def sign_pic_url(self):
        return self._sign_pic_url

    @sign_pic_url.setter
    def sign_pic_url(self, value):
        self._sign_pic_url = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalHealthcaPrescriptionpicApproveResponse, self).parse_response_content(response_content)
        if 'sign_pic_file_id' in response:
            self.sign_pic_file_id = response['sign_pic_file_id']
        if 'sign_pic_url' in response:
            self.sign_pic_url = response['sign_pic_url']
