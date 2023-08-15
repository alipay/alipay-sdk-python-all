#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.MpcpromoGoodsList import MpcpromoGoodsList


class TechriskInnovateMpcpromoDataQueryResponse(AlipayResponse):

    def __init__(self):
        super(TechriskInnovateMpcpromoDataQueryResponse, self).__init__()
        self._goods_list = None

    @property
    def goods_list(self):
        return self._goods_list

    @goods_list.setter
    def goods_list(self, value):
        if isinstance(value, list):
            self._goods_list = list()
            for i in value:
                if isinstance(i, MpcpromoGoodsList):
                    self._goods_list.append(i)
                else:
                    self._goods_list.append(MpcpromoGoodsList.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(TechriskInnovateMpcpromoDataQueryResponse, self).parse_response_content(response_content)
        if 'goods_list' in response:
            self.goods_list = response['goods_list']
