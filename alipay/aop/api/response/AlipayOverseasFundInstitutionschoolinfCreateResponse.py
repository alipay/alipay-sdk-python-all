#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOverseasFundInstitutionschoolinfCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOverseasFundInstitutionschoolinfCreateResponse, self).__init__()
        self._isv_pid = None
        self._isv_request_no = None
        self._pass_through_info = None
        self._school_pid = None

    @property
    def isv_pid(self):
        return self._isv_pid

    @isv_pid.setter
    def isv_pid(self, value):
        self._isv_pid = value
    @property
    def isv_request_no(self):
        return self._isv_request_no

    @isv_request_no.setter
    def isv_request_no(self, value):
        self._isv_request_no = value
    @property
    def pass_through_info(self):
        return self._pass_through_info

    @pass_through_info.setter
    def pass_through_info(self, value):
        self._pass_through_info = value
    @property
    def school_pid(self):
        return self._school_pid

    @school_pid.setter
    def school_pid(self, value):
        self._school_pid = value

    def parse_response_content(self, response_content):
        response = super(AlipayOverseasFundInstitutionschoolinfCreateResponse, self).parse_response_content(response_content)
        if 'isv_pid' in response:
            self.isv_pid = response['isv_pid']
        if 'isv_request_no' in response:
            self.isv_request_no = response['isv_request_no']
        if 'pass_through_info' in response:
            self.pass_through_info = response['pass_through_info']
        if 'school_pid' in response:
            self.school_pid = response['school_pid']
