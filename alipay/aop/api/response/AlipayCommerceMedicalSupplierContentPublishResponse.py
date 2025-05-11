#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceMedicalSupplierContentPublishResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalSupplierContentPublishResponse, self).__init__()
        self._med_content_id = None

    @property
    def med_content_id(self):
        return self._med_content_id

    @med_content_id.setter
    def med_content_id(self, value):
        self._med_content_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalSupplierContentPublishResponse, self).parse_response_content(response_content)
        if 'med_content_id' in response:
            self.med_content_id = response['med_content_id']
