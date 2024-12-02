#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceMedicalIndustrydataPrescriptionSyncResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalIndustrydataPrescriptionSyncResponse, self).__init__()
        self._alipay_prescription_id = None

    @property
    def alipay_prescription_id(self):
        return self._alipay_prescription_id

    @alipay_prescription_id.setter
    def alipay_prescription_id(self, value):
        self._alipay_prescription_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalIndustrydataPrescriptionSyncResponse, self).parse_response_content(response_content)
        if 'alipay_prescription_id' in response:
            self.alipay_prescription_id = response['alipay_prescription_id']
