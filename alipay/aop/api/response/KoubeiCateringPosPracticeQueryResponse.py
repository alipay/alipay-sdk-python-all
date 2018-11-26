#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.PracticeEntity import PracticeEntity


class KoubeiCateringPosPracticeQueryResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiCateringPosPracticeQueryResponse, self).__init__()
        self._practice_entity_list = None

    @property
    def practice_entity_list(self):
        return self._practice_entity_list

    @practice_entity_list.setter
    def practice_entity_list(self, value):
        if isinstance(value, list):
            self._practice_entity_list = list()
            for i in value:
                if isinstance(i, PracticeEntity):
                    self._practice_entity_list.append(i)
                else:
                    self._practice_entity_list.append(PracticeEntity.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(KoubeiCateringPosPracticeQueryResponse, self).parse_response_content(response_content)
        if 'practice_entity_list' in response:
            self.practice_entity_list = response['practice_entity_list']
