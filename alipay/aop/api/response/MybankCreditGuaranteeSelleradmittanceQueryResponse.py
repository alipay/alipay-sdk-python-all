#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class MybankCreditGuaranteeSelleradmittanceQueryResponse(AlipayResponse):

    def __init__(self):
        super(MybankCreditGuaranteeSelleradmittanceQueryResponse, self).__init__()
        self._is_admitted = None
        self._is_signed = None
        self._is_unsigned = None
        self._unsign_date = None

    @property
    def is_admitted(self):
        return self._is_admitted

    @is_admitted.setter
    def is_admitted(self, value):
        self._is_admitted = value
    @property
    def is_signed(self):
        return self._is_signed

    @is_signed.setter
    def is_signed(self, value):
        self._is_signed = value
    @property
    def is_unsigned(self):
        return self._is_unsigned

    @is_unsigned.setter
    def is_unsigned(self, value):
        self._is_unsigned = value
    @property
    def unsign_date(self):
        return self._unsign_date

    @unsign_date.setter
    def unsign_date(self, value):
        self._unsign_date = value

    def parse_response_content(self, response_content):
        response = super(MybankCreditGuaranteeSelleradmittanceQueryResponse, self).parse_response_content(response_content)
        if 'is_admitted' in response:
            self.is_admitted = response['is_admitted']
        if 'is_signed' in response:
            self.is_signed = response['is_signed']
        if 'is_unsigned' in response:
            self.is_unsigned = response['is_unsigned']
        if 'unsign_date' in response:
            self.unsign_date = response['unsign_date']
