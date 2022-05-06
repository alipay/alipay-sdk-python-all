#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceEducateSceneFacegroupQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceEducateSceneFacegroupQueryResponse, self).__init__()
        self._school_group_id = None

    @property
    def school_group_id(self):
        return self._school_group_id

    @school_group_id.setter
    def school_group_id(self, value):
        self._school_group_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceEducateSceneFacegroupQueryResponse, self).parse_response_content(response_content)
        if 'school_group_id' in response:
            self.school_group_id = response['school_group_id']
