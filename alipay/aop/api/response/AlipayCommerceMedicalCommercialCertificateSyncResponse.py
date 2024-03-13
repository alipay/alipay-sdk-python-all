#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.MemberCardCertificateDetail import MemberCardCertificateDetail


class AlipayCommerceMedicalCommercialCertificateSyncResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalCommercialCertificateSyncResponse, self).__init__()
        self._certificate_detail = None
        self._sync_result = None

    @property
    def certificate_detail(self):
        return self._certificate_detail

    @certificate_detail.setter
    def certificate_detail(self, value):
        if isinstance(value, MemberCardCertificateDetail):
            self._certificate_detail = value
        else:
            self._certificate_detail = MemberCardCertificateDetail.from_alipay_dict(value)
    @property
    def sync_result(self):
        return self._sync_result

    @sync_result.setter
    def sync_result(self, value):
        self._sync_result = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalCommercialCertificateSyncResponse, self).parse_response_content(response_content)
        if 'certificate_detail' in response:
            self.certificate_detail = response['certificate_detail']
        if 'sync_result' in response:
            self.sync_result = response['sync_result']
