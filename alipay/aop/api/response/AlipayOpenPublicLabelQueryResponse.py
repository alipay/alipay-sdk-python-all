#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.PublicLabel import PublicLabel


class AlipayOpenPublicLabelQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenPublicLabelQueryResponse, self).__init__()
        self._label_list = None

    @property
    def label_list(self):
        return self._label_list

    @label_list.setter
    def label_list(self, value):
        if isinstance(value, list):
            self._label_list = list()
            for i in value:
                if isinstance(i, PublicLabel):
                    self._label_list.append(i)
                else:
                    self._label_list.append(PublicLabel.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayOpenPublicLabelQueryResponse, self).parse_response_content(response_content)
        if 'label_list' in response:
            self.label_list = response['label_list']
