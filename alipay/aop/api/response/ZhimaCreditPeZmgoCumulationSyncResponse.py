#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class ZhimaCreditPeZmgoCumulationSyncResponse(AlipayResponse):

    def __init__(self):
        super(ZhimaCreditPeZmgoCumulationSyncResponse, self).__init__()
        self._agreement_no = None
        self._fail_reason = None
        self._out_biz_no = None
        self._user_id = None

    @property
    def agreement_no(self):
        return self._agreement_no

    @agreement_no.setter
    def agreement_no(self, value):
        self._agreement_no = value
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
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value

    def parse_response_content(self, response_content):
        response = super(ZhimaCreditPeZmgoCumulationSyncResponse, self).parse_response_content(response_content)
        if 'agreement_no' in response:
            self.agreement_no = response['agreement_no']
        if 'fail_reason' in response:
            self.fail_reason = response['fail_reason']
        if 'out_biz_no' in response:
            self.out_biz_no = response['out_biz_no']
        if 'user_id' in response:
            self.user_id = response['user_id']
