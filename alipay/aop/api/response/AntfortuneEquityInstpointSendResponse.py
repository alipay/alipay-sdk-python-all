#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AntfortuneEquityInstpointSendResponse(AlipayResponse):

    def __init__(self):
        super(AntfortuneEquityInstpointSendResponse, self).__init__()
        self._point_trans_no = None
        self._send_result = None

    @property
    def point_trans_no(self):
        return self._point_trans_no

    @point_trans_no.setter
    def point_trans_no(self, value):
        self._point_trans_no = value
    @property
    def send_result(self):
        return self._send_result

    @send_result.setter
    def send_result(self, value):
        self._send_result = value

    def parse_response_content(self, response_content):
        response = super(AntfortuneEquityInstpointSendResponse, self).parse_response_content(response_content)
        if 'point_trans_no' in response:
            self.point_trans_no = response['point_trans_no']
        if 'send_result' in response:
            self.send_result = response['send_result']
