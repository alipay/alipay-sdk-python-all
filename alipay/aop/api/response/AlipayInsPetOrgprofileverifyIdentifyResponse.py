#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayInsPetOrgprofileverifyIdentifyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayInsPetOrgprofileverifyIdentifyResponse, self).__init__()
        self._check_record_no = None

    @property
    def check_record_no(self):
        return self._check_record_no

    @check_record_no.setter
    def check_record_no(self, value):
        self._check_record_no = value

    def parse_response_content(self, response_content):
        response = super(AlipayInsPetOrgprofileverifyIdentifyResponse, self).parse_response_content(response_content)
        if 'check_record_no' in response:
            self.check_record_no = response['check_record_no']
