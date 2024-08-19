#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayIserviceIcontroldcUserQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayIserviceIcontroldcUserQueryResponse, self).__init__()
        self._nebula_id = None
        self._tnt_inst_id = None
        self._ur_id = None

    @property
    def nebula_id(self):
        return self._nebula_id

    @nebula_id.setter
    def nebula_id(self, value):
        self._nebula_id = value
    @property
    def tnt_inst_id(self):
        return self._tnt_inst_id

    @tnt_inst_id.setter
    def tnt_inst_id(self, value):
        self._tnt_inst_id = value
    @property
    def ur_id(self):
        return self._ur_id

    @ur_id.setter
    def ur_id(self, value):
        self._ur_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayIserviceIcontroldcUserQueryResponse, self).parse_response_content(response_content)
        if 'nebula_id' in response:
            self.nebula_id = response['nebula_id']
        if 'tnt_inst_id' in response:
            self.tnt_inst_id = response['tnt_inst_id']
        if 'ur_id' in response:
            self.ur_id = response['ur_id']
