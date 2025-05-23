#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceMedicalInstitutionExportQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalInstitutionExportQueryResponse, self).__init__()
        self._daily_export_data = None

    @property
    def daily_export_data(self):
        return self._daily_export_data

    @daily_export_data.setter
    def daily_export_data(self, value):
        self._daily_export_data = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalInstitutionExportQueryResponse, self).parse_response_content(response_content)
        if 'daily_export_data' in response:
            self.daily_export_data = response['daily_export_data']
