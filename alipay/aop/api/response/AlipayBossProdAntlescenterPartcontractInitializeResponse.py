#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayBossProdAntlescenterPartcontractInitializeResponse(AlipayResponse):

    def __init__(self):
        super(AlipayBossProdAntlescenterPartcontractInitializeResponse, self).__init__()
        self._contract_no = None

    @property
    def contract_no(self):
        return self._contract_no

    @contract_no.setter
    def contract_no(self, value):
        self._contract_no = value

    def parse_response_content(self, response_content):
        response = super(AlipayBossProdAntlescenterPartcontractInitializeResponse, self).parse_response_content(response_content)
        if 'contract_no' in response:
            self.contract_no = response['contract_no']
