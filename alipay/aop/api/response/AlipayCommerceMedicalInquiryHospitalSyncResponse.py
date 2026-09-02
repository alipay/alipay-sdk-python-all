#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceMedicalInquiryHospitalSyncResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalInquiryHospitalSyncResponse, self).__init__()
        self._original_record_id = None

    @property
    def original_record_id(self):
        return self._original_record_id

    @original_record_id.setter
    def original_record_id(self, value):
        self._original_record_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalInquiryHospitalSyncResponse, self).parse_response_content(response_content)
        if 'original_record_id' in response:
            self.original_record_id = response['original_record_id']
