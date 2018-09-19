#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.LifeLabel import LifeLabel


class AlipayOpenPublicLifeLabelBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenPublicLifeLabelBatchqueryResponse, self).__init__()
        self._labels = None

    @property
    def labels(self):
        return self._labels

    @labels.setter
    def labels(self, value):
        if isinstance(value, list):
            self._labels = list()
            for i in value:
                if isinstance(i, LifeLabel):
                    self._labels.append(i)
                else:
                    self._labels.append(LifeLabel.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayOpenPublicLifeLabelBatchqueryResponse, self).parse_response_content(response_content)
        if 'labels' in response:
            self.labels = response['labels']
