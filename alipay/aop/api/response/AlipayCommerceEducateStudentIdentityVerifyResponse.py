#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceEducateStudentIdentityVerifyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceEducateStudentIdentityVerifyResponse, self).__init__()
        self._biz_sign = None
        self._college_online_tag = None
        self._degree = None
        self._enroll_date = None
        self._examine_status = None
        self._member_ship_status = None
        self._school_id = None
        self._school_name = None
        self._time_stamp = None
        self._type = None

    @property
    def biz_sign(self):
        return self._biz_sign

    @biz_sign.setter
    def biz_sign(self, value):
        self._biz_sign = value
    @property
    def college_online_tag(self):
        return self._college_online_tag

    @college_online_tag.setter
    def college_online_tag(self, value):
        self._college_online_tag = value
    @property
    def degree(self):
        return self._degree

    @degree.setter
    def degree(self, value):
        self._degree = value
    @property
    def enroll_date(self):
        return self._enroll_date

    @enroll_date.setter
    def enroll_date(self, value):
        self._enroll_date = value
    @property
    def examine_status(self):
        return self._examine_status

    @examine_status.setter
    def examine_status(self, value):
        self._examine_status = value
    @property
    def member_ship_status(self):
        return self._member_ship_status

    @member_ship_status.setter
    def member_ship_status(self, value):
        self._member_ship_status = value
    @property
    def school_id(self):
        return self._school_id

    @school_id.setter
    def school_id(self, value):
        self._school_id = value
    @property
    def school_name(self):
        return self._school_name

    @school_name.setter
    def school_name(self, value):
        self._school_name = value
    @property
    def time_stamp(self):
        return self._time_stamp

    @time_stamp.setter
    def time_stamp(self, value):
        self._time_stamp = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceEducateStudentIdentityVerifyResponse, self).parse_response_content(response_content)
        if 'biz_sign' in response:
            self.biz_sign = response['biz_sign']
        if 'college_online_tag' in response:
            self.college_online_tag = response['college_online_tag']
        if 'degree' in response:
            self.degree = response['degree']
        if 'enroll_date' in response:
            self.enroll_date = response['enroll_date']
        if 'examine_status' in response:
            self.examine_status = response['examine_status']
        if 'member_ship_status' in response:
            self.member_ship_status = response['member_ship_status']
        if 'school_id' in response:
            self.school_id = response['school_id']
        if 'school_name' in response:
            self.school_name = response['school_name']
        if 'time_stamp' in response:
            self.time_stamp = response['time_stamp']
        if 'type' in response:
            self.type = response['type']
