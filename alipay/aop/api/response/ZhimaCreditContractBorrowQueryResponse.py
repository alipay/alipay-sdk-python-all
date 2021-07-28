#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class ZhimaCreditContractBorrowQueryResponse(AlipayResponse):

    def __init__(self):
        super(ZhimaCreditContractBorrowQueryResponse, self).__init__()
        self._status = None
        self._subjects_borrowed = None
        self._subjects_returned = None

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def subjects_borrowed(self):
        return self._subjects_borrowed

    @subjects_borrowed.setter
    def subjects_borrowed(self, value):
        self._subjects_borrowed = value
    @property
    def subjects_returned(self):
        return self._subjects_returned

    @subjects_returned.setter
    def subjects_returned(self, value):
        self._subjects_returned = value

    def parse_response_content(self, response_content):
        response = super(ZhimaCreditContractBorrowQueryResponse, self).parse_response_content(response_content)
        if 'status' in response:
            self.status = response['status']
        if 'subjects_borrowed' in response:
            self.subjects_borrowed = response['subjects_borrowed']
        if 'subjects_returned' in response:
            self.subjects_returned = response['subjects_returned']
