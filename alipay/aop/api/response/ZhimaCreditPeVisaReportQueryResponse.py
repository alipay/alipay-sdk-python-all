#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class ZhimaCreditPeVisaReportQueryResponse(AlipayResponse):

    def __init__(self):
        super(ZhimaCreditPeVisaReportQueryResponse, self).__init__()
        self._report_apply_status = None
        self._report_content_files = None
        self._user_permit_status = None

    @property
    def report_apply_status(self):
        return self._report_apply_status

    @report_apply_status.setter
    def report_apply_status(self, value):
        self._report_apply_status = value
    @property
    def report_content_files(self):
        return self._report_content_files

    @report_content_files.setter
    def report_content_files(self, value):
        if isinstance(value, list):
            self._report_content_files = list()
            for i in value:
                self._report_content_files.append(i)
    @property
    def user_permit_status(self):
        return self._user_permit_status

    @user_permit_status.setter
    def user_permit_status(self, value):
        self._user_permit_status = value

    def parse_response_content(self, response_content):
        response = super(ZhimaCreditPeVisaReportQueryResponse, self).parse_response_content(response_content)
        if 'report_apply_status' in response:
            self.report_apply_status = response['report_apply_status']
        if 'report_content_files' in response:
            self.report_content_files = response['report_content_files']
        if 'user_permit_status' in response:
            self.user_permit_status = response['user_permit_status']
