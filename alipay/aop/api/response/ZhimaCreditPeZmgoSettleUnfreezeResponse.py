#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class ZhimaCreditPeZmgoSettleUnfreezeResponse(AlipayResponse):

    def __init__(self):
        super(ZhimaCreditPeZmgoSettleUnfreezeResponse, self).__init__()
        self._fail_reaseon = None
        self._retry = None
        self._unfreeze_amount = None
        self._unfreeze_status = None

    @property
    def fail_reaseon(self):
        return self._fail_reaseon

    @fail_reaseon.setter
    def fail_reaseon(self, value):
        self._fail_reaseon = value
    @property
    def retry(self):
        return self._retry

    @retry.setter
    def retry(self, value):
        self._retry = value
    @property
    def unfreeze_amount(self):
        return self._unfreeze_amount

    @unfreeze_amount.setter
    def unfreeze_amount(self, value):
        self._unfreeze_amount = value
    @property
    def unfreeze_status(self):
        return self._unfreeze_status

    @unfreeze_status.setter
    def unfreeze_status(self, value):
        self._unfreeze_status = value

    def parse_response_content(self, response_content):
        response = super(ZhimaCreditPeZmgoSettleUnfreezeResponse, self).parse_response_content(response_content)
        if 'fail_reaseon' in response:
            self.fail_reaseon = response['fail_reaseon']
        if 'retry' in response:
            self.retry = response['retry']
        if 'unfreeze_amount' in response:
            self.unfreeze_amount = response['unfreeze_amount']
        if 'unfreeze_status' in response:
            self.unfreeze_status = response['unfreeze_status']
