#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class KoubeiMarketingCampaignMemberAuthApplyResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiMarketingCampaignMemberAuthApplyResponse, self).__init__()
        self._infos = None
        self._user_id = None

    @property
    def infos(self):
        return self._infos

    @infos.setter
    def infos(self, value):
        self._infos = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value

    def parse_response_content(self, response_content):
        response = super(KoubeiMarketingCampaignMemberAuthApplyResponse, self).parse_response_content(response_content)
        if 'infos' in response:
            self.infos = response['infos']
        if 'user_id' in response:
            self.user_id = response['user_id']
