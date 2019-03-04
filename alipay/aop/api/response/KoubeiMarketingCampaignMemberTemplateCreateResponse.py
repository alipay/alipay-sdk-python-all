#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class KoubeiMarketingCampaignMemberTemplateCreateResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiMarketingCampaignMemberTemplateCreateResponse, self).__init__()
        self._member_template_id = None

    @property
    def member_template_id(self):
        return self._member_template_id

    @member_template_id.setter
    def member_template_id(self, value):
        self._member_template_id = value

    def parse_response_content(self, response_content):
        response = super(KoubeiMarketingCampaignMemberTemplateCreateResponse, self).parse_response_content(response_content)
        if 'member_template_id' in response:
            self.member_template_id = response['member_template_id']
