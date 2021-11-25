#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ActivityLiteInfo import ActivityLiteInfo


class AlipayMarketingActivityBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMarketingActivityBatchqueryResponse, self).__init__()
        self._activity_lite_infos = None
        self._page_num = None
        self._page_size = None
        self._total_size = None

    @property
    def activity_lite_infos(self):
        return self._activity_lite_infos

    @activity_lite_infos.setter
    def activity_lite_infos(self, value):
        if isinstance(value, list):
            self._activity_lite_infos = list()
            for i in value:
                if isinstance(i, ActivityLiteInfo):
                    self._activity_lite_infos.append(i)
                else:
                    self._activity_lite_infos.append(ActivityLiteInfo.from_alipay_dict(i))
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
        response = super(AlipayMarketingActivityBatchqueryResponse, self).parse_response_content(response_content)
        if 'activity_lite_infos' in response:
            self.activity_lite_infos = response['activity_lite_infos']
        if 'page_num' in response:
            self.page_num = response['page_num']
        if 'page_size' in response:
            self.page_size = response['page_size']
        if 'total_size' in response:
            self.total_size = response['total_size']
