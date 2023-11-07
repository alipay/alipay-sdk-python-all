#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ObArtifactVersionQueryRequest(object):

    def __init__(self):
        self._artifact_name = None

    @property
    def artifact_name(self):
        return self._artifact_name

    @artifact_name.setter
    def artifact_name(self, value):
        self._artifact_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.artifact_name:
            if hasattr(self.artifact_name, 'to_alipay_dict'):
                params['artifact_name'] = self.artifact_name.to_alipay_dict()
            else:
                params['artifact_name'] = self.artifact_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ObArtifactVersionQueryRequest()
        if 'artifact_name' in d:
            o.artifact_name = d['artifact_name']
        return o


