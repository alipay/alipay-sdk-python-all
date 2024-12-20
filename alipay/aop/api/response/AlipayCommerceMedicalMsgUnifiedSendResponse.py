#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceMedicalMsgUnifiedSendResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalMsgUnifiedSendResponse, self).__init__()
        self._msg_id_list = None
        self._out_biz_no = None

    @property
    def msg_id_list(self):
        return self._msg_id_list

    @msg_id_list.setter
    def msg_id_list(self, value):
        if isinstance(value, list):
            self._msg_id_list = list()
            for i in value:
                self._msg_id_list.append(i)
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalMsgUnifiedSendResponse, self).parse_response_content(response_content)
        if 'msg_id_list' in response:
            self.msg_id_list = response['msg_id_list']
        if 'out_biz_no' in response:
            self.out_biz_no = response['out_biz_no']
