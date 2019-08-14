#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.UserTaskView import UserTaskView


class AlipayMerchantWeikeSettleQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMerchantWeikeSettleQueryResponse, self).__init__()
        self._out_biz_no = None
        self._page_no = None
        self._page_size = None
        self._user_task_views = None

    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def page_no(self):
        return self._page_no

    @page_no.setter
    def page_no(self, value):
        self._page_no = value
    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, value):
        self._page_size = value
    @property
    def user_task_views(self):
        return self._user_task_views

    @user_task_views.setter
    def user_task_views(self, value):
        if isinstance(value, list):
            self._user_task_views = list()
            for i in value:
                if isinstance(i, UserTaskView):
                    self._user_task_views.append(i)
                else:
                    self._user_task_views.append(UserTaskView.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayMerchantWeikeSettleQueryResponse, self).parse_response_content(response_content)
        if 'out_biz_no' in response:
            self.out_biz_no = response['out_biz_no']
        if 'page_no' in response:
            self.page_no = response['page_no']
        if 'page_size' in response:
            self.page_size = response['page_size']
        if 'user_task_views' in response:
            self.user_task_views = response['user_task_views']
