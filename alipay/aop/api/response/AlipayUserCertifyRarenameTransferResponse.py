#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayUserCertifyRarenameTransferResponse(AlipayResponse):

    def __init__(self):
        super(AlipayUserCertifyRarenameTransferResponse, self).__init__()
        self._ret_name_list = None

    @property
    def ret_name_list(self):
        return self._ret_name_list

    @ret_name_list.setter
    def ret_name_list(self, value):
        self._ret_name_list = value

    def parse_response_content(self, response_content):
        response = super(AlipayUserCertifyRarenameTransferResponse, self).parse_response_content(response_content)
        if 'ret_name_list' in response:
            self.ret_name_list = response['ret_name_list']
