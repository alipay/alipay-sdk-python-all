#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.TreeData import TreeData


class AlipaySocialForestTreeQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipaySocialForestTreeQueryResponse, self).__init__()
        self._forest_status = None
        self._tree_datas = None

    @property
    def forest_status(self):
        return self._forest_status

    @forest_status.setter
    def forest_status(self, value):
        self._forest_status = value
    @property
    def tree_datas(self):
        return self._tree_datas

    @tree_datas.setter
    def tree_datas(self, value):
        if isinstance(value, list):
            self._tree_datas = list()
            for i in value:
                if isinstance(i, TreeData):
                    self._tree_datas.append(i)
                else:
                    self._tree_datas.append(TreeData.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipaySocialForestTreeQueryResponse, self).parse_response_content(response_content)
        if 'forest_status' in response:
            self.forest_status = response['forest_status']
        if 'tree_datas' in response:
            self.tree_datas = response['tree_datas']
