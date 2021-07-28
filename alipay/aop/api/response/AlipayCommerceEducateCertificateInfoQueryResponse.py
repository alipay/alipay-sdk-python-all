#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.StudentCertificate import StudentCertificate


class AlipayCommerceEducateCertificateInfoQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceEducateCertificateInfoQueryResponse, self).__init__()
        self._certificates = None

    @property
    def certificates(self):
        return self._certificates

    @certificates.setter
    def certificates(self, value):
        if isinstance(value, list):
            self._certificates = list()
            for i in value:
                if isinstance(i, StudentCertificate):
                    self._certificates.append(i)
                else:
                    self._certificates.append(StudentCertificate.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceEducateCertificateInfoQueryResponse, self).parse_response_content(response_content)
        if 'certificates' in response:
            self.certificates = response['certificates']
