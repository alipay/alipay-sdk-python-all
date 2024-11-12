#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.GroupJoinRuleVO import GroupJoinRuleVO


class AlipayMerchantGroupJoinruleQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMerchantGroupJoinruleQueryResponse, self).__init__()
        self._group_join_rules = None

    @property
    def group_join_rules(self):
        return self._group_join_rules

    @group_join_rules.setter
    def group_join_rules(self, value):
        if isinstance(value, list):
            self._group_join_rules = list()
            for i in value:
                if isinstance(i, GroupJoinRuleVO):
                    self._group_join_rules.append(i)
                else:
                    self._group_join_rules.append(GroupJoinRuleVO.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayMerchantGroupJoinruleQueryResponse, self).parse_response_content(response_content)
        if 'group_join_rules' in response:
            self.group_join_rules = response['group_join_rules']
