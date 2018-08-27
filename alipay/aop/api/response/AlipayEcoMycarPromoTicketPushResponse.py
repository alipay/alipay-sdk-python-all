#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayEcoMycarPromoTicketPushResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEcoMycarPromoTicketPushResponse, self).__init__()
        self._sp_apply_no = None

    @property
    def sp_apply_no(self):
        return self._sp_apply_no

    @sp_apply_no.setter
    def sp_apply_no(self, value):
        self._sp_apply_no = value

    def parse_response_content(self, response_content):
        response = super(AlipayEcoMycarPromoTicketPushResponse, self).parse_response_content(response_content)
        if 'sp_apply_no' in response:
            self.sp_apply_no = response['sp_apply_no']
