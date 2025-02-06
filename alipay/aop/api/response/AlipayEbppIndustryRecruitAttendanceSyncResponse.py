#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayEbppIndustryRecruitAttendanceSyncResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEbppIndustryRecruitAttendanceSyncResponse, self).__init__()
        self._attendance_id = None

    @property
    def attendance_id(self):
        return self._attendance_id

    @attendance_id.setter
    def attendance_id(self, value):
        self._attendance_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayEbppIndustryRecruitAttendanceSyncResponse, self).parse_response_content(response_content)
        if 'attendance_id' in response:
            self.attendance_id = response['attendance_id']
