#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.SubscribeRelation import SubscribeRelation


class AlipayOpenAppMessagetemplateSubscribeQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenAppMessagetemplateSubscribeQueryResponse, self).__init__()
        self._show_component = None
        self._subscribe_relations = None

    @property
    def show_component(self):
        return self._show_component

    @show_component.setter
    def show_component(self, value):
        self._show_component = value
    @property
    def subscribe_relations(self):
        return self._subscribe_relations

    @subscribe_relations.setter
    def subscribe_relations(self, value):
        if isinstance(value, list):
            self._subscribe_relations = list()
            for i in value:
                if isinstance(i, SubscribeRelation):
                    self._subscribe_relations.append(i)
                else:
                    self._subscribe_relations.append(SubscribeRelation.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayOpenAppMessagetemplateSubscribeQueryResponse, self).parse_response_content(response_content)
        if 'show_component' in response:
            self.show_component = response['show_component']
        if 'subscribe_relations' in response:
            self.subscribe_relations = response['subscribe_relations']
