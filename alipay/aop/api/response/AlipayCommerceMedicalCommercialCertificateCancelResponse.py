#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.MemberCardCertificateDetail import MemberCardCertificateDetail


class AlipayCommerceMedicalCommercialCertificateCancelResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalCommercialCertificateCancelResponse, self).__init__()
        self._cancel_result = None
        self._certificate_detail = None

    @property
    def cancel_result(self):
        return self._cancel_result

    @cancel_result.setter
    def cancel_result(self, value):
        self._cancel_result = value
    @property
    def certificate_detail(self):
        return self._certificate_detail

    @certificate_detail.setter
    def certificate_detail(self, value):
        if isinstance(value, MemberCardCertificateDetail):
            self._certificate_detail = value
        else:
            self._certificate_detail = MemberCardCertificateDetail.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalCommercialCertificateCancelResponse, self).parse_response_content(response_content)
        if 'cancel_result' in response:
            self.cancel_result = response['cancel_result']
        if 'certificate_detail' in response:
            self.certificate_detail = response['certificate_detail']
