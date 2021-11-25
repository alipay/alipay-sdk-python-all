#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ActivityGoodsInfo import ActivityGoodsInfo


class AlipayMarketingActivityGoodsBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMarketingActivityGoodsBatchqueryResponse, self).__init__()
        self._activity_id = None
        self._goods_infos = None
        self._page_num = None
        self._page_size = None
        self._total_size = None

    @property
    def activity_id(self):
        return self._activity_id

    @activity_id.setter
    def activity_id(self, value):
        self._activity_id = value
    @property
    def goods_infos(self):
        return self._goods_infos

    @goods_infos.setter
    def goods_infos(self, value):
        if isinstance(value, list):
            self._goods_infos = list()
            for i in value:
                if isinstance(i, ActivityGoodsInfo):
                    self._goods_infos.append(i)
                else:
                    self._goods_infos.append(ActivityGoodsInfo.from_alipay_dict(i))
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
    def total_size(self):
        return self._total_size

    @total_size.setter
    def total_size(self, value):
        self._total_size = value

    def parse_response_content(self, response_content):
        response = super(AlipayMarketingActivityGoodsBatchqueryResponse, self).parse_response_content(response_content)
        if 'activity_id' in response:
            self.activity_id = response['activity_id']
        if 'goods_infos' in response:
            self.goods_infos = response['goods_infos']
        if 'page_num' in response:
            self.page_num = response['page_num']
        if 'page_size' in response:
            self.page_size = response['page_size']
        if 'total_size' in response:
            self.total_size = response['total_size']
