#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.BcGroupClusterDetail import BcGroupClusterDetail


class AlipaySocialBaseBcClusterQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipaySocialBaseBcClusterQueryResponse, self).__init__()
        self._cluster_details = None

    @property
    def cluster_details(self):
        return self._cluster_details

    @cluster_details.setter
    def cluster_details(self, value):
        if isinstance(value, list):
            self._cluster_details = list()
            for i in value:
                if isinstance(i, BcGroupClusterDetail):
                    self._cluster_details.append(i)
                else:
                    self._cluster_details.append(BcGroupClusterDetail.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipaySocialBaseBcClusterQueryResponse, self).parse_response_content(response_content)
        if 'cluster_details' in response:
            self.cluster_details = response['cluster_details']
