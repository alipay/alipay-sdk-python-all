#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.YxContactInfo import YxContactInfo


class AlipayIserviceCcmCrmYxcustomerModifyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayIserviceCcmCrmYxcustomerModifyResponse, self).__init__()
        self._contact_info_list = None
        self._data_id = None

    @property
    def contact_info_list(self):
        return self._contact_info_list

    @contact_info_list.setter
    def contact_info_list(self, value):
        if isinstance(value, list):
            self._contact_info_list = list()
            for i in value:
                if isinstance(i, YxContactInfo):
                    self._contact_info_list.append(i)
                else:
                    self._contact_info_list.append(YxContactInfo.from_alipay_dict(i))
    @property
    def data_id(self):
        return self._data_id

    @data_id.setter
    def data_id(self, value):
        self._data_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayIserviceCcmCrmYxcustomerModifyResponse, self).parse_response_content(response_content)
        if 'contact_info_list' in response:
            self.contact_info_list = response['contact_info_list']
        if 'data_id' in response:
            self.data_id = response['data_id']
