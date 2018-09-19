#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ItermInfo import ItermInfo


class AlipayEbppRechargeItemGetResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEbppRechargeItemGetResponse, self).__init__()
        self._error_code = None
        self._error_message = None
        self._iterm_infos = None
        self._success = None

    @property
    def error_code(self):
        return self._error_code

    @error_code.setter
    def error_code(self, value):
        self._error_code = value
    @property
    def error_message(self):
        return self._error_message

    @error_message.setter
    def error_message(self, value):
        self._error_message = value
    @property
    def iterm_infos(self):
        return self._iterm_infos

    @iterm_infos.setter
    def iterm_infos(self, value):
        if isinstance(value, list):
            self._iterm_infos = list()
            for i in value:
                if isinstance(i, ItermInfo):
                    self._iterm_infos.append(i)
                else:
                    self._iterm_infos.append(ItermInfo.from_alipay_dict(i))
    @property
    def success(self):
        return self._success

    @success.setter
    def success(self, value):
        self._success = value

    def parse_response_content(self, response_content):
        response = super(AlipayEbppRechargeItemGetResponse, self).parse_response_content(response_content)
        if 'error_code' in response:
            self.error_code = response['error_code']
        if 'error_message' in response:
            self.error_message = response['error_message']
        if 'iterm_infos' in response:
            self.iterm_infos = response['iterm_infos']
        if 'success' in response:
            self.success = response['success']
