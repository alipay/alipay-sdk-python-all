#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.QuestInstanceDO import QuestInstanceDO


class AlipaySocialBaseQuestInstanceModifyResponse(AlipayResponse):

    def __init__(self):
        super(AlipaySocialBaseQuestInstanceModifyResponse, self).__init__()
        self._instance = None

    @property
    def instance(self):
        return self._instance

    @instance.setter
    def instance(self, value):
        if isinstance(value, QuestInstanceDO):
            self._instance = value
        else:
            self._instance = QuestInstanceDO.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipaySocialBaseQuestInstanceModifyResponse, self).parse_response_content(response_content)
        if 'instance' in response:
            self.instance = response['instance']
