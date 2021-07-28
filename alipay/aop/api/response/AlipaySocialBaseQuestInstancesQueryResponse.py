#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.QuestInstanceDTO import QuestInstanceDTO


class AlipaySocialBaseQuestInstancesQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipaySocialBaseQuestInstancesQueryResponse, self).__init__()
        self._instances = None

    @property
    def instances(self):
        return self._instances

    @instances.setter
    def instances(self, value):
        if isinstance(value, list):
            self._instances = list()
            for i in value:
                if isinstance(i, QuestInstanceDTO):
                    self._instances.append(i)
                else:
                    self._instances.append(QuestInstanceDTO.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipaySocialBaseQuestInstancesQueryResponse, self).parse_response_content(response_content)
        if 'instances' in response:
            self.instances = response['instances']
