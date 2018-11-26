#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class MybankCreditGuaranteeWriteoffPayResponse(AlipayResponse):

    def __init__(self):
        super(MybankCreditGuaranteeWriteoffPayResponse, self).__init__()
        self._writeoff_apply_no = None

    @property
    def writeoff_apply_no(self):
        return self._writeoff_apply_no

    @writeoff_apply_no.setter
    def writeoff_apply_no(self, value):
        self._writeoff_apply_no = value

    def parse_response_content(self, response_content):
        response = super(MybankCreditGuaranteeWriteoffPayResponse, self).parse_response_content(response_content)
        if 'writeoff_apply_no' in response:
            self.writeoff_apply_no = response['writeoff_apply_no']
