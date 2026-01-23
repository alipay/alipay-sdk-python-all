#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceMedicalHdfcheckSyncResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalHdfcheckSyncResponse, self).__init__()
        self._hdf_check_no = None

    @property
    def hdf_check_no(self):
        return self._hdf_check_no

    @hdf_check_no.setter
    def hdf_check_no(self, value):
        self._hdf_check_no = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalHdfcheckSyncResponse, self).parse_response_content(response_content)
        if 'hdf_check_no' in response:
            self.hdf_check_no = response['hdf_check_no']
