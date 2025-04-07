#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.CategoryAttributeInfoVO import CategoryAttributeInfoVO
from alipay.aop.api.domain.ControlRuleVO import ControlRuleVO


class AlipayOpenAppItemCateattrQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenAppItemCateattrQueryResponse, self).__init__()
        self._cat_attr_list = None
        self._control_rule = None

    @property
    def cat_attr_list(self):
        return self._cat_attr_list

    @cat_attr_list.setter
    def cat_attr_list(self, value):
        if isinstance(value, list):
            self._cat_attr_list = list()
            for i in value:
                if isinstance(i, CategoryAttributeInfoVO):
                    self._cat_attr_list.append(i)
                else:
                    self._cat_attr_list.append(CategoryAttributeInfoVO.from_alipay_dict(i))
    @property
    def control_rule(self):
        return self._control_rule

    @control_rule.setter
    def control_rule(self, value):
        if isinstance(value, list):
            self._control_rule = list()
            for i in value:
                if isinstance(i, ControlRuleVO):
                    self._control_rule.append(i)
                else:
                    self._control_rule.append(ControlRuleVO.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayOpenAppItemCateattrQueryResponse, self).parse_response_content(response_content)
        if 'cat_attr_list' in response:
            self.cat_attr_list = response['cat_attr_list']
        if 'control_rule' in response:
            self.control_rule = response['control_rule']
