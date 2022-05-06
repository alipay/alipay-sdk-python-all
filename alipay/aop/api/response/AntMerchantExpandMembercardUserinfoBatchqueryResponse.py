#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.MemberCardUserInfo import MemberCardUserInfo


class AntMerchantExpandMembercardUserinfoBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AntMerchantExpandMembercardUserinfoBatchqueryResponse, self).__init__()
        self._partner_id = None
        self._user_info_list = None

    @property
    def partner_id(self):
        return self._partner_id

    @partner_id.setter
    def partner_id(self, value):
        self._partner_id = value
    @property
    def user_info_list(self):
        return self._user_info_list

    @user_info_list.setter
    def user_info_list(self, value):
        if isinstance(value, list):
            self._user_info_list = list()
            for i in value:
                if isinstance(i, MemberCardUserInfo):
                    self._user_info_list.append(i)
                else:
                    self._user_info_list.append(MemberCardUserInfo.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AntMerchantExpandMembercardUserinfoBatchqueryResponse, self).parse_response_content(response_content)
        if 'partner_id' in response:
            self.partner_id = response['partner_id']
        if 'user_info_list' in response:
            self.user_info_list = response['user_info_list']
