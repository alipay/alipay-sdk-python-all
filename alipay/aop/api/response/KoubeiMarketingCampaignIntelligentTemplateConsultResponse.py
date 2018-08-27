#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class KoubeiMarketingCampaignIntelligentTemplateConsultResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiMarketingCampaignIntelligentTemplateConsultResponse, self).__init__()
        self._template_codes = None

    @property
    def template_codes(self):
        return self._template_codes

    @template_codes.setter
    def template_codes(self, value):
        if isinstance(value, list):
            self._template_codes = list()
            for i in value:
                self._template_codes.append(i)

    def parse_response_content(self, response_content):
        response = super(KoubeiMarketingCampaignIntelligentTemplateConsultResponse, self).parse_response_content(response_content)
        if 'template_codes' in response:
            self.template_codes = response['template_codes']
