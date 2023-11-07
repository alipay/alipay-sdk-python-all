#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.RedisInstanceInfo import RedisInstanceInfo


class AlipayCloudCloudbaseRedisInstanceQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCloudCloudbaseRedisInstanceQueryResponse, self).__init__()
        self._instances = None

    @property
    def instances(self):
        return self._instances

    @instances.setter
    def instances(self, value):
        if isinstance(value, list):
            self._instances = list()
            for i in value:
                if isinstance(i, RedisInstanceInfo):
                    self._instances.append(i)
                else:
                    self._instances.append(RedisInstanceInfo.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayCloudCloudbaseRedisInstanceQueryResponse, self).parse_response_content(response_content)
        if 'instances' in response:
            self.instances = response['instances']
