#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceMedicalPatientsigninPatientdataSendResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalPatientsigninPatientdataSendResponse, self).__init__()
        self._pushflag = None

    @property
    def pushflag(self):
        return self._pushflag

    @pushflag.setter
    def pushflag(self, value):
        self._pushflag = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalPatientsigninPatientdataSendResponse, self).parse_response_content(response_content)
        if 'pushflag' in response:
            self.pushflag = response['pushflag']
