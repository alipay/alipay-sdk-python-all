#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.RelationCombinedVO import RelationCombinedVO


class AlipaySocialBaseRelationCombinedQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipaySocialBaseRelationCombinedQueryResponse, self).__init__()
        self._relation_combined_list = None

    @property
    def relation_combined_list(self):
        return self._relation_combined_list

    @relation_combined_list.setter
    def relation_combined_list(self, value):
        if isinstance(value, list):
            self._relation_combined_list = list()
            for i in value:
                if isinstance(i, RelationCombinedVO):
                    self._relation_combined_list.append(i)
                else:
                    self._relation_combined_list.append(RelationCombinedVO.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipaySocialBaseRelationCombinedQueryResponse, self).parse_response_content(response_content)
        if 'relation_combined_list' in response:
            self.relation_combined_list = response['relation_combined_list']
