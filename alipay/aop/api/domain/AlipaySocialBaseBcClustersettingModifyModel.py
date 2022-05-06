#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipaySocialBaseBcClustersettingModifyModel(object):

    def __init__(self):
        self._cluster_id = None
        self._notice = None
        self._operate_business_id = None
        self._tenant_id = None
        self._welcome_msg = None

    @property
    def cluster_id(self):
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, value):
        self._cluster_id = value
    @property
    def notice(self):
        return self._notice

    @notice.setter
    def notice(self, value):
        self._notice = value
    @property
    def operate_business_id(self):
        return self._operate_business_id

    @operate_business_id.setter
    def operate_business_id(self, value):
        self._operate_business_id = value
    @property
    def tenant_id(self):
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, value):
        self._tenant_id = value
    @property
    def welcome_msg(self):
        return self._welcome_msg

    @welcome_msg.setter
    def welcome_msg(self, value):
        self._welcome_msg = value


    def to_alipay_dict(self):
        params = dict()
        if self.cluster_id:
            if hasattr(self.cluster_id, 'to_alipay_dict'):
                params['cluster_id'] = self.cluster_id.to_alipay_dict()
            else:
                params['cluster_id'] = self.cluster_id
        if self.notice:
            if hasattr(self.notice, 'to_alipay_dict'):
                params['notice'] = self.notice.to_alipay_dict()
            else:
                params['notice'] = self.notice
        if self.operate_business_id:
            if hasattr(self.operate_business_id, 'to_alipay_dict'):
                params['operate_business_id'] = self.operate_business_id.to_alipay_dict()
            else:
                params['operate_business_id'] = self.operate_business_id
        if self.tenant_id:
            if hasattr(self.tenant_id, 'to_alipay_dict'):
                params['tenant_id'] = self.tenant_id.to_alipay_dict()
            else:
                params['tenant_id'] = self.tenant_id
        if self.welcome_msg:
            if hasattr(self.welcome_msg, 'to_alipay_dict'):
                params['welcome_msg'] = self.welcome_msg.to_alipay_dict()
            else:
                params['welcome_msg'] = self.welcome_msg
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipaySocialBaseBcClustersettingModifyModel()
        if 'cluster_id' in d:
            o.cluster_id = d['cluster_id']
        if 'notice' in d:
            o.notice = d['notice']
        if 'operate_business_id' in d:
            o.operate_business_id = d['operate_business_id']
        if 'tenant_id' in d:
            o.tenant_id = d['tenant_id']
        if 'welcome_msg' in d:
            o.welcome_msg = d['welcome_msg']
        return o


