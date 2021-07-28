#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.QuestInstanceDO import QuestInstanceDO


class AlipaySocialBaseQuestInstanceAddResponse(AlipayResponse):

    def __init__(self):
        super(AlipaySocialBaseQuestInstanceAddResponse, self).__init__()
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
        response = super(AlipaySocialBaseQuestInstanceAddResponse, self).parse_response_content(response_content)
        if 'instance' in response:
            self.instance = response['instance']
