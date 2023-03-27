#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.MpcpormoDataCheckInfo import MpcpormoDataCheckInfo


class TechriskInnovateMpcpromoDataSyncResponse(AlipayResponse):

    def __init__(self):
        super(TechriskInnovateMpcpromoDataSyncResponse, self).__init__()
        self._check_info_list = None

    @property
    def check_info_list(self):
        return self._check_info_list

    @check_info_list.setter
    def check_info_list(self, value):
        if isinstance(value, list):
            self._check_info_list = list()
            for i in value:
                if isinstance(i, MpcpormoDataCheckInfo):
                    self._check_info_list.append(i)
                else:
                    self._check_info_list.append(MpcpormoDataCheckInfo.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(TechriskInnovateMpcpromoDataSyncResponse, self).parse_response_content(response_content)
        if 'check_info_list' in response:
            self.check_info_list = response['check_info_list']
