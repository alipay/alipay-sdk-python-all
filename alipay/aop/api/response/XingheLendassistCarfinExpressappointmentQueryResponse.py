#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class XingheLendassistCarfinExpressappointmentQueryResponse(AlipayResponse):

    def __init__(self):
        super(XingheLendassistCarfinExpressappointmentQueryResponse, self).__init__()
        self._appointment_list = None

    @property
    def appointment_list(self):
        return self._appointment_list

    @appointment_list.setter
    def appointment_list(self, value):
        self._appointment_list = value

    def parse_response_content(self, response_content):
        response = super(XingheLendassistCarfinExpressappointmentQueryResponse, self).parse_response_content(response_content)
        if 'appointment_list' in response:
            self.appointment_list = response['appointment_list']
