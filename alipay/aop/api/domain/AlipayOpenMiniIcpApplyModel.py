#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.IcpAppletsInfo import IcpAppletsInfo
from alipay.aop.api.domain.IcpAppletsPrincipalInfo import IcpAppletsPrincipalInfo
from alipay.aop.api.domain.IcpSubjectInfo import IcpSubjectInfo


class AlipayOpenMiniIcpApplyModel(object):

    def __init__(self):
        self._icp_applets = None
        self._icp_applets_principal_info = None
        self._icp_subject = None

    @property
    def icp_applets(self):
        return self._icp_applets

    @icp_applets.setter
    def icp_applets(self, value):
        if isinstance(value, IcpAppletsInfo):
            self._icp_applets = value
        else:
            self._icp_applets = IcpAppletsInfo.from_alipay_dict(value)
    @property
    def icp_applets_principal_info(self):
        return self._icp_applets_principal_info

    @icp_applets_principal_info.setter
    def icp_applets_principal_info(self, value):
        if isinstance(value, IcpAppletsPrincipalInfo):
            self._icp_applets_principal_info = value
        else:
            self._icp_applets_principal_info = IcpAppletsPrincipalInfo.from_alipay_dict(value)
    @property
    def icp_subject(self):
        return self._icp_subject

    @icp_subject.setter
    def icp_subject(self, value):
        if isinstance(value, IcpSubjectInfo):
            self._icp_subject = value
        else:
            self._icp_subject = IcpSubjectInfo.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.icp_applets:
            if hasattr(self.icp_applets, 'to_alipay_dict'):
                params['icp_applets'] = self.icp_applets.to_alipay_dict()
            else:
                params['icp_applets'] = self.icp_applets
        if self.icp_applets_principal_info:
            if hasattr(self.icp_applets_principal_info, 'to_alipay_dict'):
                params['icp_applets_principal_info'] = self.icp_applets_principal_info.to_alipay_dict()
            else:
                params['icp_applets_principal_info'] = self.icp_applets_principal_info
        if self.icp_subject:
            if hasattr(self.icp_subject, 'to_alipay_dict'):
                params['icp_subject'] = self.icp_subject.to_alipay_dict()
            else:
                params['icp_subject'] = self.icp_subject
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenMiniIcpApplyModel()
        if 'icp_applets' in d:
            o.icp_applets = d['icp_applets']
        if 'icp_applets_principal_info' in d:
            o.icp_applets_principal_info = d['icp_applets_principal_info']
        if 'icp_subject' in d:
            o.icp_subject = d['icp_subject']
        return o


