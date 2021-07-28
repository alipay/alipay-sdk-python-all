#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.TreeInfo import TreeInfo


class AlipayIserviceCcmSwTreeBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayIserviceCcmSwTreeBatchqueryResponse, self).__init__()
        self._trees = None

    @property
    def trees(self):
        return self._trees

    @trees.setter
    def trees(self, value):
        if isinstance(value, list):
            self._trees = list()
            for i in value:
                if isinstance(i, TreeInfo):
                    self._trees.append(i)
                else:
                    self._trees.append(TreeInfo.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayIserviceCcmSwTreeBatchqueryResponse, self).parse_response_content(response_content)
        if 'trees' in response:
            self.trees = response['trees']
