#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceOperationZftApplyresultSubmitModel(object):

    def __init__(self):
        self._apply_time = None
        self._external_id = None
        self._fail_reason = None
        self._fk_audit = None
        self._fk_audit_memo = None
        self._kz_audit = None
        self._kz_audit_memo = None
        self._order_id = None
        self._smid = None
        self._status = None
        self._sub_confirm = None

    @property
    def apply_time(self):
        return self._apply_time

    @apply_time.setter
    def apply_time(self, value):
        self._apply_time = value
    @property
    def external_id(self):
        return self._external_id

    @external_id.setter
    def external_id(self, value):
        self._external_id = value
    @property
    def fail_reason(self):
        return self._fail_reason

    @fail_reason.setter
    def fail_reason(self, value):
        self._fail_reason = value
    @property
    def fk_audit(self):
        return self._fk_audit

    @fk_audit.setter
    def fk_audit(self, value):
        self._fk_audit = value
    @property
    def fk_audit_memo(self):
        return self._fk_audit_memo

    @fk_audit_memo.setter
    def fk_audit_memo(self, value):
        self._fk_audit_memo = value
    @property
    def kz_audit(self):
        return self._kz_audit

    @kz_audit.setter
    def kz_audit(self, value):
        self._kz_audit = value
    @property
    def kz_audit_memo(self):
        return self._kz_audit_memo

    @kz_audit_memo.setter
    def kz_audit_memo(self, value):
        self._kz_audit_memo = value
    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        self._order_id = value
    @property
    def smid(self):
        return self._smid

    @smid.setter
    def smid(self, value):
        self._smid = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def sub_confirm(self):
        return self._sub_confirm

    @sub_confirm.setter
    def sub_confirm(self, value):
        self._sub_confirm = value


    def to_alipay_dict(self):
        params = dict()
        if self.apply_time:
            if hasattr(self.apply_time, 'to_alipay_dict'):
                params['apply_time'] = self.apply_time.to_alipay_dict()
            else:
                params['apply_time'] = self.apply_time
        if self.external_id:
            if hasattr(self.external_id, 'to_alipay_dict'):
                params['external_id'] = self.external_id.to_alipay_dict()
            else:
                params['external_id'] = self.external_id
        if self.fail_reason:
            if hasattr(self.fail_reason, 'to_alipay_dict'):
                params['fail_reason'] = self.fail_reason.to_alipay_dict()
            else:
                params['fail_reason'] = self.fail_reason
        if self.fk_audit:
            if hasattr(self.fk_audit, 'to_alipay_dict'):
                params['fk_audit'] = self.fk_audit.to_alipay_dict()
            else:
                params['fk_audit'] = self.fk_audit
        if self.fk_audit_memo:
            if hasattr(self.fk_audit_memo, 'to_alipay_dict'):
                params['fk_audit_memo'] = self.fk_audit_memo.to_alipay_dict()
            else:
                params['fk_audit_memo'] = self.fk_audit_memo
        if self.kz_audit:
            if hasattr(self.kz_audit, 'to_alipay_dict'):
                params['kz_audit'] = self.kz_audit.to_alipay_dict()
            else:
                params['kz_audit'] = self.kz_audit
        if self.kz_audit_memo:
            if hasattr(self.kz_audit_memo, 'to_alipay_dict'):
                params['kz_audit_memo'] = self.kz_audit_memo.to_alipay_dict()
            else:
                params['kz_audit_memo'] = self.kz_audit_memo
        if self.order_id:
            if hasattr(self.order_id, 'to_alipay_dict'):
                params['order_id'] = self.order_id.to_alipay_dict()
            else:
                params['order_id'] = self.order_id
        if self.smid:
            if hasattr(self.smid, 'to_alipay_dict'):
                params['smid'] = self.smid.to_alipay_dict()
            else:
                params['smid'] = self.smid
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.sub_confirm:
            if hasattr(self.sub_confirm, 'to_alipay_dict'):
                params['sub_confirm'] = self.sub_confirm.to_alipay_dict()
            else:
                params['sub_confirm'] = self.sub_confirm
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceOperationZftApplyresultSubmitModel()
        if 'apply_time' in d:
            o.apply_time = d['apply_time']
        if 'external_id' in d:
            o.external_id = d['external_id']
        if 'fail_reason' in d:
            o.fail_reason = d['fail_reason']
        if 'fk_audit' in d:
            o.fk_audit = d['fk_audit']
        if 'fk_audit_memo' in d:
            o.fk_audit_memo = d['fk_audit_memo']
        if 'kz_audit' in d:
            o.kz_audit = d['kz_audit']
        if 'kz_audit_memo' in d:
            o.kz_audit_memo = d['kz_audit_memo']
        if 'order_id' in d:
            o.order_id = d['order_id']
        if 'smid' in d:
            o.smid = d['smid']
        if 'status' in d:
            o.status = d['status']
        if 'sub_confirm' in d:
            o.sub_confirm = d['sub_confirm']
        return o


