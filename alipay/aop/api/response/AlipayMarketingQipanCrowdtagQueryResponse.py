#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.CrowdSelectTagOpen import CrowdSelectTagOpen


class AlipayMarketingQipanCrowdtagQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMarketingQipanCrowdtagQueryResponse, self).__init__()
        self._select_tag_list = None

    @property
    def select_tag_list(self):
        return self._select_tag_list

    @select_tag_list.setter
    def select_tag_list(self, value):
        if isinstance(value, list):
            self._select_tag_list = list()
            for i in value:
                if isinstance(i, CrowdSelectTagOpen):
                    self._select_tag_list.append(i)
                else:
                    self._select_tag_list.append(CrowdSelectTagOpen.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayMarketingQipanCrowdtagQueryResponse, self).parse_response_content(response_content)
        if 'select_tag_list' in response:
            self.select_tag_list = response['select_tag_list']
