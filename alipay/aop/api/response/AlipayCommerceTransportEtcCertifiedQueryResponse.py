#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.EtcAuthResult import EtcAuthResult


class AlipayCommerceTransportEtcCertifiedQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceTransportEtcCertifiedQueryResponse, self).__init__()
        self._etc_certified_result = None

    @property
    def etc_certified_result(self):
        return self._etc_certified_result

    @etc_certified_result.setter
    def etc_certified_result(self, value):
        if isinstance(value, EtcAuthResult):
            self._etc_certified_result = value
        else:
            self._etc_certified_result = EtcAuthResult.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceTransportEtcCertifiedQueryResponse, self).parse_response_content(response_content)
        if 'etc_certified_result' in response:
            self.etc_certified_result = response['etc_certified_result']
