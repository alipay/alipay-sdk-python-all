#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ObArtifacOnlineVersionQueryResponse(object):

    def __init__(self):
        self._artifact_id = None
        self._online_version = None

    @property
    def artifact_id(self):
        return self._artifact_id

    @artifact_id.setter
    def artifact_id(self, value):
        self._artifact_id = value
    @property
    def online_version(self):
        return self._online_version

    @online_version.setter
    def online_version(self, value):
        self._online_version = value


    def to_alipay_dict(self):
        params = dict()
        if self.artifact_id:
            if hasattr(self.artifact_id, 'to_alipay_dict'):
                params['artifact_id'] = self.artifact_id.to_alipay_dict()
            else:
                params['artifact_id'] = self.artifact_id
        if self.online_version:
            if hasattr(self.online_version, 'to_alipay_dict'):
                params['online_version'] = self.online_version.to_alipay_dict()
            else:
                params['online_version'] = self.online_version
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ObArtifacOnlineVersionQueryResponse()
        if 'artifact_id' in d:
            o.artifact_id = d['artifact_id']
        if 'online_version' in d:
            o.online_version = d['online_version']
        return o


