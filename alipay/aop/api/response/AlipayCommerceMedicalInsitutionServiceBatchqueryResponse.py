#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.OrgOperationalAggregateItem import OrgOperationalAggregateItem


class AlipayCommerceMedicalInsitutionServiceBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalInsitutionServiceBatchqueryResponse, self).__init__()
        self._org_operational_metric_list = None

    @property
    def org_operational_metric_list(self):
        return self._org_operational_metric_list

    @org_operational_metric_list.setter
    def org_operational_metric_list(self, value):
        if isinstance(value, list):
            self._org_operational_metric_list = list()
            for i in value:
                if isinstance(i, OrgOperationalAggregateItem):
                    self._org_operational_metric_list.append(i)
                else:
                    self._org_operational_metric_list.append(OrgOperationalAggregateItem.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalInsitutionServiceBatchqueryResponse, self).parse_response_content(response_content)
        if 'org_operational_metric_list' in response:
            self.org_operational_metric_list = response['org_operational_metric_list']
