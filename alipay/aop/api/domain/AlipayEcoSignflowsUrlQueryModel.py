#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEcoSignflowsUrlQueryModel(object):

    def __init__(self):
        self._flow_id = None
        self._org_third_party_user_id = None
        self._third_party_user_id = None

    @property
    def flow_id(self):
        return self._flow_id

    @flow_id.setter
    def flow_id(self, value):
        self._flow_id = value
    @property
    def org_third_party_user_id(self):
        return self._org_third_party_user_id

    @org_third_party_user_id.setter
    def org_third_party_user_id(self, value):
        self._org_third_party_user_id = value
    @property
    def third_party_user_id(self):
        return self._third_party_user_id

    @third_party_user_id.setter
    def third_party_user_id(self, value):
        self._third_party_user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.flow_id:
            if hasattr(self.flow_id, 'to_alipay_dict'):
                params['flow_id'] = self.flow_id.to_alipay_dict()
            else:
                params['flow_id'] = self.flow_id
        if self.org_third_party_user_id:
            if hasattr(self.org_third_party_user_id, 'to_alipay_dict'):
                params['org_third_party_user_id'] = self.org_third_party_user_id.to_alipay_dict()
            else:
                params['org_third_party_user_id'] = self.org_third_party_user_id
        if self.third_party_user_id:
            if hasattr(self.third_party_user_id, 'to_alipay_dict'):
                params['third_party_user_id'] = self.third_party_user_id.to_alipay_dict()
            else:
                params['third_party_user_id'] = self.third_party_user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEcoSignflowsUrlQueryModel()
        if 'flow_id' in d:
            o.flow_id = d['flow_id']
        if 'org_third_party_user_id' in d:
            o.org_third_party_user_id = d['org_third_party_user_id']
        if 'third_party_user_id' in d:
            o.third_party_user_id = d['third_party_user_id']
        return o


