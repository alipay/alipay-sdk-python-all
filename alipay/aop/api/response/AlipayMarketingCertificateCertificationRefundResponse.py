#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.CertificateReverseResult import CertificateReverseResult


class AlipayMarketingCertificateCertificationRefundResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMarketingCertificateCertificationRefundResponse, self).__init__()
        self._certificate_reverse_result_list = None

    @property
    def certificate_reverse_result_list(self):
        return self._certificate_reverse_result_list

    @certificate_reverse_result_list.setter
    def certificate_reverse_result_list(self, value):
        if isinstance(value, list):
            self._certificate_reverse_result_list = list()
            for i in value:
                if isinstance(i, CertificateReverseResult):
                    self._certificate_reverse_result_list.append(i)
                else:
                    self._certificate_reverse_result_list.append(CertificateReverseResult.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayMarketingCertificateCertificationRefundResponse, self).parse_response_content(response_content)
        if 'certificate_reverse_result_list' in response:
            self.certificate_reverse_result_list = response['certificate_reverse_result_list']
