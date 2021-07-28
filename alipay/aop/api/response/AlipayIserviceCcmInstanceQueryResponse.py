#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.Instance import Instance


class AlipayIserviceCcmInstanceQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayIserviceCcmInstanceQueryResponse, self).__init__()
        self._instances = None
        self._page_num = None
        self._page_size = None
        self._total_count = None

    @property
    def instances(self):
        return self._instances

    @instances.setter
    def instances(self, value):
        if isinstance(value, list):
            self._instances = list()
            for i in value:
                if isinstance(i, Instance):
                    self._instances.append(i)
                else:
                    self._instances.append(Instance.from_alipay_dict(i))
    @property
    def page_num(self):
        return self._page_num

    @page_num.setter
    def page_num(self, value):
        self._page_num = value
    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, value):
        self._page_size = value
    @property
    def total_count(self):
        return self._total_count

    @total_count.setter
    def total_count(self, value):
        self._total_count = value

    def parse_response_content(self, response_content):
        response = super(AlipayIserviceCcmInstanceQueryResponse, self).parse_response_content(response_content)
        if 'instances' in response:
            self.instances = response['instances']
        if 'page_num' in response:
            self.page_num = response['page_num']
        if 'page_size' in response:
            self.page_size = response['page_size']
        if 'total_count' in response:
            self.total_count = response['total_count']
