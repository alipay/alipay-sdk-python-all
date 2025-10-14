#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.TourOrderSyncResponse import TourOrderSyncResponse
from alipay.aop.api.domain.TourOrderSyncFailureDetail import TourOrderSyncFailureDetail


class AlipayCommerceTransportTourOrderSyncResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceTransportTourOrderSyncResponse, self).__init__()
        self._success_order_list = None
        self._sync_failure_detail_list = None
        self._un_sync_order_no_list = None

    @property
    def success_order_list(self):
        return self._success_order_list

    @success_order_list.setter
    def success_order_list(self, value):
        if isinstance(value, list):
            self._success_order_list = list()
            for i in value:
                if isinstance(i, TourOrderSyncResponse):
                    self._success_order_list.append(i)
                else:
                    self._success_order_list.append(TourOrderSyncResponse.from_alipay_dict(i))
    @property
    def sync_failure_detail_list(self):
        return self._sync_failure_detail_list

    @sync_failure_detail_list.setter
    def sync_failure_detail_list(self, value):
        if isinstance(value, list):
            self._sync_failure_detail_list = list()
            for i in value:
                if isinstance(i, TourOrderSyncFailureDetail):
                    self._sync_failure_detail_list.append(i)
                else:
                    self._sync_failure_detail_list.append(TourOrderSyncFailureDetail.from_alipay_dict(i))
    @property
    def un_sync_order_no_list(self):
        return self._un_sync_order_no_list

    @un_sync_order_no_list.setter
    def un_sync_order_no_list(self, value):
        self._un_sync_order_no_list = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceTransportTourOrderSyncResponse, self).parse_response_content(response_content)
        if 'success_order_list' in response:
            self.success_order_list = response['success_order_list']
        if 'sync_failure_detail_list' in response:
            self.sync_failure_detail_list = response['sync_failure_detail_list']
        if 'un_sync_order_no_list' in response:
            self.un_sync_order_no_list = response['un_sync_order_no_list']
