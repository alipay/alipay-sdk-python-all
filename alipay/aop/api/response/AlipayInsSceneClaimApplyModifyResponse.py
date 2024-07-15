#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayInsSceneClaimApplyModifyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayInsSceneClaimApplyModifyResponse, self).__init__()
        self._claim_report_no = None
        self._partner_org_id = None

    @property
    def claim_report_no(self):
        return self._claim_report_no

    @claim_report_no.setter
    def claim_report_no(self, value):
        self._claim_report_no = value
    @property
    def partner_org_id(self):
        return self._partner_org_id

    @partner_org_id.setter
    def partner_org_id(self, value):
        self._partner_org_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayInsSceneClaimApplyModifyResponse, self).parse_response_content(response_content)
        if 'claim_report_no' in response:
            self.claim_report_no = response['claim_report_no']
        if 'partner_org_id' in response:
            self.partner_org_id = response['partner_org_id']
