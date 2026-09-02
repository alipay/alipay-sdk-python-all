#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ExternalItemLabel import ExternalItemLabel


class AlipayInsSceneInshealthserviceprodMalllabelQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayInsSceneInshealthserviceprodMalllabelQueryResponse, self).__init__()
        self._item_label_list = None

    @property
    def item_label_list(self):
        return self._item_label_list

    @item_label_list.setter
    def item_label_list(self, value):
        if isinstance(value, list):
            self._item_label_list = list()
            for i in value:
                if isinstance(i, ExternalItemLabel):
                    self._item_label_list.append(i)
                else:
                    self._item_label_list.append(ExternalItemLabel.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayInsSceneInshealthserviceprodMalllabelQueryResponse, self).parse_response_content(response_content)
        if 'item_label_list' in response:
            self.item_label_list = response['item_label_list']
