#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ExternalCateProperty import ExternalCateProperty


class AlipayInsSceneInshealthserviceprodCategorypropertyQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayInsSceneInshealthserviceprodCategorypropertyQueryResponse, self).__init__()
        self._properties = None

    @property
    def properties(self):
        return self._properties

    @properties.setter
    def properties(self, value):
        if isinstance(value, list):
            self._properties = list()
            for i in value:
                if isinstance(i, ExternalCateProperty):
                    self._properties.append(i)
                else:
                    self._properties.append(ExternalCateProperty.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayInsSceneInshealthserviceprodCategorypropertyQueryResponse, self).parse_response_content(response_content)
        if 'properties' in response:
            self.properties = response['properties']
