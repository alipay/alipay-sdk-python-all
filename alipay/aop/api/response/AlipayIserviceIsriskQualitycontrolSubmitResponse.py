#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayIserviceIsriskQualitycontrolSubmitResponse(AlipayResponse):

    def __init__(self):
        super(AlipayIserviceIsriskQualitycontrolSubmitResponse, self).__init__()
        self._qc_detect_result_id = None
        self._qc_message = None
        self._qc_result = None

    @property
    def qc_detect_result_id(self):
        return self._qc_detect_result_id

    @qc_detect_result_id.setter
    def qc_detect_result_id(self, value):
        self._qc_detect_result_id = value
    @property
    def qc_message(self):
        return self._qc_message

    @qc_message.setter
    def qc_message(self, value):
        self._qc_message = value
    @property
    def qc_result(self):
        return self._qc_result

    @qc_result.setter
    def qc_result(self, value):
        self._qc_result = value

    def parse_response_content(self, response_content):
        response = super(AlipayIserviceIsriskQualitycontrolSubmitResponse, self).parse_response_content(response_content)
        if 'qc_detect_result_id' in response:
            self.qc_detect_result_id = response['qc_detect_result_id']
        if 'qc_message' in response:
            self.qc_message = response['qc_message']
        if 'qc_result' in response:
            self.qc_result = response['qc_result']
