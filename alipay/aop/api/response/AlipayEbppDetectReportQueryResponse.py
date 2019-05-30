#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayEbppDetectReportQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEbppDetectReportQueryResponse, self).__init__()
        self._audit_done = None
        self._audit_pass = None
        self._err_msg = None
        self._out_biz_no = None

    @property
    def audit_done(self):
        return self._audit_done

    @audit_done.setter
    def audit_done(self, value):
        self._audit_done = value
    @property
    def audit_pass(self):
        return self._audit_pass

    @audit_pass.setter
    def audit_pass(self, value):
        self._audit_pass = value
    @property
    def err_msg(self):
        return self._err_msg

    @err_msg.setter
    def err_msg(self, value):
        self._err_msg = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value

    def parse_response_content(self, response_content):
        response = super(AlipayEbppDetectReportQueryResponse, self).parse_response_content(response_content)
        if 'audit_done' in response:
            self.audit_done = response['audit_done']
        if 'audit_pass' in response:
            self.audit_pass = response['audit_pass']
        if 'err_msg' in response:
            self.err_msg = response['err_msg']
        if 'out_biz_no' in response:
            self.out_biz_no = response['out_biz_no']
