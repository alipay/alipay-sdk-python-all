#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.DeviceGroup import DeviceGroup


class AlipayCommerceIotGroupBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceIotGroupBatchqueryResponse, self).__init__()
        self._groups = None
        self._total = None

    @property
    def groups(self):
        return self._groups

    @groups.setter
    def groups(self, value):
        if isinstance(value, list):
            self._groups = list()
            for i in value:
                if isinstance(i, DeviceGroup):
                    self._groups.append(i)
                else:
                    self._groups.append(DeviceGroup.from_alipay_dict(i))
    @property
    def total(self):
        return self._total

    @total.setter
    def total(self, value):
        if isinstance(value, list):
            self._total = list()
            for i in value:
                self._total.append(i)

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceIotGroupBatchqueryResponse, self).parse_response_content(response_content)
        if 'groups' in response:
            self.groups = response['groups']
        if 'total' in response:
            self.total = response['total']
