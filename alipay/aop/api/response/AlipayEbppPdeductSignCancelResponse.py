#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayEbppPdeductSignCancelResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEbppPdeductSignCancelResponse, self).__init__()
        self._agreement_id = None
        self._agreement_status = None
        self._out_agreement_id = None

    @property
    def agreement_id(self):
        return self._agreement_id

    @agreement_id.setter
    def agreement_id(self, value):
        self._agreement_id = value
    @property
    def agreement_status(self):
        return self._agreement_status

    @agreement_status.setter
    def agreement_status(self, value):
        self._agreement_status = value
    @property
    def out_agreement_id(self):
        return self._out_agreement_id

    @out_agreement_id.setter
    def out_agreement_id(self, value):
        self._out_agreement_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayEbppPdeductSignCancelResponse, self).parse_response_content(response_content)
        if 'agreement_id' in response:
            self.agreement_id = response['agreement_id']
        if 'agreement_status' in response:
            self.agreement_status = response['agreement_status']
        if 'out_agreement_id' in response:
            self.out_agreement_id = response['out_agreement_id']
