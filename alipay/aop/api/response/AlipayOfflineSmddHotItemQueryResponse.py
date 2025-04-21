#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.DiscountActivityBean import DiscountActivityBean


class AlipayOfflineSmddHotItemQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOfflineSmddHotItemQueryResponse, self).__init__()
        self._activity_list = None

    @property
    def activity_list(self):
        return self._activity_list

    @activity_list.setter
    def activity_list(self, value):
        if isinstance(value, list):
            self._activity_list = list()
            for i in value:
                if isinstance(i, DiscountActivityBean):
                    self._activity_list.append(i)
                else:
                    self._activity_list.append(DiscountActivityBean.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayOfflineSmddHotItemQueryResponse, self).parse_response_content(response_content)
        if 'activity_list' in response:
            self.activity_list = response['activity_list']
