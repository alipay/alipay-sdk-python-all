#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.AdPublicTabInfo import AdPublicTabInfo


class AlipayDataDataserviceAdcampaignSeriestabQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayDataDataserviceAdcampaignSeriestabQueryResponse, self).__init__()
        self._public_list = None

    @property
    def public_list(self):
        return self._public_list

    @public_list.setter
    def public_list(self, value):
        if isinstance(value, list):
            self._public_list = list()
            for i in value:
                if isinstance(i, AdPublicTabInfo):
                    self._public_list.append(i)
                else:
                    self._public_list.append(AdPublicTabInfo.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayDataDataserviceAdcampaignSeriestabQueryResponse, self).parse_response_content(response_content)
        if 'public_list' in response:
            self.public_list = response['public_list']
