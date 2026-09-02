#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.PreconsultResult import PreconsultResult


class AlipayCommerceAcommunicationCreditphonePreconsultQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceAcommunicationCreditphonePreconsultQueryResponse, self).__init__()
        self._consult_status = None
        self._preconsult_result_list = None
        self._request_no = None

    @property
    def consult_status(self):
        return self._consult_status

    @consult_status.setter
    def consult_status(self, value):
        self._consult_status = value
    @property
    def preconsult_result_list(self):
        return self._preconsult_result_list

    @preconsult_result_list.setter
    def preconsult_result_list(self, value):
        if isinstance(value, list):
            self._preconsult_result_list = list()
            for i in value:
                if isinstance(i, PreconsultResult):
                    self._preconsult_result_list.append(i)
                else:
                    self._preconsult_result_list.append(PreconsultResult.from_alipay_dict(i))
    @property
    def request_no(self):
        return self._request_no

    @request_no.setter
    def request_no(self, value):
        self._request_no = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceAcommunicationCreditphonePreconsultQueryResponse, self).parse_response_content(response_content)
        if 'consult_status' in response:
            self.consult_status = response['consult_status']
        if 'preconsult_result_list' in response:
            self.preconsult_result_list = response['preconsult_result_list']
        if 'request_no' in response:
            self.request_no = response['request_no']
