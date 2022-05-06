#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.IotIdentityOrgQueryAllApiResponse import IotIdentityOrgQueryAllApiResponse


class IotIdentityOrgQueryAllListApiResponse(object):

    def __init__(self):
        self._orgs = None

    @property
    def orgs(self):
        return self._orgs

    @orgs.setter
    def orgs(self, value):
        if isinstance(value, list):
            self._orgs = list()
            for i in value:
                if isinstance(i, IotIdentityOrgQueryAllApiResponse):
                    self._orgs.append(i)
                else:
                    self._orgs.append(IotIdentityOrgQueryAllApiResponse.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.orgs:
            if isinstance(self.orgs, list):
                for i in range(0, len(self.orgs)):
                    element = self.orgs[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.orgs[i] = element.to_alipay_dict()
            if hasattr(self.orgs, 'to_alipay_dict'):
                params['orgs'] = self.orgs.to_alipay_dict()
            else:
                params['orgs'] = self.orgs
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = IotIdentityOrgQueryAllListApiResponse()
        if 'orgs' in d:
            o.orgs = d['orgs']
        return o


