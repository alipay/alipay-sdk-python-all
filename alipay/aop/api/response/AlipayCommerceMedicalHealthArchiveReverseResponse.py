#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ReverseResultList import ReverseResultList


class AlipayCommerceMedicalHealthArchiveReverseResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalHealthArchiveReverseResponse, self).__init__()
        self._is_success = None
        self._result_code = None
        self._result_details = None

    @property
    def is_success(self):
        return self._is_success

    @is_success.setter
    def is_success(self, value):
        self._is_success = value
    @property
    def result_code(self):
        return self._result_code

    @result_code.setter
    def result_code(self, value):
        self._result_code = value
    @property
    def result_details(self):
        return self._result_details

    @result_details.setter
    def result_details(self, value):
        if isinstance(value, list):
            self._result_details = list()
            for i in value:
                if isinstance(i, ReverseResultList):
                    self._result_details.append(i)
                else:
                    self._result_details.append(ReverseResultList.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalHealthArchiveReverseResponse, self).parse_response_content(response_content)
        if 'is_success' in response:
            self.is_success = response['is_success']
        if 'result_code' in response:
            self.result_code = response['result_code']
        if 'result_details' in response:
            self.result_details = response['result_details']
