#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.RareNameEncodeInfo import RareNameEncodeInfo


class AlipayUserCertifyRarenameUniandpuaTransferResponse(AlipayResponse):

    def __init__(self):
        super(AlipayUserCertifyRarenameUniandpuaTransferResponse, self).__init__()
        self._other_names = None
        self._ret_name = None

    @property
    def other_names(self):
        return self._other_names

    @other_names.setter
    def other_names(self, value):
        if isinstance(value, list):
            self._other_names = list()
            for i in value:
                if isinstance(i, RareNameEncodeInfo):
                    self._other_names.append(i)
                else:
                    self._other_names.append(RareNameEncodeInfo.from_alipay_dict(i))
    @property
    def ret_name(self):
        return self._ret_name

    @ret_name.setter
    def ret_name(self, value):
        self._ret_name = value

    def parse_response_content(self, response_content):
        response = super(AlipayUserCertifyRarenameUniandpuaTransferResponse, self).parse_response_content(response_content)
        if 'other_names' in response:
            self.other_names = response['other_names']
        if 'ret_name' in response:
            self.ret_name = response['ret_name']
