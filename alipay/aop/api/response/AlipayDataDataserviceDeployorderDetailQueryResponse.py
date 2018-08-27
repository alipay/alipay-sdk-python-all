#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.DxDeployOrderInfo import DxDeployOrderInfo


class AlipayDataDataserviceDeployorderDetailQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayDataDataserviceDeployorderDetailQueryResponse, self).__init__()
        self._deploy_order_list = None

    @property
    def deploy_order_list(self):
        return self._deploy_order_list

    @deploy_order_list.setter
    def deploy_order_list(self, value):
        if isinstance(value, list):
            self._deploy_order_list = list()
            for i in value:
                if isinstance(i, DxDeployOrderInfo):
                    self._deploy_order_list.append(i)
                else:
                    self._deploy_order_list.append(DxDeployOrderInfo.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayDataDataserviceDeployorderDetailQueryResponse, self).parse_response_content(response_content)
        if 'deploy_order_list' in response:
            self.deploy_order_list = response['deploy_order_list']
