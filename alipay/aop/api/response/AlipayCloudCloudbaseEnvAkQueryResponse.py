#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.WorkspaceAk import WorkspaceAk


class AlipayCloudCloudbaseEnvAkQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCloudCloudbaseEnvAkQueryResponse, self).__init__()
        self._aks = None
        self._page_index = None
        self._page_size = None
        self._total = None

    @property
    def aks(self):
        return self._aks

    @aks.setter
    def aks(self, value):
        if isinstance(value, list):
            self._aks = list()
            for i in value:
                if isinstance(i, WorkspaceAk):
                    self._aks.append(i)
                else:
                    self._aks.append(WorkspaceAk.from_alipay_dict(i))
    @property
    def page_index(self):
        return self._page_index

    @page_index.setter
    def page_index(self, value):
        self._page_index = value
    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, value):
        self._page_size = value
    @property
    def total(self):
        return self._total

    @total.setter
    def total(self, value):
        self._total = value

    def parse_response_content(self, response_content):
        response = super(AlipayCloudCloudbaseEnvAkQueryResponse, self).parse_response_content(response_content)
        if 'aks' in response:
            self.aks = response['aks']
        if 'page_index' in response:
            self.page_index = response['page_index']
        if 'page_size' in response:
            self.page_size = response['page_size']
        if 'total' in response:
            self.total = response['total']
