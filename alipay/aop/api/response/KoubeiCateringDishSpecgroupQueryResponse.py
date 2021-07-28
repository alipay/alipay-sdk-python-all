#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.KbdishSpecGroup import KbdishSpecGroup


class KoubeiCateringDishSpecgroupQueryResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiCateringDishSpecgroupQueryResponse, self).__init__()
        self._merchant_id = None
        self._spec_group_list = None

    @property
    def merchant_id(self):
        return self._merchant_id

    @merchant_id.setter
    def merchant_id(self, value):
        self._merchant_id = value
    @property
    def spec_group_list(self):
        return self._spec_group_list

    @spec_group_list.setter
    def spec_group_list(self, value):
        if isinstance(value, list):
            self._spec_group_list = list()
            for i in value:
                if isinstance(i, KbdishSpecGroup):
                    self._spec_group_list.append(i)
                else:
                    self._spec_group_list.append(KbdishSpecGroup.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(KoubeiCateringDishSpecgroupQueryResponse, self).parse_response_content(response_content)
        if 'merchant_id' in response:
            self.merchant_id = response['merchant_id']
        if 'spec_group_list' in response:
            self.spec_group_list = response['spec_group_list']
