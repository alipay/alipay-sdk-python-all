#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayTradeSolutionprodMerchantupgradeQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayTradeSolutionprodMerchantupgradeQueryResponse, self).__init__()
        self._binding_logon_id = None
        self._fail_reason = None
        self._order_id = None
        self._out_biz_no = None
        self._smid = None
        self._status = None

    @property
    def binding_logon_id(self):
        return self._binding_logon_id

    @binding_logon_id.setter
    def binding_logon_id(self, value):
        self._binding_logon_id = value
    @property
    def fail_reason(self):
        return self._fail_reason

    @fail_reason.setter
    def fail_reason(self, value):
        self._fail_reason = value
    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        self._order_id = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def smid(self):
        return self._smid

    @smid.setter
    def smid(self, value):
        self._smid = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value

    def parse_response_content(self, response_content):
        response = super(AlipayTradeSolutionprodMerchantupgradeQueryResponse, self).parse_response_content(response_content)
        if 'binding_logon_id' in response:
            self.binding_logon_id = response['binding_logon_id']
        if 'fail_reason' in response:
            self.fail_reason = response['fail_reason']
        if 'order_id' in response:
            self.order_id = response['order_id']
        if 'out_biz_no' in response:
            self.out_biz_no = response['out_biz_no']
        if 'smid' in response:
            self.smid = response['smid']
        if 'status' in response:
            self.status = response['status']
