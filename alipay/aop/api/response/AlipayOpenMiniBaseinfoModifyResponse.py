#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenMiniBaseinfoModifyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenMiniBaseinfoModifyResponse, self).__init__()
        self._modify_status = None

    @property
    def modify_status(self):
        return self._modify_status

    @modify_status.setter
    def modify_status(self, value):
        self._modify_status = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenMiniBaseinfoModifyResponse, self).parse_response_content(response_content)
        if 'modify_status' in response:
            self.modify_status = response['modify_status']
