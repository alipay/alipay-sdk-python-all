#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceCityfacilitatorVoucherGenerateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceCityfacilitatorVoucherGenerateResponse, self).__init__()
        self._expired_date = None
        self._qr_code_no = None
        self._ticket_no = None

    @property
    def expired_date(self):
        return self._expired_date

    @expired_date.setter
    def expired_date(self, value):
        self._expired_date = value
    @property
    def qr_code_no(self):
        return self._qr_code_no

    @qr_code_no.setter
    def qr_code_no(self, value):
        self._qr_code_no = value
    @property
    def ticket_no(self):
        return self._ticket_no

    @ticket_no.setter
    def ticket_no(self, value):
        self._ticket_no = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceCityfacilitatorVoucherGenerateResponse, self).parse_response_content(response_content)
        if 'expired_date' in response:
            self.expired_date = response['expired_date']
        if 'qr_code_no' in response:
            self.qr_code_no = response['qr_code_no']
        if 'ticket_no' in response:
            self.ticket_no = response['ticket_no']
