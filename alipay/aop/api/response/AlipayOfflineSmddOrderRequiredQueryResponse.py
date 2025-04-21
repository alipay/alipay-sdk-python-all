#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.RequireBean import RequireBean


class AlipayOfflineSmddOrderRequiredQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOfflineSmddOrderRequiredQueryResponse, self).__init__()
        self._require_info_list = None

    @property
    def require_info_list(self):
        return self._require_info_list

    @require_info_list.setter
    def require_info_list(self, value):
        if isinstance(value, list):
            self._require_info_list = list()
            for i in value:
                if isinstance(i, RequireBean):
                    self._require_info_list.append(i)
                else:
                    self._require_info_list.append(RequireBean.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayOfflineSmddOrderRequiredQueryResponse, self).parse_response_content(response_content)
        if 'require_info_list' in response:
            self.require_info_list = response['require_info_list']
