#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.DecisionExtInfo import DecisionExtInfo
from alipay.aop.api.domain.UserAccessInfo import UserAccessInfo


class AlipayMerchantOrderSnssmsaccessQueryModel(object):

    def __init__(self):
        self._activity_code = None
        self._decision_ext_info = None
        self._user_access_info = None

    @property
    def activity_code(self):
        return self._activity_code

    @activity_code.setter
    def activity_code(self, value):
        self._activity_code = value
    @property
    def decision_ext_info(self):
        return self._decision_ext_info

    @decision_ext_info.setter
    def decision_ext_info(self, value):
        if isinstance(value, DecisionExtInfo):
            self._decision_ext_info = value
        else:
            self._decision_ext_info = DecisionExtInfo.from_alipay_dict(value)
    @property
    def user_access_info(self):
        return self._user_access_info

    @user_access_info.setter
    def user_access_info(self, value):
        if isinstance(value, UserAccessInfo):
            self._user_access_info = value
        else:
            self._user_access_info = UserAccessInfo.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.activity_code:
            if hasattr(self.activity_code, 'to_alipay_dict'):
                params['activity_code'] = self.activity_code.to_alipay_dict()
            else:
                params['activity_code'] = self.activity_code
        if self.decision_ext_info:
            if hasattr(self.decision_ext_info, 'to_alipay_dict'):
                params['decision_ext_info'] = self.decision_ext_info.to_alipay_dict()
            else:
                params['decision_ext_info'] = self.decision_ext_info
        if self.user_access_info:
            if hasattr(self.user_access_info, 'to_alipay_dict'):
                params['user_access_info'] = self.user_access_info.to_alipay_dict()
            else:
                params['user_access_info'] = self.user_access_info
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayMerchantOrderSnssmsaccessQueryModel()
        if 'activity_code' in d:
            o.activity_code = d['activity_code']
        if 'decision_ext_info' in d:
            o.decision_ext_info = d['decision_ext_info']
        if 'user_access_info' in d:
            o.user_access_info = d['user_access_info']
        return o


