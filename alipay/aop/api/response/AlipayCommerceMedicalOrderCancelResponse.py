#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceMedicalOrderCancelResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalOrderCancelResponse, self).__init__()
        self._data = None
        self._refund_msg = None
        self._refund_no = None
        self._refund_status = None

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        self._data = value
    @property
    def refund_msg(self):
        return self._refund_msg

    @refund_msg.setter
    def refund_msg(self, value):
        self._refund_msg = value
    @property
    def refund_no(self):
        return self._refund_no

    @refund_no.setter
    def refund_no(self, value):
        self._refund_no = value
    @property
    def refund_status(self):
        return self._refund_status

    @refund_status.setter
    def refund_status(self, value):
        self._refund_status = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalOrderCancelResponse, self).parse_response_content(response_content)
        if 'data' in response:
            self.data = response['data']
        if 'refund_msg' in response:
            self.refund_msg = response['refund_msg']
        if 'refund_no' in response:
            self.refund_no = response['refund_no']
        if 'refund_status' in response:
            self.refund_status = response['refund_status']
