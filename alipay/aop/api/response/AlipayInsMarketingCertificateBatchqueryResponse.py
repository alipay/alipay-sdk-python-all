#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.InsCertificatePaginationList import InsCertificatePaginationList


class AlipayInsMarketingCertificateBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayInsMarketingCertificateBatchqueryResponse, self).__init__()
        self._ins_certificate_pagination_list = None

    @property
    def ins_certificate_pagination_list(self):
        return self._ins_certificate_pagination_list

    @ins_certificate_pagination_list.setter
    def ins_certificate_pagination_list(self, value):
        if isinstance(value, InsCertificatePaginationList):
            self._ins_certificate_pagination_list = value
        else:
            self._ins_certificate_pagination_list = InsCertificatePaginationList.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayInsMarketingCertificateBatchqueryResponse, self).parse_response_content(response_content)
        if 'ins_certificate_pagination_list' in response:
            self.ins_certificate_pagination_list = response['ins_certificate_pagination_list']
