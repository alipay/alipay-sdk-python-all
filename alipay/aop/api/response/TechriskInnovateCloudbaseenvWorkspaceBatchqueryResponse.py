#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.WorkspaceVO import WorkspaceVO


class TechriskInnovateCloudbaseenvWorkspaceBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(TechriskInnovateCloudbaseenvWorkspaceBatchqueryResponse, self).__init__()
        self._workspace_list = None

    @property
    def workspace_list(self):
        return self._workspace_list

    @workspace_list.setter
    def workspace_list(self, value):
        if isinstance(value, list):
            self._workspace_list = list()
            for i in value:
                if isinstance(i, WorkspaceVO):
                    self._workspace_list.append(i)
                else:
                    self._workspace_list.append(WorkspaceVO.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(TechriskInnovateCloudbaseenvWorkspaceBatchqueryResponse, self).parse_response_content(response_content)
        if 'workspace_list' in response:
            self.workspace_list = response['workspace_list']
