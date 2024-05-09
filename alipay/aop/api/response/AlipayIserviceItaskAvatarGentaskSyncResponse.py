#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.AvatarHumanTaskResultDTO import AvatarHumanTaskResultDTO


class AlipayIserviceItaskAvatarGentaskSyncResponse(AlipayResponse):

    def __init__(self):
        super(AlipayIserviceItaskAvatarGentaskSyncResponse, self).__init__()
        self._avatar_task_result = None

    @property
    def avatar_task_result(self):
        return self._avatar_task_result

    @avatar_task_result.setter
    def avatar_task_result(self, value):
        if isinstance(value, AvatarHumanTaskResultDTO):
            self._avatar_task_result = value
        else:
            self._avatar_task_result = AvatarHumanTaskResultDTO.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayIserviceItaskAvatarGentaskSyncResponse, self).parse_response_content(response_content)
        if 'avatar_task_result' in response:
            self.avatar_task_result = response['avatar_task_result']
