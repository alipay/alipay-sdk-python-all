#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.MpcLogisticsOrderResult import MpcLogisticsOrderResult


class AlipayCloudCloudpromoMallLogisticsBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCloudCloudpromoMallLogisticsBatchqueryResponse, self).__init__()
        self._mpc_logistics = None

    @property
    def mpc_logistics(self):
        return self._mpc_logistics

    @mpc_logistics.setter
    def mpc_logistics(self, value):
        if isinstance(value, list):
            self._mpc_logistics = list()
            for i in value:
                if isinstance(i, MpcLogisticsOrderResult):
                    self._mpc_logistics.append(i)
                else:
                    self._mpc_logistics.append(MpcLogisticsOrderResult.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayCloudCloudpromoMallLogisticsBatchqueryResponse, self).parse_response_content(response_content)
        if 'mpc_logistics' in response:
            self.mpc_logistics = response['mpc_logistics']
