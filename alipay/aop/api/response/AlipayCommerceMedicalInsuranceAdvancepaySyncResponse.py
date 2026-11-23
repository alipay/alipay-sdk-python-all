#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceMedicalInsuranceAdvancepaySyncResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalInsuranceAdvancepaySyncResponse, self).__init__()
        self._ant_apply_no = None
        self._data = None

    @property
    def ant_apply_no(self):
        return self._ant_apply_no

    @ant_apply_no.setter
    def ant_apply_no(self, value):
        self._ant_apply_no = value
    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        self._data = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalInsuranceAdvancepaySyncResponse, self).parse_response_content(response_content)
        if 'ant_apply_no' in response:
            self.ant_apply_no = response['ant_apply_no']
        if 'data' in response:
            self.data = response['data']
