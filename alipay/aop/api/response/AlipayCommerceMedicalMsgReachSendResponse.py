#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceMedicalMsgReachSendResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalMsgReachSendResponse, self).__init__()
        self._channel_results = None
        self._out_biz_no = None

    @property
    def channel_results(self):
        return self._channel_results

    @channel_results.setter
    def channel_results(self, value):
        if isinstance(value, list):
            self._channel_results = list()
            for i in value:
                self._channel_results.append(i)
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalMsgReachSendResponse, self).parse_response_content(response_content)
        if 'channel_results' in response:
            self.channel_results = response['channel_results']
        if 'out_biz_no' in response:
            self.out_biz_no = response['out_biz_no']
