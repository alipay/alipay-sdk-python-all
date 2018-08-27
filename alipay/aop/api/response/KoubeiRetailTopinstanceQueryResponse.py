#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.InstanceInfo import InstanceInfo


class KoubeiRetailTopinstanceQueryResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiRetailTopinstanceQueryResponse, self).__init__()
        self._instance_list = None
        self._total_count = None

    @property
    def instance_list(self):
        return self._instance_list

    @instance_list.setter
    def instance_list(self, value):
        if isinstance(value, list):
            self._instance_list = list()
            for i in value:
                if isinstance(i, InstanceInfo):
                    self._instance_list.append(i)
                else:
                    self._instance_list.append(InstanceInfo.from_alipay_dict(i))
    @property
    def total_count(self):
        return self._total_count

    @total_count.setter
    def total_count(self, value):
        self._total_count = value

    def parse_response_content(self, response_content):
        response = super(KoubeiRetailTopinstanceQueryResponse, self).parse_response_content(response_content)
        if 'instance_list' in response:
            self.instance_list = response['instance_list']
        if 'total_count' in response:
            self.total_count = response['total_count']
