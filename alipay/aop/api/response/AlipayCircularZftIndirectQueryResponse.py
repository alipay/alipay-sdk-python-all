#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ZftIndirectRelation import ZftIndirectRelation


class AlipayCircularZftIndirectQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCircularZftIndirectQueryResponse, self).__init__()
        self._relations = None

    @property
    def relations(self):
        return self._relations

    @relations.setter
    def relations(self, value):
        if isinstance(value, list):
            self._relations = list()
            for i in value:
                if isinstance(i, ZftIndirectRelation):
                    self._relations.append(i)
                else:
                    self._relations.append(ZftIndirectRelation.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayCircularZftIndirectQueryResponse, self).parse_response_content(response_content)
        if 'relations' in response:
            self.relations = response['relations']
