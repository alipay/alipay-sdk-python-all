#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEcoEduJzApplyresultSyncModel(object):

    def __init__(self):
        self._apply_third_id = None
        self._audit_remark = None
        self._listing_status = None

    @property
    def apply_third_id(self):
        return self._apply_third_id

    @apply_third_id.setter
    def apply_third_id(self, value):
        self._apply_third_id = value
    @property
    def audit_remark(self):
        return self._audit_remark

    @audit_remark.setter
    def audit_remark(self, value):
        self._audit_remark = value
    @property
    def listing_status(self):
        return self._listing_status

    @listing_status.setter
    def listing_status(self, value):
        self._listing_status = value


    def to_alipay_dict(self):
        params = dict()
        if self.apply_third_id:
            if hasattr(self.apply_third_id, 'to_alipay_dict'):
                params['apply_third_id'] = self.apply_third_id.to_alipay_dict()
            else:
                params['apply_third_id'] = self.apply_third_id
        if self.audit_remark:
            if hasattr(self.audit_remark, 'to_alipay_dict'):
                params['audit_remark'] = self.audit_remark.to_alipay_dict()
            else:
                params['audit_remark'] = self.audit_remark
        if self.listing_status:
            if hasattr(self.listing_status, 'to_alipay_dict'):
                params['listing_status'] = self.listing_status.to_alipay_dict()
            else:
                params['listing_status'] = self.listing_status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEcoEduJzApplyresultSyncModel()
        if 'apply_third_id' in d:
            o.apply_third_id = d['apply_third_id']
        if 'audit_remark' in d:
            o.audit_remark = d['audit_remark']
        if 'listing_status' in d:
            o.listing_status = d['listing_status']
        return o


