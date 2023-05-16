#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.FamilyPayQuotaInfo import FamilyPayQuotaInfo


class FamilyPayCardInfo(object):

    def __init__(self):
        self._agreement_no = None
        self._apply_no = None
        self._card_id = None
        self._gmt_valid = None
        self._out_biz_no = None
        self._payer_id = None
        self._payer_open_id = None
        self._quota = None
        self._quota_remain = None
        self._quota_used = None
        self._spender_id = None
        self._spender_open_id = None
        self._status = None

    @property
    def agreement_no(self):
        return self._agreement_no

    @agreement_no.setter
    def agreement_no(self, value):
        self._agreement_no = value
    @property
    def apply_no(self):
        return self._apply_no

    @apply_no.setter
    def apply_no(self, value):
        self._apply_no = value
    @property
    def card_id(self):
        return self._card_id

    @card_id.setter
    def card_id(self, value):
        self._card_id = value
    @property
    def gmt_valid(self):
        return self._gmt_valid

    @gmt_valid.setter
    def gmt_valid(self, value):
        self._gmt_valid = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def payer_id(self):
        return self._payer_id

    @payer_id.setter
    def payer_id(self, value):
        self._payer_id = value
    @property
    def payer_open_id(self):
        return self._payer_open_id

    @payer_open_id.setter
    def payer_open_id(self, value):
        self._payer_open_id = value
    @property
    def quota(self):
        return self._quota

    @quota.setter
    def quota(self, value):
        if isinstance(value, FamilyPayQuotaInfo):
            self._quota = value
        else:
            self._quota = FamilyPayQuotaInfo.from_alipay_dict(value)
    @property
    def quota_remain(self):
        return self._quota_remain

    @quota_remain.setter
    def quota_remain(self, value):
        self._quota_remain = value
    @property
    def quota_used(self):
        return self._quota_used

    @quota_used.setter
    def quota_used(self, value):
        self._quota_used = value
    @property
    def spender_id(self):
        return self._spender_id

    @spender_id.setter
    def spender_id(self, value):
        self._spender_id = value
    @property
    def spender_open_id(self):
        return self._spender_open_id

    @spender_open_id.setter
    def spender_open_id(self, value):
        self._spender_open_id = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value


    def to_alipay_dict(self):
        params = dict()
        if self.agreement_no:
            if hasattr(self.agreement_no, 'to_alipay_dict'):
                params['agreement_no'] = self.agreement_no.to_alipay_dict()
            else:
                params['agreement_no'] = self.agreement_no
        if self.apply_no:
            if hasattr(self.apply_no, 'to_alipay_dict'):
                params['apply_no'] = self.apply_no.to_alipay_dict()
            else:
                params['apply_no'] = self.apply_no
        if self.card_id:
            if hasattr(self.card_id, 'to_alipay_dict'):
                params['card_id'] = self.card_id.to_alipay_dict()
            else:
                params['card_id'] = self.card_id
        if self.gmt_valid:
            if hasattr(self.gmt_valid, 'to_alipay_dict'):
                params['gmt_valid'] = self.gmt_valid.to_alipay_dict()
            else:
                params['gmt_valid'] = self.gmt_valid
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.payer_id:
            if hasattr(self.payer_id, 'to_alipay_dict'):
                params['payer_id'] = self.payer_id.to_alipay_dict()
            else:
                params['payer_id'] = self.payer_id
        if self.payer_open_id:
            if hasattr(self.payer_open_id, 'to_alipay_dict'):
                params['payer_open_id'] = self.payer_open_id.to_alipay_dict()
            else:
                params['payer_open_id'] = self.payer_open_id
        if self.quota:
            if hasattr(self.quota, 'to_alipay_dict'):
                params['quota'] = self.quota.to_alipay_dict()
            else:
                params['quota'] = self.quota
        if self.quota_remain:
            if hasattr(self.quota_remain, 'to_alipay_dict'):
                params['quota_remain'] = self.quota_remain.to_alipay_dict()
            else:
                params['quota_remain'] = self.quota_remain
        if self.quota_used:
            if hasattr(self.quota_used, 'to_alipay_dict'):
                params['quota_used'] = self.quota_used.to_alipay_dict()
            else:
                params['quota_used'] = self.quota_used
        if self.spender_id:
            if hasattr(self.spender_id, 'to_alipay_dict'):
                params['spender_id'] = self.spender_id.to_alipay_dict()
            else:
                params['spender_id'] = self.spender_id
        if self.spender_open_id:
            if hasattr(self.spender_open_id, 'to_alipay_dict'):
                params['spender_open_id'] = self.spender_open_id.to_alipay_dict()
            else:
                params['spender_open_id'] = self.spender_open_id
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = FamilyPayCardInfo()
        if 'agreement_no' in d:
            o.agreement_no = d['agreement_no']
        if 'apply_no' in d:
            o.apply_no = d['apply_no']
        if 'card_id' in d:
            o.card_id = d['card_id']
        if 'gmt_valid' in d:
            o.gmt_valid = d['gmt_valid']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'payer_id' in d:
            o.payer_id = d['payer_id']
        if 'payer_open_id' in d:
            o.payer_open_id = d['payer_open_id']
        if 'quota' in d:
            o.quota = d['quota']
        if 'quota_remain' in d:
            o.quota_remain = d['quota_remain']
        if 'quota_used' in d:
            o.quota_used = d['quota_used']
        if 'spender_id' in d:
            o.spender_id = d['spender_id']
        if 'spender_open_id' in d:
            o.spender_open_id = d['spender_open_id']
        if 'status' in d:
            o.status = d['status']
        return o


