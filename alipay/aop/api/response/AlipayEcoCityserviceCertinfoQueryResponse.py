#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.CertInfoResponse import CertInfoResponse


class AlipayEcoCityserviceCertinfoQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEcoCityserviceCertinfoQueryResponse, self).__init__()
        self._result_list = None

    @property
    def result_list(self):
        return self._result_list

    @result_list.setter
    def result_list(self, value):
        if isinstance(value, list):
            self._result_list = list()
            for i in value:
                if isinstance(i, CertInfoResponse):
                    self._result_list.append(i)
                else:
                    self._result_list.append(CertInfoResponse.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayEcoCityserviceCertinfoQueryResponse, self).parse_response_content(response_content)
        if 'result_list' in response:
            self.result_list = response['result_list']
