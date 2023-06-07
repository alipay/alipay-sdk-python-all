#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.CertificateUseResult import CertificateUseResult


class AlipayMarketingCertificateCertificationUseResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMarketingCertificateCertificationUseResponse, self).__init__()
        self._certificate_use_result_list = None

    @property
    def certificate_use_result_list(self):
        return self._certificate_use_result_list

    @certificate_use_result_list.setter
    def certificate_use_result_list(self, value):
        if isinstance(value, list):
            self._certificate_use_result_list = list()
            for i in value:
                if isinstance(i, CertificateUseResult):
                    self._certificate_use_result_list.append(i)
                else:
                    self._certificate_use_result_list.append(CertificateUseResult.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayMarketingCertificateCertificationUseResponse, self).parse_response_content(response_content)
        if 'certificate_use_result_list' in response:
            self.certificate_use_result_list = response['certificate_use_result_list']
