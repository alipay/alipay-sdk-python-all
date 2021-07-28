#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.QuestInstanceDO import QuestInstanceDO


class AlipaySocialBaseQuestInstanceQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipaySocialBaseQuestInstanceQueryResponse, self).__init__()
        self._instances = None

    @property
    def instances(self):
        return self._instances

    @instances.setter
    def instances(self, value):
        if isinstance(value, list):
            self._instances = list()
            for i in value:
                if isinstance(i, QuestInstanceDO):
                    self._instances.append(i)
                else:
                    self._instances.append(QuestInstanceDO.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipaySocialBaseQuestInstanceQueryResponse, self).parse_response_content(response_content)
        if 'instances' in response:
            self.instances = response['instances']
