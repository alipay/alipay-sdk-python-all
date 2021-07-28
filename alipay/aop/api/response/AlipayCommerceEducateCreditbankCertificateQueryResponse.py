#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.CreditBankCertificateExperience import CreditBankCertificateExperience


class AlipayCommerceEducateCreditbankCertificateQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceEducateCreditbankCertificateQueryResponse, self).__init__()
        self._certificates = None

    @property
    def certificates(self):
        return self._certificates

    @certificates.setter
    def certificates(self, value):
        if isinstance(value, list):
            self._certificates = list()
            for i in value:
                if isinstance(i, CreditBankCertificateExperience):
                    self._certificates.append(i)
                else:
                    self._certificates.append(CreditBankCertificateExperience.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceEducateCreditbankCertificateQueryResponse, self).parse_response_content(response_content)
        if 'certificates' in response:
            self.certificates = response['certificates']
