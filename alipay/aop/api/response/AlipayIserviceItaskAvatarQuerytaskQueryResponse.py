#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.AvatarHumanTaskResultDTO import AvatarHumanTaskResultDTO


class AlipayIserviceItaskAvatarQuerytaskQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayIserviceItaskAvatarQuerytaskQueryResponse, self).__init__()
        self._avatar_task_results = None

    @property
    def avatar_task_results(self):
        return self._avatar_task_results

    @avatar_task_results.setter
    def avatar_task_results(self, value):
        if isinstance(value, list):
            self._avatar_task_results = list()
            for i in value:
                if isinstance(i, AvatarHumanTaskResultDTO):
                    self._avatar_task_results.append(i)
                else:
                    self._avatar_task_results.append(AvatarHumanTaskResultDTO.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayIserviceItaskAvatarQuerytaskQueryResponse, self).parse_response_content(response_content)
        if 'avatar_task_results' in response:
            self.avatar_task_results = response['avatar_task_results']
