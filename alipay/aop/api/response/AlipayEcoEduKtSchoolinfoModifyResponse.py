#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayEcoEduKtSchoolinfoModifyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEcoEduKtSchoolinfoModifyResponse, self).__init__()
        self._school_no = None
        self._status = None

    @property
    def school_no(self):
        return self._school_no

    @school_no.setter
    def school_no(self, value):
        self._school_no = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value

    def parse_response_content(self, response_content):
        response = super(AlipayEcoEduKtSchoolinfoModifyResponse, self).parse_response_content(response_content)
        if 'school_no' in response:
            self.school_no = response['school_no']
        if 'status' in response:
            self.status = response['status']
