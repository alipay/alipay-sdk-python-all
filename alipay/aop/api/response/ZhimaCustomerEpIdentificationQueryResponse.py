#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class ZhimaCustomerEpIdentificationQueryResponse(AlipayResponse):

    def __init__(self):
        super(ZhimaCustomerEpIdentificationQueryResponse, self).__init__()
        self._ep_cert_no = None
        self._ep_name = None
        self._failed_code = None
        self._passed = None

    @property
    def ep_cert_no(self):
        return self._ep_cert_no

    @ep_cert_no.setter
    def ep_cert_no(self, value):
        self._ep_cert_no = value
    @property
    def ep_name(self):
        return self._ep_name

    @ep_name.setter
    def ep_name(self, value):
        self._ep_name = value
    @property
    def failed_code(self):
        return self._failed_code

    @failed_code.setter
    def failed_code(self, value):
        self._failed_code = value
    @property
    def passed(self):
        return self._passed

    @passed.setter
    def passed(self, value):
        self._passed = value

    def parse_response_content(self, response_content):
        response = super(ZhimaCustomerEpIdentificationQueryResponse, self).parse_response_content(response_content)
        if 'ep_cert_no' in response:
            self.ep_cert_no = response['ep_cert_no']
        if 'ep_name' in response:
            self.ep_name = response['ep_name']
        if 'failed_code' in response:
            self.failed_code = response['failed_code']
        if 'passed' in response:
            self.passed = response['passed']
