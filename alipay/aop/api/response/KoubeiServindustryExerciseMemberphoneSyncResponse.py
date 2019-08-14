#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ExerciseUserMappingDTO import ExerciseUserMappingDTO


class KoubeiServindustryExerciseMemberphoneSyncResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiServindustryExerciseMemberphoneSyncResponse, self).__init__()
        self._mapping_list = None

    @property
    def mapping_list(self):
        return self._mapping_list

    @mapping_list.setter
    def mapping_list(self, value):
        if isinstance(value, list):
            self._mapping_list = list()
            for i in value:
                if isinstance(i, ExerciseUserMappingDTO):
                    self._mapping_list.append(i)
                else:
                    self._mapping_list.append(ExerciseUserMappingDTO.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(KoubeiServindustryExerciseMemberphoneSyncResponse, self).parse_response_content(response_content)
        if 'mapping_list' in response:
            self.mapping_list = response['mapping_list']
