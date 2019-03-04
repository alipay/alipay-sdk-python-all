#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayEcoEduKtZftschoolQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEcoEduKtZftschoolQueryResponse, self).__init__()
        self._reason = None
        self._school_no = None
        self._smid = None
        self._status = None

    @property
    def reason(self):
        return self._reason

    @reason.setter
    def reason(self, value):
        self._reason = value
    @property
    def school_no(self):
        return self._school_no

    @school_no.setter
    def school_no(self, value):
        self._school_no = value
    @property
    def smid(self):
        return self._smid

    @smid.setter
    def smid(self, value):
        self._smid = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value

    def parse_response_content(self, response_content):
        response = super(AlipayEcoEduKtZftschoolQueryResponse, self).parse_response_content(response_content)
        if 'reason' in response:
            self.reason = response['reason']
        if 'school_no' in response:
            self.school_no = response['school_no']
        if 'smid' in response:
            self.smid = response['smid']
        if 'status' in response:
            self.status = response['status']
