#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayFundFlexiblestaffingEmployeehomeUnsignResponse(AlipayResponse):

    def __init__(self):
        super(AlipayFundFlexiblestaffingEmployeehomeUnsignResponse, self).__init__()
        self._id = None
        self._status = None

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value

    def parse_response_content(self, response_content):
        response = super(AlipayFundFlexiblestaffingEmployeehomeUnsignResponse, self).parse_response_content(response_content)
        if 'id' in response:
            self.id = response['id']
        if 'status' in response:
            self.status = response['status']
