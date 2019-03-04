#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.MerchantMemberTemplateModel import MerchantMemberTemplateModel


class KoubeiMarketingCampaignMemberTemplateBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiMarketingCampaignMemberTemplateBatchqueryResponse, self).__init__()
        self._member_templates = None

    @property
    def member_templates(self):
        return self._member_templates

    @member_templates.setter
    def member_templates(self, value):
        if isinstance(value, list):
            self._member_templates = list()
            for i in value:
                if isinstance(i, MerchantMemberTemplateModel):
                    self._member_templates.append(i)
                else:
                    self._member_templates.append(MerchantMemberTemplateModel.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(KoubeiMarketingCampaignMemberTemplateBatchqueryResponse, self).parse_response_content(response_content)
        if 'member_templates' in response:
            self.member_templates = response['member_templates']
