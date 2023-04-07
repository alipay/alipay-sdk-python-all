#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ObArtifactSyncDTO import ObArtifactSyncDTO


class AnttechOceanbaseObglobalObartifactSyncModel(object):

    def __init__(self):
        self._ob_artifacts = None

    @property
    def ob_artifacts(self):
        return self._ob_artifacts

    @ob_artifacts.setter
    def ob_artifacts(self, value):
        if isinstance(value, list):
            self._ob_artifacts = list()
            for i in value:
                if isinstance(i, ObArtifactSyncDTO):
                    self._ob_artifacts.append(i)
                else:
                    self._ob_artifacts.append(ObArtifactSyncDTO.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.ob_artifacts:
            if isinstance(self.ob_artifacts, list):
                for i in range(0, len(self.ob_artifacts)):
                    element = self.ob_artifacts[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.ob_artifacts[i] = element.to_alipay_dict()
            if hasattr(self.ob_artifacts, 'to_alipay_dict'):
                params['ob_artifacts'] = self.ob_artifacts.to_alipay_dict()
            else:
                params['ob_artifacts'] = self.ob_artifacts
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AnttechOceanbaseObglobalObartifactSyncModel()
        if 'ob_artifacts' in d:
            o.ob_artifacts = d['ob_artifacts']
        return o


