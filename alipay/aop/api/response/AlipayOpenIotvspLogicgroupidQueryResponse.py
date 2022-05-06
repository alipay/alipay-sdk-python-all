#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenIotvspLogicgroupidQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenIotvspLogicgroupidQueryResponse, self).__init__()
        self._logic_group_id = None

    @property
    def logic_group_id(self):
        return self._logic_group_id

    @logic_group_id.setter
    def logic_group_id(self, value):
        self._logic_group_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenIotvspLogicgroupidQueryResponse, self).parse_response_content(response_content)
        if 'logic_group_id' in response:
            self.logic_group_id = response['logic_group_id']
