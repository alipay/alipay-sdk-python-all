#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ExternalCategoryTreeNode import ExternalCategoryTreeNode


class AlipayInsSceneInshealthserviceprodCategorytreeQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayInsSceneInshealthserviceprodCategorytreeQueryResponse, self).__init__()
        self._category_tree_list = None

    @property
    def category_tree_list(self):
        return self._category_tree_list

    @category_tree_list.setter
    def category_tree_list(self, value):
        if isinstance(value, ExternalCategoryTreeNode):
            self._category_tree_list = value
        else:
            self._category_tree_list = ExternalCategoryTreeNode.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayInsSceneInshealthserviceprodCategorytreeQueryResponse, self).parse_response_content(response_content)
        if 'category_tree_list' in response:
            self.category_tree_list = response['category_tree_list']
