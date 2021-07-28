#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.CommunityPartnerRelationDataSyncDTO import CommunityPartnerRelationDataSyncDTO


class AlipayOpenAppCommunityPartnerSyncResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenAppCommunityPartnerSyncResponse, self).__init__()
        self._target_list = None

    @property
    def target_list(self):
        return self._target_list

    @target_list.setter
    def target_list(self, value):
        if isinstance(value, list):
            self._target_list = list()
            for i in value:
                if isinstance(i, CommunityPartnerRelationDataSyncDTO):
                    self._target_list.append(i)
                else:
                    self._target_list.append(CommunityPartnerRelationDataSyncDTO.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayOpenAppCommunityPartnerSyncResponse, self).parse_response_content(response_content)
        if 'target_list' in response:
            self.target_list = response['target_list']
