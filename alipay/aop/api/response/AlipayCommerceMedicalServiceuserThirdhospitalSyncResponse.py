#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceMedicalServiceuserThirdhospitalSyncResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalServiceuserThirdhospitalSyncResponse, self).__init__()
        self._health_doc_id = None

    @property
    def health_doc_id(self):
        return self._health_doc_id

    @health_doc_id.setter
    def health_doc_id(self, value):
        self._health_doc_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalServiceuserThirdhospitalSyncResponse, self).parse_response_content(response_content)
        if 'health_doc_id' in response:
            self.health_doc_id = response['health_doc_id']
