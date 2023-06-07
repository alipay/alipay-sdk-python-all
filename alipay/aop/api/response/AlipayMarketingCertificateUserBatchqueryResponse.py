#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.CertificateQueryInfo import CertificateQueryInfo


class AlipayMarketingCertificateUserBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMarketingCertificateUserBatchqueryResponse, self).__init__()
        self._certificate_info_list = None
        self._page_num = None
        self._page_size = None
        self._total_size = None

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
    def page_num(self):
        return self._page_num

    @page_num.setter
    def page_num(self, value):
        self._page_num = value
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

    def parse_response_content(self, response_content):
        response = super(AlipayMarketingCertificateUserBatchqueryResponse, self).parse_response_content(response_content)
        if 'certificate_info_list' in response:
            self.certificate_info_list = response['certificate_info_list']
        if 'page_num' in response:
            self.page_num = response['page_num']
        if 'page_size' in response:
            self.page_size = response['page_size']
        if 'total_size' in response:
            self.total_size = response['total_size']
