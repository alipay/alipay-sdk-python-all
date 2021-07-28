#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class KoubeiCateringDishSpecgroupSyncResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiCateringDishSpecgroupSyncResponse, self).__init__()
        self._kbdish_spec_group_id = None

    @property
    def kbdish_spec_group_id(self):
        return self._kbdish_spec_group_id

    @kbdish_spec_group_id.setter
    def kbdish_spec_group_id(self, value):
        self._kbdish_spec_group_id = value

    def parse_response_content(self, response_content):
        response = super(KoubeiCateringDishSpecgroupSyncResponse, self).parse_response_content(response_content)
        if 'kbdish_spec_group_id' in response:
            self.kbdish_spec_group_id = response['kbdish_spec_group_id']
