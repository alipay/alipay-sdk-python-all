#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.KbdishRuleInfo import KbdishRuleInfo


class KoubeiCateringDishRuleQueryResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiCateringDishRuleQueryResponse, self).__init__()
        self._kb_dish_rule_info_list = None

    @property
    def kb_dish_rule_info_list(self):
        return self._kb_dish_rule_info_list

    @kb_dish_rule_info_list.setter
    def kb_dish_rule_info_list(self, value):
        if isinstance(value, list):
            self._kb_dish_rule_info_list = list()
            for i in value:
                if isinstance(i, KbdishRuleInfo):
                    self._kb_dish_rule_info_list.append(i)
                else:
                    self._kb_dish_rule_info_list.append(KbdishRuleInfo.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(KoubeiCateringDishRuleQueryResponse, self).parse_response_content(response_content)
        if 'kb_dish_rule_info_list' in response:
            self.kb_dish_rule_info_list = response['kb_dish_rule_info_list']
