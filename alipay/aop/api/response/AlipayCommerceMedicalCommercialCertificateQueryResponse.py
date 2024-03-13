#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.MemberCardCertificateDetail import MemberCardCertificateDetail


class AlipayCommerceMedicalCommercialCertificateQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalCommercialCertificateQueryResponse, self).__init__()
        self._certificate_details = None
        self._total = None

    @property
    def certificate_details(self):
        return self._certificate_details

    @certificate_details.setter
    def certificate_details(self, value):
        if isinstance(value, list):
            self._certificate_details = list()
            for i in value:
                if isinstance(i, MemberCardCertificateDetail):
                    self._certificate_details.append(i)
                else:
                    self._certificate_details.append(MemberCardCertificateDetail.from_alipay_dict(i))
    @property
    def total(self):
        return self._total

    @total.setter
    def total(self, value):
        self._total = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalCommercialCertificateQueryResponse, self).parse_response_content(response_content)
        if 'certificate_details' in response:
            self.certificate_details = response['certificate_details']
        if 'total' in response:
            self.total = response['total']
