#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.CertAvailableNumVO import CertAvailableNumVO


class AlipayMarketingToolCertNumQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMarketingToolCertNumQueryResponse, self).__init__()
        self._cert_available_num = None

    @property
    def cert_available_num(self):
        return self._cert_available_num

    @cert_available_num.setter
    def cert_available_num(self, value):
        if isinstance(value, list):
            self._cert_available_num = list()
            for i in value:
                if isinstance(i, CertAvailableNumVO):
                    self._cert_available_num.append(i)
                else:
                    self._cert_available_num.append(CertAvailableNumVO.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayMarketingToolCertNumQueryResponse, self).parse_response_content(response_content)
        if 'cert_available_num' in response:
            self.cert_available_num = response['cert_available_num']
