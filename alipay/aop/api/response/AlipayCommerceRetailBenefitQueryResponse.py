#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceRetailBenefitQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceRetailBenefitQueryResponse, self).__init__()
        self._activity_id_list = None
        self._total_num = None

    @property
    def activity_id_list(self):
        return self._activity_id_list

    @activity_id_list.setter
    def activity_id_list(self, value):
        if isinstance(value, list):
            self._activity_id_list = list()
            for i in value:
                self._activity_id_list.append(i)
    @property
    def total_num(self):
        return self._total_num

    @total_num.setter
    def total_num(self, value):
        self._total_num = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceRetailBenefitQueryResponse, self).parse_response_content(response_content)
        if 'activity_id_list' in response:
            self.activity_id_list = response['activity_id_list']
        if 'total_num' in response:
            self.total_num = response['total_num']
