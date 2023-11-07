#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AnttechOceanbaseObglobalArtifactQueryModel(object):

    def __init__(self):
        self._query_artifact_project_names_request = None

    @property
    def query_artifact_project_names_request(self):
        return self._query_artifact_project_names_request

    @query_artifact_project_names_request.setter
    def query_artifact_project_names_request(self, value):
        self._query_artifact_project_names_request = value


    def to_alipay_dict(self):
        params = dict()
        if self.query_artifact_project_names_request:
            if hasattr(self.query_artifact_project_names_request, 'to_alipay_dict'):
                params['query_artifact_project_names_request'] = self.query_artifact_project_names_request.to_alipay_dict()
            else:
                params['query_artifact_project_names_request'] = self.query_artifact_project_names_request
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AnttechOceanbaseObglobalArtifactQueryModel()
        if 'query_artifact_project_names_request' in d:
            o.query_artifact_project_names_request = d['query_artifact_project_names_request']
        return o


