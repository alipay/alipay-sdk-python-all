#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayIserviceIcontrolDispatchQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayIserviceIcontrolDispatchQueryResponse, self).__init__()
        self._skill_group_id = None

    @property
    def skill_group_id(self):
        return self._skill_group_id

    @skill_group_id.setter
    def skill_group_id(self, value):
        self._skill_group_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayIserviceIcontrolDispatchQueryResponse, self).parse_response_content(response_content)
        if 'skill_group_id' in response:
            self.skill_group_id = response['skill_group_id']
