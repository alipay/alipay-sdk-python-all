#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenLotterymallExchangerecordstatusSyncResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenLotterymallExchangerecordstatusSyncResponse, self).__init__()
        self._errorcode = None
        self._errormsg = None
        self._success = None

    @property
    def errorcode(self):
        return self._errorcode

    @errorcode.setter
    def errorcode(self, value):
        self._errorcode = value
    @property
    def errormsg(self):
        return self._errormsg

    @errormsg.setter
    def errormsg(self, value):
        self._errormsg = value
    @property
    def success(self):
        return self._success

    @success.setter
    def success(self, value):
        self._success = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenLotterymallExchangerecordstatusSyncResponse, self).parse_response_content(response_content)
        if 'errorcode' in response:
            self.errorcode = response['errorcode']
        if 'errormsg' in response:
            self.errormsg = response['errormsg']
        if 'success' in response:
            self.success = response['success']
