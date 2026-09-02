#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class XingheLendassistCarfinOrgexpressCancelResponse(AlipayResponse):

    def __init__(self):
        super(XingheLendassistCarfinOrgexpressCancelResponse, self).__init__()
        self._refuse_msg = None
        self._status = None

    @property
    def refuse_msg(self):
        return self._refuse_msg

    @refuse_msg.setter
    def refuse_msg(self, value):
        self._refuse_msg = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value

    def parse_response_content(self, response_content):
        response = super(XingheLendassistCarfinOrgexpressCancelResponse, self).parse_response_content(response_content)
        if 'refuse_msg' in response:
            self.refuse_msg = response['refuse_msg']
        if 'status' in response:
            self.status = response['status']
