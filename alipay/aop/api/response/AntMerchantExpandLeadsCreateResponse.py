#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AntMerchantExpandLeadsCreateResponse(AlipayResponse):

    def __init__(self):
        super(AntMerchantExpandLeadsCreateResponse, self).__init__()
        self._fail_reason = None
        self._leads_id = None
        self._need_audit = None
        self._out_biz_id = None
        self._pass = None
        self._repeat_leads_id = None

    @property
    def fail_reason(self):
        return self._fail_reason

    @fail_reason.setter
    def fail_reason(self, value):
        self._fail_reason = value
    @property
    def leads_id(self):
        return self._leads_id

    @leads_id.setter
    def leads_id(self, value):
        self._leads_id = value
    @property
    def need_audit(self):
        return self._need_audit

    @need_audit.setter
    def need_audit(self, value):
        self._need_audit = value
    @property
    def out_biz_id(self):
        return self._out_biz_id

    @out_biz_id.setter
    def out_biz_id(self, value):
        self._out_biz_id = value
    @property
    def pass(self):
        return self._pass

    @pass.setter
    def pass(self, value):
        self._pass = value
    @property
    def repeat_leads_id(self):
        return self._repeat_leads_id

    @repeat_leads_id.setter
    def repeat_leads_id(self, value):
        self._repeat_leads_id = value

    def parse_response_content(self, response_content):
        response = super(AntMerchantExpandLeadsCreateResponse, self).parse_response_content(response_content)
        if 'fail_reason' in response:
            self.fail_reason = response['fail_reason']
        if 'leads_id' in response:
            self.leads_id = response['leads_id']
        if 'need_audit' in response:
            self.need_audit = response['need_audit']
        if 'out_biz_id' in response:
            self.out_biz_id = response['out_biz_id']
        if 'pass' in response:
            self.pass = response['pass']
        if 'repeat_leads_id' in response:
            self.repeat_leads_id = response['repeat_leads_id']
