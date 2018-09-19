#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCreditCreditriskDataPutResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCreditCreditriskDataPutResponse, self).__init__()
        self._dataid = None

    @property
    def dataid(self):
        return self._dataid

    @dataid.setter
    def dataid(self, value):
        self._dataid = value

    def parse_response_content(self, response_content):
        response = super(AlipayCreditCreditriskDataPutResponse, self).parse_response_content(response_content)
        if 'dataid' in response:
            self.dataid = response['dataid']
