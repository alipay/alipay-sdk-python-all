#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.UserOrgEntityInfoDTO import UserOrgEntityInfoDTO


class AnttechOceanbaseUserorgentityBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AnttechOceanbaseUserorgentityBatchqueryResponse, self).__init__()
        self._user_org_entity_info_list = None

    @property
    def user_org_entity_info_list(self):
        return self._user_org_entity_info_list

    @user_org_entity_info_list.setter
    def user_org_entity_info_list(self, value):
        if isinstance(value, list):
            self._user_org_entity_info_list = list()
            for i in value:
                if isinstance(i, UserOrgEntityInfoDTO):
                    self._user_org_entity_info_list.append(i)
                else:
                    self._user_org_entity_info_list.append(UserOrgEntityInfoDTO.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AnttechOceanbaseUserorgentityBatchqueryResponse, self).parse_response_content(response_content)
        if 'user_org_entity_info_list' in response:
            self.user_org_entity_info_list = response['user_org_entity_info_list']
