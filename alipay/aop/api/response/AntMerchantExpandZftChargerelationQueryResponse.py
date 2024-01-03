#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AntMerchantExpandZftChargerelationQueryResponse(AlipayResponse):

    def __init__(self):
        super(AntMerchantExpandZftChargerelationQueryResponse, self).__init__()
        self._audit_memo = None
        self._order_id = None
        self._reason = None
        self._smid = None
        self._status = None
        self._target_smid = None

    @property
    def audit_memo(self):
        return self._audit_memo

    @audit_memo.setter
    def audit_memo(self, value):
        self._audit_memo = value
    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        self._order_id = value
    @property
    def reason(self):
        return self._reason

    @reason.setter
    def reason(self, value):
        self._reason = value
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
    @property
    def target_smid(self):
        return self._target_smid

    @target_smid.setter
    def target_smid(self, value):
        self._target_smid = value

    def parse_response_content(self, response_content):
        response = super(AntMerchantExpandZftChargerelationQueryResponse, self).parse_response_content(response_content)
        if 'audit_memo' in response:
            self.audit_memo = response['audit_memo']
        if 'order_id' in response:
            self.order_id = response['order_id']
        if 'reason' in response:
            self.reason = response['reason']
        if 'smid' in response:
            self.smid = response['smid']
        if 'status' in response:
            self.status = response['status']
        if 'target_smid' in response:
            self.target_smid = response['target_smid']
