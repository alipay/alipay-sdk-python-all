#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.StageGroupInfoVO import StageGroupInfoVO


class AlipayCommerceEducateTrainStagecaterelationQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceEducateTrainStagecaterelationQueryResponse, self).__init__()
        self._stage_group_infos = None

    @property
    def stage_group_infos(self):
        return self._stage_group_infos

    @stage_group_infos.setter
    def stage_group_infos(self, value):
        if isinstance(value, list):
            self._stage_group_infos = list()
            for i in value:
                if isinstance(i, StageGroupInfoVO):
                    self._stage_group_infos.append(i)
                else:
                    self._stage_group_infos.append(StageGroupInfoVO.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceEducateTrainStagecaterelationQueryResponse, self).parse_response_content(response_content)
        if 'stage_group_infos' in response:
            self.stage_group_infos = response['stage_group_infos']
