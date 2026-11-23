#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.CertificateSimpleInfo import CertificateSimpleInfo
from alipay.aop.api.domain.UnavailableCertificate import UnavailableCertificate


class AlipayOpenSpNordercateringCertificatesQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenSpNordercateringCertificatesQueryResponse, self).__init__()
        self._certificate_list = None
        self._completion_status = None
        self._has_more = None
        self._page_no = None
        self._page_size = None
        self._total_size = None
        self._unavailable_certificates = None

    @property
    def certificate_list(self):
        return self._certificate_list

    @certificate_list.setter
    def certificate_list(self, value):
        if isinstance(value, list):
            self._certificate_list = list()
            for i in value:
                if isinstance(i, CertificateSimpleInfo):
                    self._certificate_list.append(i)
                else:
                    self._certificate_list.append(CertificateSimpleInfo.from_alipay_dict(i))
    @property
    def completion_status(self):
        return self._completion_status

    @completion_status.setter
    def completion_status(self, value):
        self._completion_status = value
    @property
    def has_more(self):
        return self._has_more

    @has_more.setter
    def has_more(self, value):
        self._has_more = value
    @property
    def page_no(self):
        return self._page_no

    @page_no.setter
    def page_no(self, value):
        self._page_no = value
    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, value):
        self._page_size = value
    @property
    def total_size(self):
        return self._total_size

    @total_size.setter
    def total_size(self, value):
        self._total_size = value
    @property
    def unavailable_certificates(self):
        return self._unavailable_certificates

    @unavailable_certificates.setter
    def unavailable_certificates(self, value):
        if isinstance(value, list):
            self._unavailable_certificates = list()
            for i in value:
                if isinstance(i, UnavailableCertificate):
                    self._unavailable_certificates.append(i)
                else:
                    self._unavailable_certificates.append(UnavailableCertificate.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayOpenSpNordercateringCertificatesQueryResponse, self).parse_response_content(response_content)
        if 'certificate_list' in response:
            self.certificate_list = response['certificate_list']
        if 'completion_status' in response:
            self.completion_status = response['completion_status']
        if 'has_more' in response:
            self.has_more = response['has_more']
        if 'page_no' in response:
            self.page_no = response['page_no']
        if 'page_size' in response:
            self.page_size = response['page_size']
        if 'total_size' in response:
            self.total_size = response['total_size']
        if 'unavailable_certificates' in response:
            self.unavailable_certificates = response['unavailable_certificates']
