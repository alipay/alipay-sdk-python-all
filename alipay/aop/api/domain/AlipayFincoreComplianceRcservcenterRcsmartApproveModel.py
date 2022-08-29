#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.RcsmartCommonAppInfo import RcsmartCommonAppInfo
from alipay.aop.api.domain.RcsmartCommonApprovalReq import RcsmartCommonApprovalReq


class AlipayFincoreComplianceRcservcenterRcsmartApproveModel(object):

    def __init__(self):
        self._app_info = None
        self._commercialization_approval_req = None

    @property
    def app_info(self):
        return self._app_info

    @app_info.setter
    def app_info(self, value):
        if isinstance(value, RcsmartCommonAppInfo):
            self._app_info = value
        else:
            self._app_info = RcsmartCommonAppInfo.from_alipay_dict(value)
    @property
    def commercialization_approval_req(self):
        return self._commercialization_approval_req

    @commercialization_approval_req.setter
    def commercialization_approval_req(self, value):
        if isinstance(value, RcsmartCommonApprovalReq):
            self._commercialization_approval_req = value
        else:
            self._commercialization_approval_req = RcsmartCommonApprovalReq.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.app_info:
            if hasattr(self.app_info, 'to_alipay_dict'):
                params['app_info'] = self.app_info.to_alipay_dict()
            else:
                params['app_info'] = self.app_info
        if self.commercialization_approval_req:
            if hasattr(self.commercialization_approval_req, 'to_alipay_dict'):
                params['commercialization_approval_req'] = self.commercialization_approval_req.to_alipay_dict()
            else:
                params['commercialization_approval_req'] = self.commercialization_approval_req
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayFincoreComplianceRcservcenterRcsmartApproveModel()
        if 'app_info' in d:
            o.app_info = d['app_info']
        if 'commercialization_approval_req' in d:
            o.commercialization_approval_req = d['commercialization_approval_req']
        return o


