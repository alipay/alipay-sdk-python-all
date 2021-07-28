#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.KbdishCommRuleInfo import KbdishCommRuleInfo


class KoubeiCateringDishCommruleSyncResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiCateringDishCommruleSyncResponse, self).__init__()
        self._kbdish_comm_rule_info_list = None

    @property
    def kbdish_comm_rule_info_list(self):
        return self._kbdish_comm_rule_info_list

    @kbdish_comm_rule_info_list.setter
    def kbdish_comm_rule_info_list(self, value):
        if isinstance(value, list):
            self._kbdish_comm_rule_info_list = list()
            for i in value:
                if isinstance(i, KbdishCommRuleInfo):
                    self._kbdish_comm_rule_info_list.append(i)
                else:
                    self._kbdish_comm_rule_info_list.append(KbdishCommRuleInfo.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(KoubeiCateringDishCommruleSyncResponse, self).parse_response_content(response_content)
        if 'kbdish_comm_rule_info_list' in response:
            self.kbdish_comm_rule_info_list = response['kbdish_comm_rule_info_list']
