#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipaySocialAntforestProjectQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipaySocialAntforestProjectQueryResponse, self).__init__()
        self._projects = None

    @property
    def projects(self):
        return self._projects

    @projects.setter
    def projects(self, value):
        if isinstance(value, list):
            self._projects = list()
            for i in value:
                self._projects.append(i)

    def parse_response_content(self, response_content):
        response = super(AlipaySocialAntforestProjectQueryResponse, self).parse_response_content(response_content)
        if 'projects' in response:
            self.projects = response['projects']
