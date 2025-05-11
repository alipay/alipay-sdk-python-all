#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceLogisticsFreightflowTransferApplyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceLogisticsFreightflowTransferApplyResponse, self).__init__()
        self._bank_operate_no = None
        self._biz_no = None
        self._partner_id = None
        self._status = None

    @property
    def bank_operate_no(self):
        return self._bank_operate_no

    @bank_operate_no.setter
    def bank_operate_no(self, value):
        self._bank_operate_no = value
    @property
    def biz_no(self):
        return self._biz_no

    @biz_no.setter
    def biz_no(self, value):
        self._biz_no = value
    @property
    def partner_id(self):
        return self._partner_id

    @partner_id.setter
    def partner_id(self, value):
        self._partner_id = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceLogisticsFreightflowTransferApplyResponse, self).parse_response_content(response_content)
        if 'bank_operate_no' in response:
            self.bank_operate_no = response['bank_operate_no']
        if 'biz_no' in response:
            self.biz_no = response['biz_no']
        if 'partner_id' in response:
            self.partner_id = response['partner_id']
        if 'status' in response:
            self.status = response['status']
