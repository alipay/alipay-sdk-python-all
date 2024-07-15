#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.SiteSelectionTask import SiteSelectionTask


class AlipayCommerceTransportChargerSiteselectionBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceTransportChargerSiteselectionBatchqueryResponse, self).__init__()
        self._tasks = None

    @property
    def tasks(self):
        return self._tasks

    @tasks.setter
    def tasks(self, value):
        if isinstance(value, list):
            self._tasks = list()
            for i in value:
                if isinstance(i, SiteSelectionTask):
                    self._tasks.append(i)
                else:
                    self._tasks.append(SiteSelectionTask.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceTransportChargerSiteselectionBatchqueryResponse, self).parse_response_content(response_content)
        if 'tasks' in response:
            self.tasks = response['tasks']
