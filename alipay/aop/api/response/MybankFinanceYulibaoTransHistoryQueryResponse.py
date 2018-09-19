#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.YLBTransDetailInfo import YLBTransDetailInfo


class MybankFinanceYulibaoTransHistoryQueryResponse(AlipayResponse):

    def __init__(self):
        super(MybankFinanceYulibaoTransHistoryQueryResponse, self).__init__()
        self._current_page = None
        self._has_next_page = None
        self._history_trans_detail_infos = None
        self._total_item_count = None

    @property
    def current_page(self):
        return self._current_page

    @current_page.setter
    def current_page(self, value):
        self._current_page = value
    @property
    def has_next_page(self):
        return self._has_next_page

    @has_next_page.setter
    def has_next_page(self, value):
        self._has_next_page = value
    @property
    def history_trans_detail_infos(self):
        return self._history_trans_detail_infos

    @history_trans_detail_infos.setter
    def history_trans_detail_infos(self, value):
        if isinstance(value, list):
            self._history_trans_detail_infos = list()
            for i in value:
                if isinstance(i, YLBTransDetailInfo):
                    self._history_trans_detail_infos.append(i)
                else:
                    self._history_trans_detail_infos.append(YLBTransDetailInfo.from_alipay_dict(i))
    @property
    def total_item_count(self):
        return self._total_item_count

    @total_item_count.setter
    def total_item_count(self, value):
        self._total_item_count = value

    def parse_response_content(self, response_content):
        response = super(MybankFinanceYulibaoTransHistoryQueryResponse, self).parse_response_content(response_content)
        if 'current_page' in response:
            self.current_page = response['current_page']
        if 'has_next_page' in response:
            self.has_next_page = response['has_next_page']
        if 'history_trans_detail_infos' in response:
            self.history_trans_detail_infos = response['history_trans_detail_infos']
        if 'total_item_count' in response:
            self.total_item_count = response['total_item_count']
