#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayEbppCommunityRelationshipCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEbppCommunityRelationshipCreateResponse, self).__init__()
        self._relationship_id = None

    @property
    def relationship_id(self):
        return self._relationship_id

    @relationship_id.setter
    def relationship_id(self, value):
        self._relationship_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayEbppCommunityRelationshipCreateResponse, self).parse_response_content(response_content)
        if 'relationship_id' in response:
            self.relationship_id = response['relationship_id']
