#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.WorkspaceResourceUsage import WorkspaceResourceUsage


class AlipayCloudCloudbaseEnvResourceusageGetResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCloudCloudbaseEnvResourceusageGetResponse, self).__init__()
        self._workspace_resource_usages = None

    @property
    def workspace_resource_usages(self):
        return self._workspace_resource_usages

    @workspace_resource_usages.setter
    def workspace_resource_usages(self, value):
        if isinstance(value, list):
            self._workspace_resource_usages = list()
            for i in value:
                if isinstance(i, WorkspaceResourceUsage):
                    self._workspace_resource_usages.append(i)
                else:
                    self._workspace_resource_usages.append(WorkspaceResourceUsage.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayCloudCloudbaseEnvResourceusageGetResponse, self).parse_response_content(response_content)
        if 'workspace_resource_usages' in response:
            self.workspace_resource_usages = response['workspace_resource_usages']
