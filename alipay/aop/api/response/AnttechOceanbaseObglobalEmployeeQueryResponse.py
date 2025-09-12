#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AnttechOceanbaseObglobalEmployeeQueryResponse(AlipayResponse):

    def __init__(self):
        super(AnttechOceanbaseObglobalEmployeeQueryResponse, self).__init__()
        self._dept_name = None
        self._dept_no = None
        self._dept_short_name = None
        self._email_addr = None
        self._emp_id = None
        self._last_name = None
        self._nick_name_cn = None
        self._super_nick_name = None
        self._super_work_no = None

    @property
    def dept_name(self):
        return self._dept_name

    @dept_name.setter
    def dept_name(self, value):
        self._dept_name = value
    @property
    def dept_no(self):
        return self._dept_no

    @dept_no.setter
    def dept_no(self, value):
        self._dept_no = value
    @property
    def dept_short_name(self):
        return self._dept_short_name

    @dept_short_name.setter
    def dept_short_name(self, value):
        self._dept_short_name = value
    @property
    def email_addr(self):
        return self._email_addr

    @email_addr.setter
    def email_addr(self, value):
        self._email_addr = value
    @property
    def emp_id(self):
        return self._emp_id

    @emp_id.setter
    def emp_id(self, value):
        self._emp_id = value
    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, value):
        self._last_name = value
    @property
    def nick_name_cn(self):
        return self._nick_name_cn

    @nick_name_cn.setter
    def nick_name_cn(self, value):
        self._nick_name_cn = value
    @property
    def super_nick_name(self):
        return self._super_nick_name

    @super_nick_name.setter
    def super_nick_name(self, value):
        self._super_nick_name = value
    @property
    def super_work_no(self):
        return self._super_work_no

    @super_work_no.setter
    def super_work_no(self, value):
        self._super_work_no = value

    def parse_response_content(self, response_content):
        response = super(AnttechOceanbaseObglobalEmployeeQueryResponse, self).parse_response_content(response_content)
        if 'dept_name' in response:
            self.dept_name = response['dept_name']
        if 'dept_no' in response:
            self.dept_no = response['dept_no']
        if 'dept_short_name' in response:
            self.dept_short_name = response['dept_short_name']
        if 'email_addr' in response:
            self.email_addr = response['email_addr']
        if 'emp_id' in response:
            self.emp_id = response['emp_id']
        if 'last_name' in response:
            self.last_name = response['last_name']
        if 'nick_name_cn' in response:
            self.nick_name_cn = response['nick_name_cn']
        if 'super_nick_name' in response:
            self.super_nick_name = response['super_nick_name']
        if 'super_work_no' in response:
            self.super_work_no = response['super_work_no']
