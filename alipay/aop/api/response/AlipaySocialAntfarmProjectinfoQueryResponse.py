#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.AntfarmProjectInfo import AntfarmProjectInfo


class AlipaySocialAntfarmProjectinfoQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipaySocialAntfarmProjectinfoQueryResponse, self).__init__()
        self._project_list = None

    @property
    def project_list(self):
        return self._project_list

    @project_list.setter
    def project_list(self, value):
        if isinstance(value, list):
            self._project_list = list()
            for i in value:
                if isinstance(i, AntfarmProjectInfo):
                    self._project_list.append(i)
                else:
                    self._project_list.append(AntfarmProjectInfo.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipaySocialAntfarmProjectinfoQueryResponse, self).parse_response_content(response_content)
        if 'project_list' in response:
            self.project_list = response['project_list']
