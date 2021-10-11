#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ZftSubMerchantOrder(object):

    def __init__(self):
        self._app_pre_auth = None
        self._apply_time = None
        self._apply_type = None
        self._card_alias_no = None
        self._external_id = None
        self._face_pre_auth = None
        self._fk_audit = None
        self._fk_audit_memo = None
        self._is_face_limit = None
        self._kz_audit = None
        self._kz_audit_memo = None
        self._merchant_name = None
        self._order_id = None
        self._reason = None
        self._smid = None
        self._status = None
        self._sub_confirm = None

    @property
    def app_pre_auth(self):
        return self._app_pre_auth

    @app_pre_auth.setter
    def app_pre_auth(self, value):
        self._app_pre_auth = value
    @property
    def apply_time(self):
        return self._apply_time

    @apply_time.setter
    def apply_time(self, value):
        self._apply_time = value
    @property
    def apply_type(self):
        return self._apply_type

    @apply_type.setter
    def apply_type(self, value):
        self._apply_type = value
    @property
    def card_alias_no(self):
        return self._card_alias_no

    @card_alias_no.setter
    def card_alias_no(self, value):
        self._card_alias_no = value
    @property
    def external_id(self):
        return self._external_id

    @external_id.setter
    def external_id(self, value):
        self._external_id = value
    @property
    def face_pre_auth(self):
        return self._face_pre_auth

    @face_pre_auth.setter
    def face_pre_auth(self, value):
        self._face_pre_auth = value
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
    def is_face_limit(self):
        return self._is_face_limit

    @is_face_limit.setter
    def is_face_limit(self, value):
        self._is_face_limit = value
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
    def merchant_name(self):
        return self._merchant_name

    @merchant_name.setter
    def merchant_name(self, value):
        self._merchant_name = value
    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        self._order_id = value
    @property
    def reason(self):
        return self._reason

    @reason.setter
    def reason(self, value):
        self._reason = value
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
        if self.app_pre_auth:
            if hasattr(self.app_pre_auth, 'to_alipay_dict'):
                params['app_pre_auth'] = self.app_pre_auth.to_alipay_dict()
            else:
                params['app_pre_auth'] = self.app_pre_auth
        if self.apply_time:
            if hasattr(self.apply_time, 'to_alipay_dict'):
                params['apply_time'] = self.apply_time.to_alipay_dict()
            else:
                params['apply_time'] = self.apply_time
        if self.apply_type:
            if hasattr(self.apply_type, 'to_alipay_dict'):
                params['apply_type'] = self.apply_type.to_alipay_dict()
            else:
                params['apply_type'] = self.apply_type
        if self.card_alias_no:
            if hasattr(self.card_alias_no, 'to_alipay_dict'):
                params['card_alias_no'] = self.card_alias_no.to_alipay_dict()
            else:
                params['card_alias_no'] = self.card_alias_no
        if self.external_id:
            if hasattr(self.external_id, 'to_alipay_dict'):
                params['external_id'] = self.external_id.to_alipay_dict()
            else:
                params['external_id'] = self.external_id
        if self.face_pre_auth:
            if hasattr(self.face_pre_auth, 'to_alipay_dict'):
                params['face_pre_auth'] = self.face_pre_auth.to_alipay_dict()
            else:
                params['face_pre_auth'] = self.face_pre_auth
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
        if self.is_face_limit:
            if hasattr(self.is_face_limit, 'to_alipay_dict'):
                params['is_face_limit'] = self.is_face_limit.to_alipay_dict()
            else:
                params['is_face_limit'] = self.is_face_limit
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
        if self.merchant_name:
            if hasattr(self.merchant_name, 'to_alipay_dict'):
                params['merchant_name'] = self.merchant_name.to_alipay_dict()
            else:
                params['merchant_name'] = self.merchant_name
        if self.order_id:
            if hasattr(self.order_id, 'to_alipay_dict'):
                params['order_id'] = self.order_id.to_alipay_dict()
            else:
                params['order_id'] = self.order_id
        if self.reason:
            if hasattr(self.reason, 'to_alipay_dict'):
                params['reason'] = self.reason.to_alipay_dict()
            else:
                params['reason'] = self.reason
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
        o = ZftSubMerchantOrder()
        if 'app_pre_auth' in d:
            o.app_pre_auth = d['app_pre_auth']
        if 'apply_time' in d:
            o.apply_time = d['apply_time']
        if 'apply_type' in d:
            o.apply_type = d['apply_type']
        if 'card_alias_no' in d:
            o.card_alias_no = d['card_alias_no']
        if 'external_id' in d:
            o.external_id = d['external_id']
        if 'face_pre_auth' in d:
            o.face_pre_auth = d['face_pre_auth']
        if 'fk_audit' in d:
            o.fk_audit = d['fk_audit']
        if 'fk_audit_memo' in d:
            o.fk_audit_memo = d['fk_audit_memo']
        if 'is_face_limit' in d:
            o.is_face_limit = d['is_face_limit']
        if 'kz_audit' in d:
            o.kz_audit = d['kz_audit']
        if 'kz_audit_memo' in d:
            o.kz_audit_memo = d['kz_audit_memo']
        if 'merchant_name' in d:
            o.merchant_name = d['merchant_name']
        if 'order_id' in d:
            o.order_id = d['order_id']
        if 'reason' in d:
            o.reason = d['reason']
        if 'smid' in d:
            o.smid = d['smid']
        if 'status' in d:
            o.status = d['status']
        if 'sub_confirm' in d:
            o.sub_confirm = d['sub_confirm']
        return o


