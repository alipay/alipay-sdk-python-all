#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.RelationNodeInfo import RelationNodeInfo


class ZhimaCreditEpDossierRelationQueryResponse(AlipayResponse):

    def __init__(self):
        super(ZhimaCreditEpDossierRelationQueryResponse, self).__init__()
        self._relation_node_list = None

    @property
    def relation_node_list(self):
        return self._relation_node_list

    @relation_node_list.setter
    def relation_node_list(self, value):
        if isinstance(value, list):
            self._relation_node_list = list()
            for i in value:
                if isinstance(i, RelationNodeInfo):
                    self._relation_node_list.append(i)
                else:
                    self._relation_node_list.append(RelationNodeInfo.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(ZhimaCreditEpDossierRelationQueryResponse, self).parse_response_content(response_content)
        if 'relation_node_list' in response:
            self.relation_node_list = response['relation_node_list']
