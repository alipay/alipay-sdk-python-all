#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.RetailActivityPointInfo import RetailActivityPointInfo


class AlipayCommerceRetailActivitypointsQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceRetailActivitypointsQueryResponse, self).__init__()
        self._activity_info = None
        self._total = None

    @property
    def activity_info(self):
        return self._activity_info

    @activity_info.setter
    def activity_info(self, value):
        if isinstance(value, list):
            self._activity_info = list()
            for i in value:
                if isinstance(i, RetailActivityPointInfo):
                    self._activity_info.append(i)
                else:
                    self._activity_info.append(RetailActivityPointInfo.from_alipay_dict(i))
    @property
    def total(self):
        return self._total

    @total.setter
    def total(self, value):
        self._total = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceRetailActivitypointsQueryResponse, self).parse_response_content(response_content)
        if 'activity_info' in response:
            self.activity_info = response['activity_info']
        if 'total' in response:
            self.total = response['total']
