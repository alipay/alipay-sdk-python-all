#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.SpuInfoVO import SpuInfoVO


class AlipayOpenAppItemCatespuQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenAppItemCatespuQueryResponse, self).__init__()
        self._page_num = None
        self._page_size = None
        self._spu_infos = None
        self._total = None

    @property
    def page_num(self):
        return self._page_num

    @page_num.setter
    def page_num(self, value):
        self._page_num = value
    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, value):
        self._page_size = value
    @property
    def spu_infos(self):
        return self._spu_infos

    @spu_infos.setter
    def spu_infos(self, value):
        if isinstance(value, list):
            self._spu_infos = list()
            for i in value:
                if isinstance(i, SpuInfoVO):
                    self._spu_infos.append(i)
                else:
                    self._spu_infos.append(SpuInfoVO.from_alipay_dict(i))
    @property
    def total(self):
        return self._total

    @total.setter
    def total(self, value):
        self._total = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenAppItemCatespuQueryResponse, self).parse_response_content(response_content)
        if 'page_num' in response:
            self.page_num = response['page_num']
        if 'page_size' in response:
            self.page_size = response['page_size']
        if 'spu_infos' in response:
            self.spu_infos = response['spu_infos']
        if 'total' in response:
            self.total = response['total']
