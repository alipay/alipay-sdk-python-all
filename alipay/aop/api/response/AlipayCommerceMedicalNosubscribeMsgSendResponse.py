#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceMedicalNosubscribeMsgSendResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalNosubscribeMsgSendResponse, self).__init__()
        self._msg_id_list = None
        self._out_msg_id = None

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
    def out_msg_id(self):
        return self._out_msg_id

    @out_msg_id.setter
    def out_msg_id(self, value):
        self._out_msg_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalNosubscribeMsgSendResponse, self).parse_response_content(response_content)
        if 'msg_id_list' in response:
            self.msg_id_list = response['msg_id_list']
        if 'out_msg_id' in response:
            self.out_msg_id = response['out_msg_id']
