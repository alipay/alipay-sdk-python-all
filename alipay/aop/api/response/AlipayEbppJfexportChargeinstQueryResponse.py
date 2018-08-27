#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.JfExportChargeInstModel import JfExportChargeInstModel


class AlipayEbppJfexportChargeinstQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEbppJfexportChargeinstQueryResponse, self).__init__()
        self._charge_insts = None
        self._total_count = None

    @property
    def charge_insts(self):
        return self._charge_insts

    @charge_insts.setter
    def charge_insts(self, value):
        if isinstance(value, list):
            self._charge_insts = list()
            for i in value:
                if isinstance(i, JfExportChargeInstModel):
                    self._charge_insts.append(i)
                else:
                    self._charge_insts.append(JfExportChargeInstModel.from_alipay_dict(i))
    @property
    def total_count(self):
        return self._total_count

    @total_count.setter
    def total_count(self, value):
        self._total_count = value

    def parse_response_content(self, response_content):
        response = super(AlipayEbppJfexportChargeinstQueryResponse, self).parse_response_content(response_content)
        if 'charge_insts' in response:
            self.charge_insts = response['charge_insts']
        if 'total_count' in response:
            self.total_count = response['total_count']
