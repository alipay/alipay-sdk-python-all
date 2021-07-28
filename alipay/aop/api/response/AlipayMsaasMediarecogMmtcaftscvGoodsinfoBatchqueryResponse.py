#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.AlgorithmGoodsInfo import AlgorithmGoodsInfo


class AlipayMsaasMediarecogMmtcaftscvGoodsinfoBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMsaasMediarecogMmtcaftscvGoodsinfoBatchqueryResponse, self).__init__()
        self._goods_infos = None

    @property
    def goods_infos(self):
        return self._goods_infos

    @goods_infos.setter
    def goods_infos(self, value):
        if isinstance(value, list):
            self._goods_infos = list()
            for i in value:
                if isinstance(i, AlgorithmGoodsInfo):
                    self._goods_infos.append(i)
                else:
                    self._goods_infos.append(AlgorithmGoodsInfo.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayMsaasMediarecogMmtcaftscvGoodsinfoBatchqueryResponse, self).parse_response_content(response_content)
        if 'goods_infos' in response:
            self.goods_infos = response['goods_infos']
