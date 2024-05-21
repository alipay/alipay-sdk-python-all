#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.CertificateQueryInfo import CertificateQueryInfo


class AlipayMarketingCertificateCertificatetionSendcallbackResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMarketingCertificateCertificatetionSendcallbackResponse, self).__init__()
        self._certificate_info_list = None
        self._order_id = None

    @property
    def certificate_info_list(self):
        return self._certificate_info_list

    @certificate_info_list.setter
    def certificate_info_list(self, value):
        if isinstance(value, list):
            self._certificate_info_list = list()
            for i in value:
                if isinstance(i, CertificateQueryInfo):
                    self._certificate_info_list.append(i)
                else:
                    self._certificate_info_list.append(CertificateQueryInfo.from_alipay_dict(i))
    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        self._order_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayMarketingCertificateCertificatetionSendcallbackResponse, self).parse_response_content(response_content)
        if 'certificate_info_list' in response:
            self.certificate_info_list = response['certificate_info_list']
        if 'order_id' in response:
            self.order_id = response['order_id']
