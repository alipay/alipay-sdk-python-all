#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayInsSceneFlowcardBindcardNotifyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayInsSceneFlowcardBindcardNotifyResponse, self).__init__()
        self._ant_ser_apply_no = None

    @property
    def ant_ser_apply_no(self):
        return self._ant_ser_apply_no

    @ant_ser_apply_no.setter
    def ant_ser_apply_no(self, value):
        self._ant_ser_apply_no = value

    def parse_response_content(self, response_content):
        response = super(AlipayInsSceneFlowcardBindcardNotifyResponse, self).parse_response_content(response_content)
        if 'ant_ser_apply_no' in response:
            self.ant_ser_apply_no = response['ant_ser_apply_no']
