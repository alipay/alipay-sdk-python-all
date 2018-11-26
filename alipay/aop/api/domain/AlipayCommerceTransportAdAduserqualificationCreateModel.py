#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.AdUserQualification import AdUserQualification


class AlipayCommerceTransportAdAduserqualificationCreateModel(object):

    def __init__(self):
        self._ad_user_id = None
        self._ad_user_qualification = None

    @property
    def ad_user_id(self):
        return self._ad_user_id

    @ad_user_id.setter
    def ad_user_id(self, value):
        self._ad_user_id = value
    @property
    def ad_user_qualification(self):
        return self._ad_user_qualification

    @ad_user_qualification.setter
    def ad_user_qualification(self, value):
        if isinstance(value, AdUserQualification):
            self._ad_user_qualification = value
        else:
            self._ad_user_qualification = AdUserQualification.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.ad_user_id:
            if hasattr(self.ad_user_id, 'to_alipay_dict'):
                params['ad_user_id'] = self.ad_user_id.to_alipay_dict()
            else:
                params['ad_user_id'] = self.ad_user_id
        if self.ad_user_qualification:
            if hasattr(self.ad_user_qualification, 'to_alipay_dict'):
                params['ad_user_qualification'] = self.ad_user_qualification.to_alipay_dict()
            else:
                params['ad_user_qualification'] = self.ad_user_qualification
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceTransportAdAduserqualificationCreateModel()
        if 'ad_user_id' in d:
            o.ad_user_id = d['ad_user_id']
        if 'ad_user_qualification' in d:
            o.ad_user_qualification = d['ad_user_qualification']
        return o


