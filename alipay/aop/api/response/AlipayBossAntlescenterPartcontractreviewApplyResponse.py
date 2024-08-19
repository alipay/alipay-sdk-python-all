#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayBossAntlescenterPartcontractreviewApplyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayBossAntlescenterPartcontractreviewApplyResponse, self).__init__()
        self._apply_manual_review_url = None
        self._contract_no = None

    @property
    def apply_manual_review_url(self):
        return self._apply_manual_review_url

    @apply_manual_review_url.setter
    def apply_manual_review_url(self, value):
        self._apply_manual_review_url = value
    @property
    def contract_no(self):
        return self._contract_no

    @contract_no.setter
    def contract_no(self, value):
        self._contract_no = value

    def parse_response_content(self, response_content):
        response = super(AlipayBossAntlescenterPartcontractreviewApplyResponse, self).parse_response_content(response_content)
        if 'apply_manual_review_url' in response:
            self.apply_manual_review_url = response['apply_manual_review_url']
        if 'contract_no' in response:
            self.contract_no = response['contract_no']
