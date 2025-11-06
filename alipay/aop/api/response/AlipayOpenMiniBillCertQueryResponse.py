#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.CertBillDetail import CertBillDetail


class AlipayOpenMiniBillCertQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenMiniBillCertQueryResponse, self).__init__()
        self._response = None

    @property
    def response(self):
        return self._response

    @response.setter
    def response(self, value):
        if isinstance(value, list):
            self._response = list()
            for i in value:
                if isinstance(i, CertBillDetail):
                    self._response.append(i)
                else:
                    self._response.append(CertBillDetail.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayOpenMiniBillCertQueryResponse, self).parse_response_content(response_content)
        if 'response' in response:
            self.response = response['response']
