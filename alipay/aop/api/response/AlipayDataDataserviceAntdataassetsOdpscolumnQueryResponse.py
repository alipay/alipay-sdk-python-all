#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.AntdataassetsOdpsColumn import AntdataassetsOdpsColumn


class AlipayDataDataserviceAntdataassetsOdpscolumnQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayDataDataserviceAntdataassetsOdpscolumnQueryResponse, self).__init__()
        self._odps_columns = None

    @property
    def odps_columns(self):
        return self._odps_columns

    @odps_columns.setter
    def odps_columns(self, value):
        if isinstance(value, list):
            self._odps_columns = list()
            for i in value:
                if isinstance(i, AntdataassetsOdpsColumn):
                    self._odps_columns.append(i)
                else:
                    self._odps_columns.append(AntdataassetsOdpsColumn.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayDataDataserviceAntdataassetsOdpscolumnQueryResponse, self).parse_response_content(response_content)
        if 'odps_columns' in response:
            self.odps_columns = response['odps_columns']
