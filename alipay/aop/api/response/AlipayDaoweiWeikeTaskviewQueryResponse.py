#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.WeikeTaskView import WeikeTaskView


class AlipayDaoweiWeikeTaskviewQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayDaoweiWeikeTaskviewQueryResponse, self).__init__()
        self._task_views = None

    @property
    def task_views(self):
        return self._task_views

    @task_views.setter
    def task_views(self, value):
        if isinstance(value, list):
            self._task_views = list()
            for i in value:
                if isinstance(i, WeikeTaskView):
                    self._task_views.append(i)
                else:
                    self._task_views.append(WeikeTaskView.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayDaoweiWeikeTaskviewQueryResponse, self).parse_response_content(response_content)
        if 'task_views' in response:
            self.task_views = response['task_views']
