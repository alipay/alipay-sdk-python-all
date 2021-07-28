#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class ZhimaMerchantZmgoCumulateSyncResponse(AlipayResponse):

    def __init__(self):
        super(ZhimaMerchantZmgoCumulateSyncResponse, self).__init__()
        self._agreement_id = None
        self._fail_reason = None
        self._out_biz_no = None

    @property
    def agreement_id(self):
        return self._agreement_id

    @agreement_id.setter
    def agreement_id(self, value):
        self._agreement_id = value
    @property
    def fail_reason(self):
        return self._fail_reason

    @fail_reason.setter
    def fail_reason(self, value):
        self._fail_reason = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value

    def parse_response_content(self, response_content):
        response = super(ZhimaMerchantZmgoCumulateSyncResponse, self).parse_response_content(response_content)
        if 'agreement_id' in response:
            self.agreement_id = response['agreement_id']
        if 'fail_reason' in response:
            self.fail_reason = response['fail_reason']
        if 'out_biz_no' in response:
            self.out_biz_no = response['out_biz_no']
