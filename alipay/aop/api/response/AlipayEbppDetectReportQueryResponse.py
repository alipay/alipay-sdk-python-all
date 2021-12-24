#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayEbppDetectReportQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEbppDetectReportQueryResponse, self).__init__()
        self._audit_done = None
        self._audit_pass = None
        self._detail_report = None
        self._detect_detail = None
        self._detect_result = None
        self._detect_result_detail_list = None
        self._detect_status = None
        self._err_msg = None
        self._out_biz_no = None
        self._pass = None
        self._summary = None

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
    def detail_report(self):
        return self._detail_report

    @detail_report.setter
    def detail_report(self, value):
        self._detail_report = value
    @property
    def detect_detail(self):
        return self._detect_detail

    @detect_detail.setter
    def detect_detail(self, value):
        self._detect_detail = value
    @property
    def detect_result(self):
        return self._detect_result

    @detect_result.setter
    def detect_result(self, value):
        self._detect_result = value
    @property
    def detect_result_detail_list(self):
        return self._detect_result_detail_list

    @detect_result_detail_list.setter
    def detect_result_detail_list(self, value):
        if isinstance(value, list):
            self._detect_result_detail_list = list()
            for i in value:
                self._detect_result_detail_list.append(i)
    @property
    def detect_status(self):
        return self._detect_status

    @detect_status.setter
    def detect_status(self, value):
        self._detect_status = value
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
    @property
    def pass(self):
        return self._pass

    @pass.setter
    def pass(self, value):
        self._pass = value
    @property
    def summary(self):
        return self._summary

    @summary.setter
    def summary(self, value):
        self._summary = value

    def parse_response_content(self, response_content):
        response = super(AlipayEbppDetectReportQueryResponse, self).parse_response_content(response_content)
        if 'audit_done' in response:
            self.audit_done = response['audit_done']
        if 'audit_pass' in response:
            self.audit_pass = response['audit_pass']
        if 'detail_report' in response:
            self.detail_report = response['detail_report']
        if 'detect_detail' in response:
            self.detect_detail = response['detect_detail']
        if 'detect_result' in response:
            self.detect_result = response['detect_result']
        if 'detect_result_detail_list' in response:
            self.detect_result_detail_list = response['detect_result_detail_list']
        if 'detect_status' in response:
            self.detect_status = response['detect_status']
        if 'err_msg' in response:
            self.err_msg = response['err_msg']
        if 'out_biz_no' in response:
            self.out_biz_no = response['out_biz_no']
        if 'pass' in response:
            self.pass = response['pass']
        if 'summary' in response:
            self.summary = response['summary']
