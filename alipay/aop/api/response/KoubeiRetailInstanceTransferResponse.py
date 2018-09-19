#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class KoubeiRetailInstanceTransferResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiRetailInstanceTransferResponse, self).__init__()
        self._instance_id_list = None

    @property
    def instance_id_list(self):
        return self._instance_id_list

    @instance_id_list.setter
    def instance_id_list(self, value):
        if isinstance(value, list):
            self._instance_id_list = list()
            for i in value:
                self._instance_id_list.append(i)

    def parse_response_content(self, response_content):
        response = super(KoubeiRetailInstanceTransferResponse, self).parse_response_content(response_content)
        if 'instance_id_list' in response:
            self.instance_id_list = response['instance_id_list']
